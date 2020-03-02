def leftRotatedString(name):
    size = len(name)

    temp = name + name

    for i in range(size):
        for j in range(size):
            print(temp[i + j], end="")
        print()


string="NETSET"
# leftRotatedString(string)

def checkrotation(str1,str2):
    if(len(str1)!=len(str2)):
        return False
    size=len(str1)
    s=str1+str1
    if(str2 in s):
        print(str1,"is matching with",str2)
    else:
        print(str1, "is not matching with", str2)

checkrotation("ANU","NUR")


