name = input("Enter your name: ")

code = input("Enter your code: ")

dept = input("Enter your department: ")

print(name, code, dept)

with open("employee.txt","a") as file:
  file.write(name + "," + code + "," + dept + "\n")
  file.close()
l1 ,l2, l3 = list(), list(), list()
with open("employee.txt","r") as file:
  x , y, z = file.readline().split(",")
  l1.append(x)
  l2.append(y)
  l3.append(z)
  file.close()