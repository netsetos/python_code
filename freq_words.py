def freq_words():
    str=input("Enter a string: ")
    li=str.split()
    d={}
    print('--->',li)
    for i in li:
        d[i]=d.get(i,0)+1
    print(d)

freq_words()