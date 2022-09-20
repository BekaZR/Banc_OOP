
from random import randint

def wellcome():
    print(
        '\nЗдравствуйте вас приветствует банк Континенталь\n'
    )
    

def help():
    print(
        'Введите:\n'
        '\n1 ~ если хотите открыть счет в банке\n'
        '2 ~ если хотите внести вклад\n'
        '3 ~ если хотите вывести деньги\n'
        '4 ~ если хотите увидеть ваш баланс\n'
        '5 ~ если хотите узнать ваши личные данные\n'
        )

def deposit_description():
    print(
        '\nНаш банк предлагает несколько видов депозита\n'
        '• Минимальная сумма вклада 1000 сом '
        '• Максимальная сумма вклада ∞ \n'
        '\nВведите:\n'
        '1 ~ под 0% без ограничения на вывод средств\n'
        '2 ~ под 6% на 6 месяцев \n'
        '3 ~ под 9.75% на 12 месяцев\n'
        '4 ~ под 10% на 36 месяцев\n'
        
    )


class BancAccount:
    a = 5
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.balance = 0
        self.count = randint(100000,1000000)
    
    def __str__(self):
        return f'\nваше имя {self.name}\nваша фамилия {self.surname}\nваш баланс {self.balance}\nваш лицевой счет {self.count}\n'


class TranceAction:
    def __init__(self, user):
        self.user = user
        
    def withdraw(self, summa):
        if self.user.balance < summa:
            print(
                '\nУ вас не достаточно средств\n'
            )
        else:
            self.user.balance = self.user.balance - summa
        
    def deposit_with_percent(self,summa,percent,month):
        self.user.balance = self.user.balance + (summa + ((percent * summa) * month))
        
    def __str__(self):
        f'ваш баланс {self.user.balance}'


names = {}
balance = {}

while True:
    command = input(
    '\nВведите help, что бы посмотреть команды для использования наших услуг\n'
    )
    if command == '1':
        wellcome()
        print(
        '\nВведите ваши имя и фамилию в нижнем регистре\n'
        )
        while True:
            name_surname = input().split()

            if len(name_surname) == 2:
                name = name_surname[0]
                surname = name_surname[1]

                names[name] = BancAccount(
                                        name.capitalize(), surname.capitalize()
                                            )
                balance[name] = TranceAction(names[name])
                
            else:
                print(
            '\nВы ввели не соответсвующие данные\n'
            'Введите еще раз\n'
                    )
                continue
            break

    elif command == '2':
        while True:
            name = input(
                'Введите имя адресанта на чей счет вы хотите положить средства '
            )
            if name in balance:
                deposit_description()
                
                while True:
                    deposit_command = input()
                    
                    if deposit_command == '1':
                        summa = input(
                        '\nВведите на какую сумму денег вы хотите внести в банк\n'
                        )
                        if (
                        summa.isdigit() == True and int(summa) > 1000
                        ):
                            balance[name].deposit_with_percent(int(summa), 0,0)
                            

                    elif deposit_command == '2':
                        summa = input(
                    '\nВведите на какую сумму денег вы хотите внести в банк\n'
                        )
                        if (
                        summa.isdigit() == True and int(summa) > 1000
                        ):
                            balance[name].deposit_with_percent(int(summa),0.06,6)
                            
                        
                    elif deposit_command == '3':
                        summa = input(
                        '\nВведите на какую сумму денег вы хотите внести в банк\n'
                        )
                        if (
                            summa.isdigit() == True and int(summa) > 1000
                            ):
                            balance[name].deposit_with_percent(int(summa),0.095,12)
                            

                    elif deposit_command == '4':

                        summa = input(
                        '\nВведите на какую сумму денег вы хотите внести в банк\n'
                        )
                        if (
                        summa.isdigit() == True and int(summa) > 1000
                        ):
                            balance[name].deposit_with_percent(int(summa),0.10,36)
                            

                    elif deposit_command == 'help':
                        help()
                        

                    else:
                        print(
                            '\nТакой команды не существует\n'
                            'Введите еще раз\n'
                            )
                        continue
                    break
            break

    elif command == '3':
        while True:
            name = input(
            'введите имя адресанта c какого счета вы хотите снять средства '
            )
            if name in balance:
                print('введите какую сумму денег вы хотите вывести в банкe ')

                while True:
                    summa = input()

                    if summa.isdigit() == True:
                        balance[name].withdraw(int(summa))
                        break
                    
                    else:
                        print(
                            '\n\Вы ввели не соответствующие данные\n'
                            'Введите еще раз\n')
                        continue
            else:
                print(
                '\n\Вы ввели не соответствующие данные\n'
                'Введите еще раз\n')
                continue
            break

    elif command == '4':
        while True:
            name = input('укажите баланс какого клиента хотите увидеть ')
            if name in names:
                print(names[name].balance)
            else:
                print(
            '\nТакого пользователя не существует\n'
            'Введите еще раз\n'
                    )
                continue
            break


    elif command == '5':
        print('что бы увидеть ваши личные данные введите свое имя')
        while True:
            name = input()
            if name in names:
                print(names[name])
            else:
                print(
                '\nТакого пользователя не существует\n'
                'Введите еще раз\n'
                    )
                continue
            break

    elif command == 'help':
        wellcome()
        help()
        
    else:
        print(
        '\nТакой команды не существует\n'
        'Введите еще раз\n'
            )
        continue
