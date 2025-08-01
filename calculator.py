def add(Q,P):
    return Q+P
def subtract(Q,P):
    return Q-P
def multiply(Q,P):
    return Q*P
def divide(Q,P):
    return Q/P
print("please select the operation-")
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")
choise=input("please enter your selection(a/b/c/d)-")
num_1=int(input("please enter the first number:"))
num_2=int(input("please enter the second number:"))
if choise=='a':
   print(num_1,"+",num_2,"=",add(num_2+num_1))
if choise=='b':
   print(num_1,"-",num_2,"=",subtract(num_2-num_1))   
if choise=='c':
   print(num_1,"*",num_2,"=",multiply(num_2*num_1))   
if choise=='d':
   print(num_1,"/",num_2,"=",divide(num_2/num_1))   