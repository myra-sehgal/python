amount = int(input("please enter your amount for withdrall"))
note_1 = amount // 100
note_2 = (amount % 100)//50
note_3 = ((amount%100)%50)//10

print("notes of 100 ruppees=" , note_1)

print("notes of 50 ruppees=" , note_2)

print("notes of 10 ruppees=" , note_3)