sub1 = int(input("Enter1 subject marks\n"))
sub2 = int(input("Enter2 subject marks\n"))
sub3 = int(input("Enter3 subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are Fail")
if(sub1+sub2+sub3)/3<40:
    print("You are fail due to total percentage less than 40")
else:
    print("congratulation ! You  passed the Exam")
