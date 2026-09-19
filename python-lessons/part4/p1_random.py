#user defined module
# from calc_module import *
# result = add(2,3)
# print(result)


# from random import *
# result = randint(1,9)
# print(result)


# from random import *
# print("=== Math Question Paper ===")
# for i in range(5):
#     a = randint(11,99)
#     b = randint(1,9)
#     print(f"{a}+{b}=")

#inbuilt module
# from random import *
# print("=== Math Question Paper ===")
# operator = ["+","-","x","/"]
# for i in range(5):
#     a = randint(11,99)
#     b = randint(1,9)
#     op = choice(operator)
#     print(f"{a}{op}{b}=")


# from random import *  #or from random import randint
# num = randint(1,9)
# # print(num)
# while True:
#     usernum = int(input("Guess a number: "))
#     if usernum == num:
#         print("You have entered the correct number")
#         break



from random import *
for a in range(5):
    print("=== Math Question Paper ===")
    operator = ["+","-","x","/"]
    for i in range(5):
        a = randint(11,99)
        b = randint(1,9)
        op = choice(operator)
        print(f"{a}{op}{b}=")