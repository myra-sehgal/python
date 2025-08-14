def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("number of words withe same starting and ending letter\n",lst)
    return ctr
count = match_words(["abc","ada","dad","cfc","121","1231"]) 
print("words haveing the first and last letter same=",count)
