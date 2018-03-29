"""
===================   TASK 2   ====================
* Name: Product Of Digits
*
* Write a script that will take an input from user
* as integer number and display product of digits
* for a given number. Consider that user will always
* provide integer number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

def proizvod_cifara(broj):
    if not isinstance(broj,int):
        return -1

    proizvod = 1

    abs_broj = abs(broj)
    while abs_broj > 0:
        cifra = abs_broj % 10
        abs_broj = abs_broj // 10
        proizvod += cifra
    return proizvod

def main():
     neki_broj = -23
     proizvod = proizvod_cifara(neki_broj)
     print("proizvod cifara je", proizvod)

main()


