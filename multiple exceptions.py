try:
    num1,num2=eval(input("enter 2 numbers , seperated by a comma"))
    result=num1/num2
except ZeroDivisionError:
    print("division by zero is error!!!") 
except SyntaxError:
    print("you have not separated the 2 numbers by a comma.like this-1,2") 
except:
    print("wrong input") 
else:
    print("no exceptions")             