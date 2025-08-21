s1={1,3,2}
s2={'a','c','b'}
s3=list(zip(s1,s2))
print(s3,'\n')

list1=[1,2,3,4]
list2=[100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks={'spinneys','Wmart','grandex'}
prices={50,30,10}
new_dict={stocks:prices for stocks,prices in zip(stocks,prices)}
print('\n {}'.format(new_dict))