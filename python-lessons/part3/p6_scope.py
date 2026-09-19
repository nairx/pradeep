# x=5
# def f1():
#     x=10
#     print(x)
# f1()
# print(x)



def f1():
    global x
    x=10
    print(x)
f1()
print(x)