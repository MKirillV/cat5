data = {'admin': 'admin' , 'Катя': 59, 'Вася': 77}

secret = 'Очень важный секрет'


while True:
    log = input('Введите логин: ')
    pas = input('Введите пароль: ')


    try:
        if data[log] == pas:
            print(secret)
            break
        else:
            print("не правильный пароль")
    except:
        print("Не правильно введен логин или пароль")