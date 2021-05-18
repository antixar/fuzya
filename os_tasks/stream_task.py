import sys
name = input("Enter your name. It need to start with capital letter:")
if name.istitle():
    print('Hi, ' +name +"!")
else:
    sys.stderr.write("Enter valid name!")
