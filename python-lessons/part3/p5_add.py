# def add(a,b):
#     print(a+b)
# add(4,5)


# def add(a,b=0):
#     print(a+b)
# add(4)


# def add(a=0,b=0):
#     print(a+b)
# add(6,5)


# def add(a,b):  #positional argument
#     print(a+b)
# add(4,5)

# def add(a,b):  #keyword argument
#     print(a+b)
# add(b=4,a=5)



# def add(*args):
#     print(sum(args))
# add(6,7,8,9,6,5)


# def add(**kwargs):
#     print(sum(kwargs.values()))
# add(a=5,b=6,c=3)


def add(*args,**kwargs):
    print(sum(args)+sum(kwargs.values()))
add(1,4,7,a=5,b=6,c=3)


