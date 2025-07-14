print("marks obtained in 5 subjects")
markone=int(input())
markontwo=int(input())
markthree=int(input())
markfour=int(input())
markfive=int(input())
totalmarks=markone+markontwo+markthree+markfour+markfive
print("the total marks you have obtained =",totalmarks)
avg=totalmarks/5
print("your average =",avg)
if avg >= 90:
  print("grade A")
elif avg>=80:
  print("grade B")
elif avg>=70:
  print("grade C") 
elif avg>= 60:
  print("grade D")  
elif avg >= 50:
  print ("grade E")  
else:
  print("grade F")