"""
===================   TASK 3   ====================
* Name: Negative and Non-Negative Elements
*
* Write a script that will populate a list with as
* many elements as user defines. For taken number
* of elements the script should take the input from
* user for each element. You should expect that
* user will always provide integer numbers. At the
* end, the script should print how many negative
* and non-negative numbers there were present in
* the list.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""


def pozitivan(x):
    if x >0 :
        return True
    else:
        return False


duzina_liste = int(input("koliko ce lista imati brojeva:"))

lista = []
pozitivni = negativni = 0

for i in range(duzina_liste):
    novi_broj = int(input("unesite broj" + str(i + 1) + ":"))
    lista.append(novi_broj)

    if pozitivan(novi_broj):
        pozitivni += 1
    else:
        negativni += 1

print("Vasa lista:", str(lista))
print("Lista ima pozitivnih brojeva:", pozitivni)
print("Lista ima negativnih brojeva:", negativni)

