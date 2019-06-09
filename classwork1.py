"""
1.	Написати скрипт, 
який з двох введених чисел визначить,
 яке з них більше, а яке менше.

"""

number1 = input("input first number")
number2 = input("input second number")

if number1 > number2:
    print("first number biggest")
elif number2 > number1:
    print("second number biggest")
else:
    print("first number equals second")


"""
2.	Написати скрипт, який перевірить 
чи введене число парне чи непарне і вивести відповідне повідомлення.

"""

num = int(input("input number"))

if num%2==0:
    print("number is even")
else:
    print("number is odd")


"""
3.	Написати скрипт, який обчислить факторіал введеного числа
"""

factorial = int(input("input natural number"))

if factorial in range(0,1):
    factorial = 1
else:
    product =1
    for i in range(1,factorial+1):
        product = product *i
    factorial = product   

print(factorial)    

