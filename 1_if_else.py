#if_else.py
number=int(input("정수 입력: ")) 
if number%2==1:
    print("Weird")
elif 2<=number<=5:
     print("Not Weird")
elif 6<=number<=20:
     print("Weird")
else:
     print("Not Weird")