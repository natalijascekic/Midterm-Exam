"""
===================   TASK 1   ====================
* Name: Area Of Circle
*
* Write a function `area_of_circle` that will
* return area enclosed by a circle of radius `r`.
* Consider that only float value for radius will
* be passed. Negative values should be considered
* as typo and function should ignore sign of a
* number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here
def area_of_circle(poluprecnik):
    area_of_circle = abs(poluprecnik) * abs(poluprecnik) * 3.14
    if (not isinstance(poluprecnik, int)) and (not isinstance(poluprecnik, float)):
        return False



    return area_of_circle




def main():

    povrsina = area_of_circle(2.3)
    print("povrsina je:",povrsina)


main()
