student_value={'id1':{'name':['myra'],'class':['v'],'subject':['maths']},
              'id2':{'name':['mehr'],'class':['v'],'subject':['science']} ,
              'id3':{'name':['myra'],'class':['v'],'subject':['maths']},
              'id4':{'name':['mehr'],'class':['v'],'subject':['science']}}
result={}              
for key,value in student_value.items():
    if value not in result.values():
        result[key]=value
print(result)