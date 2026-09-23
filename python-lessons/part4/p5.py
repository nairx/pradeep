from os import listdir,chdir
chdir("python-lessons")
chdir("part4")
print(listdir())
file = open("temp.txt","a")
while True:
    name = input("Enter your name")
    age=input("Enter your age")
    skill=input("Enter your skill")
    str = f"{name},{age},{skill}"
    file.write(str+"\n")
    flag = input("Do you want to continue?(y/n)")
    if flag != "y":
        break
file.close()