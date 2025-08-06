char=input("please enter a charecter-")
if len(char)==1:
    ascii_value=ord(char)
    print(f"the ascii value of {char}is{ascii_value}")
else:
    print("please enter a single letter")