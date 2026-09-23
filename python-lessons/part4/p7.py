from os import *

chdir("python-lessons")
chdir("part4")

print(listdir())

rename("temp.txt","students.txt")

print(listdir())

remove("students.txt")