def search(list1,ele):
    list2=[]
    flag=False
    for i in range(len(list1)):
        if(ele==list1[i]):
            flag=True
            list2.append(i)

    if(flag == True):
        for i in list2:
            print("Element",ele," is found at index: ",i)

    else:
        print("Searched Element is not found")

list1=[13,15,3,6,45,3,76,81,3]
ele= int(input("Enter the number: "))
print(search(list1,ele))





