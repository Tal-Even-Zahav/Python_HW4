''' Exercise #1 '''

#########################################
# Question 1 - do not delete this comment
#########################################
def hi_name(name):
    # Write the rest of the code for question 1 below here.
    a = name.title()
    print("Hi", a + "!!!")

#########################################
# Question 2 - do not delete this comment
#########################################

def deltoid(AB, AD, ABD, ABC):
    # Write the rest of the code for question 2 below here.
    print(">>>deltoid", (AB, AD, ABD, ABC))
    print("Perimeter is: ", (AB * 2 + AD * 2))
    AC = ABC - 2 * AB
    DB = ABD - AD - AB
    print("AC: ", (AC))
    print("DB: ", (DB))
    print("S: ", (AC * DB / 2))

#########################################
# Question 3 - do not delete this comment
#########################################
def divide_by_seven(num): 
    # Write the rest of the code for question 3 below here.
    num = int(num)
    if num % 7 == 0:
        print("The number", num, "is divisible by 7")
        return (num / 7)
    else:
        print("The number", num, "is not divisible by 7")
        return None


#########################################
# Question 4 - do not delete this comment
#########################################
def str_mixer(text, copies1, copies2): 
    # Write the rest of the code for question 4 below here.
    sub1 = text[0::2]
    sub2 = text[1::2]
    new_str = sub1 * copies1 + sub2 * copies2
    print(new_str)

#########################################
# Question 5 - do not delete this comment
#########################################
def rearrange_str(name, ind1, ind2): 
    # Write the rest of the code for question 5 below here.
    if name == "" or ind1 >= len(name) or ind2 >= len(name) or ind2 <= ind1 or ind1 < 0 or ind2 < 0:
        print("Error: illegal input!")
        return -1
    else:
        sub1 = name[ind1-1::-1]
        sub2 = name[ind2-1:ind1-1:-1]
        sub3 = name[:ind2-1:-1]
        print(sub1 + " " + sub2 + " " + sub3)
        return 0


#########################################
# Question 6 - do not delete this comment
#########################################
def divisor_checker(digits, divisor): 
    # Write the rest of the code for question 6 below here.
    x = 0
    if len(digits) == 6:
        for i in range(6):
            if int(digits[i]) % divisor == 0:
                x = x + 1
            if x == 2:
                print(i)
                break
        else:
            print("-1")
    else:
        print("-1")

#########################################

if __name__=='__main__':

    # Ex1 tests
    hi_name('Tom')
    hi_name('oxana')
    hi_name('Alice')
    hi_name('aliCE')
    hi_name('boB')

    # Ex2 tests
    deltoid(10.0, 5.0, 28.0, 26.0)
    deltoid(1.0, 1.0, 3.414213562, 3.414213562)
    deltoid(4.5, 2.0, 14.0, 13.0)
    deltoid(7.0, 3.0, 22.5, 30.0)

    # Ex3 tests
    divide_by_seven('7')
    divide_by_seven('-17')

    # Ex4 tests
    str_mixer('tom', 3, 4)
    str_mixer('oxana', 2, 3)

    # Ex5 tests
    rearrange_str('ibaccaMleTvivA', 7, 10)
    rearrange_str('ibaccaMleTvivA', 6, 30)
    rearrange_str('ibaccaMleTvivA', 8, 7)
    rearrange_str('', 7, 10)

    # Ex6 tests
    divisor_checker('428315', 4)
    divisor_checker('428315', 5)
    
