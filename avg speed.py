a=int(input("enter a value"))
b=int(input("enter a value2"))
c=int(input("enter a value3"))
avg_speed=(a+b+c)/3
print("average speed = ",avg_speed)
if avg_speed > a and avg_speed >b and avg_speed > c:
    print ("average speed is greater than all individual speeds")
elif avg_speed > a and avg_speed >b :
    print ("avg speed is greater than a and b")
elif avg_speed > b and avg_speed >c :
     print ("avg speed is greater than b and c")
elif avg_speed  >a and avg_speed >c :
     print ("avg speed is greater than a and c")
elif avg_speed  >a:
     print ("avg speed is greater than a")
elif avg_speed  >b :
     print ("avg speed is greater than b")
elif  avg_speed >c :
      print ("avg speed is greater than c")
else:
     print("all individual speeds are greater than the avg speed")