#calc is a user defined module

# from calc import *
# result = add(4,6)
# print(result)
# result1 = multiply(2,3)
# print(result1)


# from calc import add
# result = add(4,6)
# print(result)


# import calc
# result = calc.add(4,6)
# print(result)
# result1 = calc.multiply(2,3)
# print(result1)


# import calc as c
# result = c.add(4,6)
# print(result)
# result1 = c.multiply(2,3)
# print(result1)


#user defined module
#module name - calc
#mothods - add,subtract,multiply


#inbuit module
# module name - random
# mothods - randint(1,9),choice(["John","Amy","Mike"])

#inbuit module
# module name - os  
# mothods - listdir(),chdir()


# from random import *
# num = randint(1,9)
# print(num)

# from random import randint
# num = randint(1,9)
# print(num)


# import random
# num = random.randint(1,9)
# print(num)


# import random as r
# num = r.randint(1,9)
# print(num)



# import os
# result = os.listdir()
# print(result)


# from os import listdir
# result = listdir()
# print(result)


# import random as r
# num = r.randint(1,9)
# print(num)


#External Module - use pip install matplotlib to install the package
import matplotlib.pyplot as plt 
year = ["2010","2011","2012", "2013", "2014"]
sales = [1000,1400,1100,1800,2000]
plt.plot(year,sales)
plt.show()
