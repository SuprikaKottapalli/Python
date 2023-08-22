#Find the phn num using empo
# there is a db Stored in a dictionay as given below
# emp_db = {1234:[Anish,'9876543210','Anish@gmail.com',9000]
# 1234:[Abc,'9876543211','Abc@gmail.com',7500]
# 1234:[Def,'9876543212','Def@gmail.com',8000]
# 1234:[Ghi,'9876543213','Ghi@gmail.com',9999]}


emp_id = int(input("Enter your Employee ID: "))
DataBase = {1234:['Anish','9876543210','Anish@gmail.com',9000],
            1235:['Abc','9876543211','Abc@gmail.com',7500],
            1236:['Def','9876543212','Def@gmail.com',8000],
            1237:['Ghi','9876543213','Ghi@gmail.com',9999]}
if emp_id in DataBase:  
    print(DataBase[emp_id][1])
else:
    print("Invaild Mobile num! Check again and try")
