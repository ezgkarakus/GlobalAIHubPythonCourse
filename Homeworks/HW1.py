list1=[i for i in range(10) if i%2==0]
list2=[i for i in range(10) if i%2==1]
list1.extend(list2)
list1=[a*2 for a in list1]
for i in range(len(list1)):
    print(type(list1[i]))
