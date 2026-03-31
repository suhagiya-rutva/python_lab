f=open("1.txt","w")
f.write("hello student\n")
f.write("Welcome to Python file handing.\n")
f.write("Learning is fun!\n")
f.close()

f=open("1.txt","w")
f.write("New content only.\n")
f.close()

f=open("1.txt","w")
lines=[
    "Python Programming\n",
    "File Handling\n",
    "Error Handling",
    "Exception Handling\n"
]
f.writelines(lines)
f.close()