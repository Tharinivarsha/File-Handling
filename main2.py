#Activity 2
file=open("myfile.txt","r")
print(file.read())

filewrite=open("myfile.txt","w")
filewrite.write("I am creating a another file.")
filewrite.write("I am adding a new line.")

file.close()