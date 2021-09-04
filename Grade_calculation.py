num=float(input("enter the percentage="))
if num<=100 and num>=80:
 print("U got a 'A' grade")
elif num<80 and num>=60:
 print("U got the 'B' grade")
elif num<60 and num>=40:
    print(" U got the 'C' grade")
elif num<40 and num>=0:
    print("U are 'Fail'")
else:
 print(" Please enter the percentage in between the 1 to 100")
