medical_cause=input("did you have a medical cause, yes or no:")
attendance=int(input("enter your attendance:"))

if medical_cause=="yes":
   print("you are allowed to take the exam")
else:
   if attendance>=75:
      print("you are allowed to take the exam")
   else:
      print(" you are not allowed to take the exam")