line=input()
line2= input()
num=line2[:1]
char=line2[2:]
if(len(line)<=int(num)):
    print("The number you gave is too large")
else:
    line=line[:int(num)]+char+line[int(num):]
    print(f"{line}")
    #성공
    