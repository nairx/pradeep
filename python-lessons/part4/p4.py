from os import listdir,chdir
chdir("python-lessons")
chdir("part4")
print(listdir())

# file = open("temp.txt","w")
# file.write("Hello World")
# file.close()


file = open("temp.txt","a")
file.write("Hello World\n")
file.close()