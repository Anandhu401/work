iplpoints=[
    {"team":"csk","mp":6,"won":5,"los":1,"pts":10},
    {"team":"srh","mp":6,"won":1,"los":5,"pts":2},
    {"team":"rcb","mp":6,"won":5,"los":1,"pts":10},
    {"team":"csk","mp":6,"won":5,"los":1,"pts":10},
    {"team":"rr","mp":5,"won":2,"los":3,"pts":4},
    {"team":"dc","mp":6,"won":4,"los":2,"pts":8},
    {"team":"pbks","mp":6,"won":2,"los":4,"pts":4}

]
# count number of participant
count=0
for i in iplpoints:
    count+=1
print("number of participant=",count)

# team name in uppercase
name_list=[]
for i in iplpoints:
    name_list.append(i["team"].upper())
print(name_list)

# sorted order basis on points
pointtable=sorted(iplpoints,key=lambda i:i["pts"],reverse=True)
print("sorted order=",pointtable)
#team detail who have highest points
print("highest point",pointtable[0],pointtable[1])
print("lowest point",pointtable[6])





    