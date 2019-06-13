"""
Роздрукувати всі парні числа менші 100
 (написати два варіанти коду: один використовуючи цикл while, 
 а інший з використанням циклу for).
"""
even = 0
while even < 100:
    if even%2 == 0:
        print(even)
    even = even +1


for i in range(0,100):
    if i%2==0:
        print(i)

"""
2.	Роздрукувати всі непарні числа менші 100. 
(написати два варіанти коду: один використовуючи оператор continue, 
а інший без цього оператора).
"""

for i in range(0,100):
    if i%2 == 0:
        continue
    print(i)    

for i in range(0,100):
    if i%2 != 0:
        print(i)

"""
3.	Перевірити чи список містить непарні числа.
          (Підказка: використати оператор break)

"""

odd_list = [2,2,4,78,9]

is_odd_num = False
for i in odd_list:
    if i%2!=0:
        print("is odd numbers")
        is_odd_num = True
        break
if is_odd_num == False:
    print("all numbers is even")

"""
4.	Створити список, який містить елементи цілочисельного типу,
 потім за допомогою циклу перебору змінити тип даних елементів на числа з
  плаваючою крапкою. 
(Підказка: використати вбудовану функцію float ()).
"""

int_list = [1,4,6,7,3,7,2,5]

for i in range(len( int_list)):
    int_list[i] = float(int_list[i])                   
print(int_list)


"""
5.Вивести числа Фібоначі включно до введеного числа n, 
використовуючи цикли. 
(Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)
"""

fibo = int(input("input natural number"))
fibo_list = []
if fibo == 0:
    fibo_list.append(1)
elif fibo == 1:
    fibo_list.append(1)
    fibo_list.append(1)
elif fibo >1:
    fibo_list.append(1)
    fibo_list.append(1)    
    for i in range(2,fibo):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])

print(fibo_list)


"""
6.	Створити список, що складається з чотирьох елементів 
типу string. Потім, за допомогою циклу for,
 вивести елементи по черзі на екран.
"""

list_str = ["one","two","three","four"]

for i in list_str:
    print(i)

"""
Змінити попередню програму так, щоб в кінці кожної букви 
елементів при виводі додавався певний символ, наприклад “#”. 
          (Підказка: цикл for може бути вкладений в інший цикл, 
          а також  треба використати функцію print(“ ”, end=”%”)).

"""
for i in list_str:
    for j in i:
        print(j,end='#')         
    print("")

"""
8.	Юзер вводить число з клавіатури,
 написати скріпт, який визначає чи це число
  просте чи складне.
"""
is_simple_num = int(input("input natural number"))

simple_list = []

for i in range(1,is_simple_num+1):
    simple_list.append(i)

is_difficult_num = False

for i in simple_list:
    if i == is_simple_num or i == 1 :
        continue  
    elif is_simple_num % i ==0:
        print("number is difficul")
        is_difficult_num = True
        break

if is_difficult_num == False:
    print("number is simple")
   
"""
9.	Знайти максимальну цифру дійсного числа.
 Дійсне число генеруємо випадковим чином за допомогою методу random() 
 з модуля random
(для цього підключаємо модуль random наступним чином 
from random import random)

"""
from random import random

random_num = random()

max_number = 0
random_list = []
for i in (str(float(random_num))):
    if i == ".":
        continue
    elif max_number < int(i):
        max_number = int(i)

print("random mumber = " , random_num)
print("maximum figure of random number is " , max_number)


"""
10.	Визначити чи введене слово паліндром, 
тобто чи воно читається однаково зліва направо і навпаки.
"""

is_palindrom_str = input("input palindrom word :")

reverse_str = is_palindrom_str.upper()
reverse_str = list(reverse_str)

reverse_str.reverse()
reverse_str = "".join(reverse_str)

if is_palindrom_str.upper() == reverse_str:
    print("word is palindrom")
else:
    print("word is not palindrom")    
      

