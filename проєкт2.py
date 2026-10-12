users = {
    "Taras": {"password": "1234", "grades": [12, 10, 8, 11, 4, 3]},
    "Denis": {"password": "qwerty", "grades": [9, 7, 12, 5, 3]},
    "Ivan": {"password": "1111", "grades": [6, 8, 4, 10, 12]},
    "Petro": {"password": "2222", "grades": [5, 7, 2, 11, 4]}
}

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in users and password == users[login]["password"]:
    grades = users[login]["grades"]

    print("Вхід успішний!")
    print("Ваші оцінки:", grades)

    good = 0
    bad = 0

    for grade in grades:
        if 5 <= grade <= 12:
            good += 1
        elif 1 <= grade <= 4:
            bad += 1

    print("Задовільних оцінок:", good)
    print("Незадовільних оцінок:", bad)

else:
    print("Неправильний логін або пароль!")