valid = False
try:
 while not valid:
    n=int(input("enter a number-"))
    while n%2==0:
        print("bye")
except ValueError:
   print("value error")
        