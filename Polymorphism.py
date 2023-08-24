class Arithemetic:
    def sum(self,x,y):#this kind of fun is not implemented in python
        return x+y
    def sum(self,x,y,z):
        return x+y+z
    def sum(self,*nums):
        s=0
        for x in nums:
            s+=x
        return s 
a = Arithemetic()
print(a.sum(1,2,3))
# print(a.sum(1,2))
print(a.sum(1,2,3,4,5,6))