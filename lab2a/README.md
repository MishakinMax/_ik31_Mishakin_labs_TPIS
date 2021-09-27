# 1

Було встановленно пайчарм

# 2 Виконання базових прикладів

Імпортуємо всі необхідні бібліотеки
````Shell script
import math
from math import *
from random import randint
````
Команди прінт та константи 
````Shell script
print("False еонстанта", False)
print("True константа" ,True)
print("Константа PI",pi)
````
Результати вбудованих функцій
````Shell script
print(abs(-12.5), f"є рівним {abs(12.5)}")
print("Заокруглення у вищу сторону",ceil(11.1))
````
Цикли та розгалуження
````Shell script
randNum = randint(0,100)
while True:
    _input = int(input("Вгадайте число число:"))
    if(_input > randNum):
        print("Число завелике")
    elif (_input < randNum):
        print("Число замале")
    elif (_input == randNum):
        break
print("Вітаю, ви вгадали число")
````

Конструкція try->except->finally.
````Shell script
A = 0
try:
    s = input("Введіть шось")
    s = s + 5
except Exception as e:
    print(e)
finally:
    print("Сталась помилка")
````

Контекст-менеджер with
````Shell script
with open("test.txt",'w') as f:
   f.write("Записав інформацію\n")
   f.write("Записав інформацію2\n")
   f.write("Записав інформацію3\n")
with open("test.txt",'r') as f:
   for l in f:
       print(l)
````

lambdas
````Shell script
Point = lambda x,y:(f'Точка:{x},{y}')
print(Point(1,5))
````
# 3 

Я створив у власному репозиторії такі файли
````Shell script
lab2a/
├── modules/
│   └── common.py
├── __init__.py
└── __main__.py
````

Я запустив виконання програми ціє. командою 
````Shell script
python .
````

Результат виконання був такий
````Shell script
2021-09-26 22:35:37.507398
win32
test
````

Ці стрічки взялись з __main__ фалу, пайтон автоматично найшов
цей файл і виконав його.

При виконанні 
````Shell script
python . -h
````

Виведе допомогу по всім параметрам
````Shell script
usage: . [-h] [-o OPT] [-l]

Приклад передачі аргументів у Python програму.

optional arguments:
  -h, --help            show this help message and exit
  -o OPT, --optional OPT
                        Цей параметр є вибірковим.
  -l, --logs            Якщо виконати команду з цим параметром будуть виводитись логи.
````

Якщо передати параметри за допомогою
````Shell script
python . -o "Цей текст також має вивестись"
````

виведе
````Shell script
We are in the __main__
2021-09-26 22:39:14.612046
win32
З консолі було передано аргумент
 ========== >> Цей текст також має вивестись << ==========
test
````

Я також ознайомився з логуванням консолі 
````Shell script
2021-09-26 22:41:28,624 root INFO: Тут буде просто інформативне повідомлення
2021-09-26 22:41:28,624 root WARNING: Це Warning повідомлення
2021-09-26 22:41:28,625 root ERROR: Це повідомлення про помилку
test
````

Я створив власну функцію яка виводить всі парні 
числа до 100 якщо у функцію передати значення True і 
непарні якщо значення False. Та викликав у мейн її 
````Shell script
def Pair(bol):
    for i in range(0,100):
        if(bol and i%2 == 0):
            print(i)
        elif(not bol and i%2 != 0):
            print(i)
````

Я зробив функцію яка може виконуватись з помилкою
та зробив логування в ній
````Shell script

````

запустив її у мейн передваши 0 як аргумент, після виконання 
у логах з'явилась помилка
````Shell script
def TwoDivideOn(num):
    try:
        a = 2/num
        logger.error("Програма виконалась")
        return a
    except Exception as ERROR:
        logger.error("Помилка")
````

# 4

Я зробив табличку у своїй папці в репозиторї з лінками 
та номерами лаб. Також зробив пулл реквест
