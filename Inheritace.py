class Collage:
    def __init__(self):
        self.clg_code = 1213
        self.clg_name = "Aits-Hyd"
#Sub class
class Student(Collage):
    def __init__(self,rno,sname):
        super().__init__()
        self.sname = sname
        self.rollnum = rno
    def displayInfo(self):
        print("Collage code: ",self.code)
        print("Collage Name:",self.clg_name)
        print("Roll num: ",self.rollnum)
        print("Student Name: ",self.sname)
s = Student(2134,"suprika")
s.displayInfo()

