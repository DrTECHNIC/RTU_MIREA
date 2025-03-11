import re


def task1():
    text = "Please contact us at support@example.com or sales@example.org for more information."
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
    print(emails)


def task2():
    text = "You can reach us at +7 (912) 345-67-89 or +7 (901) 234-56-78 during business hours."
    phone_numbers = re.findall(r'\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}', text)
    print(phone_numbers)


def task3():
    text = "Join the discussion on #python and share your thoughts on #regex. Don't forget to tag #coding!"
    hashtags = re.findall(r'#\w+', text)
    print(hashtags)


def task4():
    text = "Visit our website at https://example.com or check out http://test.org for more details."
    links = re.findall(r'http[s]?://\S+', text)
    print(links)


def task5():
    text = "The total cost is 150 dollars, but you can get a discount of 25 if you buy 3 items."
    numbers = re.findall(r'\d+', text)
    print(numbers)


def task6():
    text = "The project deadline is 15/10/2023, and the final review will be on 20/12/2023."
    datas = re.findall(r'\d{2}/\d{2}/\d{4}', text)
    print(datas)


def task7():
    text = "Python is a popular programming language. Learn Regex to improve your Skills."
    words = re.findall(r'[A-Z]\S+', text)
    print(words)


def task8():
    text = "The server IPs are 192.168.1.1, 10.0.0.1, and 8.8.8.8. Avoid using invalid IPs like 999.999.999.999."
    ip_addresses = re.findall(r'(?:25[0-5]|2[0-4]\d|1?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|1?\d\d?)', text)
    print(ip_addresses)


def task9():
    text = "The meeting starts at 14:30 and ends at 16:45. Please arrive by 14:15."
    times = re.findall(r'(?:2[0-3]|[01]?\d):[0-5][0-9]', text)
    print(times)


def task10():
    text = "She is singing and dancing while cooking dinner. The evening is full of fun activities."
    times = re.findall(r'[A-Za-z]+ing', text)
    print(times)


def task5_2():
    def decode_number(num):
        binary = bin(num)[2:].zfill(24)
        groups = [binary[i * 3:(i + 1) * 3] for i in range(8)]
        decoded = []
        for group in groups:
            decoded.append('1' if group.count('1') > 1 else '0')
        return int(''.join(decoded), 2)
    encoded = [815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031,
               1830912, 2067455, 2093116, 1044928, 2064407, 6262776, 2027968,
               4423680, 2068231, 2068474, 1999352, 1019903, 2093113, 2068439,
               2064455, 1831360, 1936903, 2067967, 2068456]
    message = ''.join([chr(decode_number(num)) for num in encoded])
    print(message)


if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()
    task5_2()
