import datetime
x = datetime.datetime.now()
name = input("Enter your name: ")
age = input("enter your age: ")
print("Hi " + name + " How are you doing?")
y = 100 - int(age)
print(name + " you will turn 100 years on " + str(int(x.year)+y))
print(name + " working on SOR-1103")
print(x)