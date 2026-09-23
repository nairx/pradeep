from os import listdir,chdir
chdir("python-lessons")
chdir("part4")
file = open("temp.txt","r")
data = file.read()
print(data)

