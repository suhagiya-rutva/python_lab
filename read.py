f=open("1.txt","r")
data=f.read()
print("File content:",data)
f.close()

f=open("1.txt","r")
data=f.read(10)
print("First Part:",data)
f.close()

f=open("1.txt","r")
line1=f.readline()
line2=f.readline()
print("Line 1:,line1")
print("Line 2:,line2")
f.close()

f=open("1.txt","r")
lines=f.readlines()
print("List of lines:",lines)
print("Number of lines:",len(lines))
f.close()

#reads specific line in file
f=open("1.txt","r")
lines=f.readlines()
print(lines[1].strip())
f.close()