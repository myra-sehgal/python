print("please enter a number(numerator):")
nume=int(input())
print("please enter a number(denomenator):")
denom=int(input())
if nume%denom==0:
    print('\n'+str(nume)+"is divisible by"+str(denom))
else:
    
    print('\n'+str(nume)+"is not divisible by"+str(denom))