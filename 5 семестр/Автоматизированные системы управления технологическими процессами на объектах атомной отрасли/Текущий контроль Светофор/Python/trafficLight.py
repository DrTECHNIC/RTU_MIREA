import time

# Функция для проверки сигналов
def check_safety(true_signal, false_signal1, false_signal2):
    signals = [true_signal, false_signal1, false_signal2]
    active_count = sum(signals)
    if active_count != 1:
        raise Exception(f"КОНФЛИКТ СОСТОЯНИЙ! Активно сигналов: {active_count}.")
    return True


print("Светофор запущен (для остановки нажмите Ctrl+C)")
print("Цикл: 🔴 Красный -> 🟢 Зеленый -> 🟡 Желтый -> 🔴 Красный...")
print("Временные интервалы: 🔴 Красный = 30 сек., 🟡 Желтый = 5 сек., 🟢 Зеленый = 30 сек.")
print()
RLight = False; RTime = 30
YLight = False; YTime = 5
GLight = False; GTime = 30
try:
    while True:
        YLight = False
        RLight = True
        if check_safety(RLight, YLight, GLight):
            print(f"🔴 Красный")
            time.sleep(RTime)
        RLight = False
        GLight = True
        if check_safety(GLight, RLight, YLight):
            print(f"🟢 Зеленый")
            time.sleep(GTime)
        GLight = False
        YLight = True
        if check_safety(YLight, GLight, RLight):
            print(f"🟡 Желтый")
            time.sleep(YTime)
except KeyboardInterrupt:
    print("\n\nРабота светофора остановлена.")
except Exception as e:
    print(f"\n\nОШИБКА БЕЗОПАСНОСТИ: {e}")
