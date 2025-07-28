string=str(input("please enter your word-"))
char=str(input("please enter the charecter-"))
i=0
count=0
while(i< len(string)):
    if (string [i]==char):
        count=count+1
    i=i+1
print  ("the total times",char,"has occured=",count)      