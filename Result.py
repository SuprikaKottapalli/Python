mark1 = int(input("Enter marks od sub1:"))
mark2 = int(input("Enter marks od sub2:"))
mark3 = int(input("Enter marks od sub3:"))
mark4 = int(input("Enter marks od sub4:"))
mark5 = int(input("Enter marks od sub5:"))

if(mark1>=0 and mark1<=100 and mark2>=0 and mark2<=100 and mark3>=0 
   and mark3<=100 and mark4>=0 and mark4<=100 and mark5>=0 and mark5<=100 ):

    if(mark1>40 and mark2>40 and mark3>40 and mark4>40 and mark5>40 ):
        print("Pass")
    else:
        print("Not Pass")


else:
    print("Invalid Marks")