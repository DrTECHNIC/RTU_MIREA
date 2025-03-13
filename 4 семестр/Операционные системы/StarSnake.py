import curses
import threading
import time
import random
import os
import signal

direction = None
running = True
snake = [(0, 0)]
food = (0, 0)
food_value = 1

def save_state(snake, direction, food):
    with open('state.txt', 'w') as f:
        f.write(f"{','.join(f'{x},{y}' for x, y in snake)},{direction},{food[0]},{food[1]}")

def load_state():
    try:
        with open('state.txt', 'r') as f:
            data = f.read().strip().split(',')
            snake = [(int(data[i]), int(data[i+1])) for i in range(0, len(data)-4, 2)]
            direction = data[-3]
            food = (int(data[-2]), int(data[-1]))
            return snake, direction, food
    except FileNotFoundError:
        return None, None, None

def is_opposite(new_dir, current_dir):
    opposites = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
    return opposites.get(new_dir) == current_dir

def place_food(stdscr, snake):
    height, width = stdscr.getmaxyx()
    while True:
        food = (random.randint(0, width-1), random.randint(0, height-1))
        if food not in snake:
            return food

def move_snake(stdscr):
    global direction, running, snake, food
    height, width = stdscr.getmaxyx()
    snake, direction, food = load_state()
    if not snake:
        snake = [(width // 2, height // 2)]
        direction = 'RIGHT'
        food = place_food(stdscr, snake)
    while running:
        stdscr.clear()
        for x, y in snake:
            stdscr.addch(y, x, '*')
        stdscr.addch(food[1], food[0], '@')
        stdscr.refresh()
        head_x, head_y = snake[0]
        if direction == 'UP':
            new_head = (head_x, (head_y - 1) % height)
            time.sleep(0.15)
        elif direction == 'DOWN':
            new_head = (head_x, (head_y + 1) % height)
            time.sleep(0.15)
        elif direction == 'LEFT':
            new_head = ((head_x - 1) % width, head_y)
            time.sleep(0.1)
        elif direction == 'RIGHT':
            new_head = ((head_x + 1) % width, head_y)
            time.sleep(0.1)
        if new_head in snake:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(height // 2, width // 2 - 5, "You lost! Press 'q' to quit.")
            stdscr.attroff(curses.color_pair(1))
            stdscr.refresh()
            while True:
                key = stdscr.getch()
                if key == ord('q'):
                    running = False
                    if os.path.exists('state.txt'):
                        os.remove('state.txt')
                    break
            break
        snake.insert(0, new_head)
        if new_head == food:
            for _ in range(food_value):
                snake.append(snake[-1])
            food = place_food(stdscr, snake)
        else:
            snake.pop()

def handle_sigint(signum, frame):
    global running
    running = False
    save_state(snake, direction, food)
    print("\nProgress saved. Exiting...")
    exit(0)

def main(stdscr):
    global direction, running, snake, food
    curses.curs_set(0)
    stdscr.keypad(True)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    snake, direction, food = load_state()
    if not snake:
        snake = [(stdscr.getmaxyx()[1] // 2, stdscr.getmaxyx()[0] // 2)]
        direction = 'RIGHT'
        food = place_food(stdscr, snake)
    signal.signal(signal.SIGINT, handle_sigint)
    move_thread = threading.Thread(target=move_snake, args=(stdscr,))
    move_thread.start()
    while True:
        key = stdscr.getch()
        new_dir = None
        if key == curses.KEY_UP:
            new_dir = 'UP'
        elif key == curses.KEY_DOWN:
            new_dir = 'DOWN'
        elif key == curses.KEY_LEFT:
            new_dir = 'LEFT'
        elif key == curses.KEY_RIGHT:
            new_dir = 'RIGHT'
        elif key == ord('q'):
            running = False
            move_thread.join()
            if os.path.exists('state.txt'):
                os.remove('state.txt')
            break
        if new_dir and not is_opposite(new_dir, direction):
            direction = new_dir

if __name__ == "__main__":
    curses.wrapper(main)