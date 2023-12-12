s = input("Enter the arithematic expression : ")
ch = 'A'

#w = a-b*c/d+e-f
print("\tThree Address Representation: ")
#for division operator
i = s.find("/")
while i!=-1:
    ch = chr(ord(ch)+1)
    three_add = s[i-1:i+2]
    s = s.replace(s[i-1],"",1)
    s = s.replace(s[i],"",1)
    s = s.replace("/",ch,1)
    print(ch, " = ", three_add,"\t\t",s )
    i = s.find("/")

#for multiplication operator
i = s.find("*")
while i!=-1:
    ch = chr(ord(ch)+1)
    three_add = s[i-1:i+2]
    s = s.replace(s[i-1],"",1)
    s = s.replace(s[i],"",1)
    s = s.replace("*",ch,1)
    print(ch, " = ", three_add,"\t\t",s )
    i = s.find("*")
#for addition operator
i = s.find("+")
while i!=-1:
    ch = chr(ord(ch)+1)
    three_add = s[i-1:i+2]
    s = s.replace(s[i-1],"",1)
    s = s.replace(s[i],"",1)
    s = s.replace("+",ch,1)
    print(ch, " = ", three_add,"\t\t",s )
    i = s.find("+")

#for addition operator
i = s.find("-")
while i!=-1:
    ch = chr(ord(ch)+1)
    three_add = s[i-1:i+2]
    s = s.replace(s[i-1],"",1)
    s = s.replace(s[i],"",1)
    s = s.replace("-",ch,1)
    print(ch, " = ", three_add,"\t\t",s )
    i = s.find("-")
