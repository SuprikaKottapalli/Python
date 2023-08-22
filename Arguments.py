#Default Arguments
def areaOfCircle(r,pi=3.14): #Default
    return r*r*pi
print(areaOfCircle(4,3.14))

#Required 
def getBalance(AccNo , WithdrawAmmount , Balance):#Required arguments
    return str(AccNo)+" Present Balance: "+ str(Balance-WithdrawAmmount)
print(getBalance(1234,3456,5678))

#Keywords
def getBalance1(AccNo , WithdrawAmmount , Balance):#Required arguments
    return str(AccNo)+" Present Balance: "+ str(Balance-WithdrawAmmount)
print(getBalance1(1234,Balance=300456,WithdrawAmmount=50678))  #Here we use keyword to say for the specific argments

# # Variables
# def product(a,b):
#     return a*b
# print(product(2,3))

# def product(*a):
#     if len(a) ==0:
#         p=0
#     else:
#         p=1
#         for i in a:
#             p*=1
#         return p
# print(product(1,3,5,6))


# # **kwargs
# def printDetails(**addresses):
#     for name , address , in addresses.items():
#         print(name,'->',address)
# printDetails(Ravi = 'Hyd', Meenu = 'Mumbai',Rani = 'India')