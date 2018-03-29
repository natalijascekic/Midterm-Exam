"""
===================   TASK 6   ====================
* Name: Attendance Checker
*
* Write a student attendance checker script. The
* script should take, as user input, minimum
* required number of attended classes for student
* in order to take an exam. File `attendance.csv`
* contains info about students and number of
* classes they attended. Print student names, that
* do not have right to take an exam.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

sve_linije = open("attendance", "r").readlines()

suma = 0
for linija in sve_linije:
    linija1 = linija.strip()
    ime_i_broj = linija1.split(",")

    ime = str (ime_i_broj[0])
    broj = int(ime_i_broj[1])

    suma += broj

rezultat = open("rezultat.txt", "a").write("Suma brojeva je:" +str(suma) + "\n")