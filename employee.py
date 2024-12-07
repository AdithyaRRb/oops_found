class employee_detail:
    year = 2020
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def add_age(self):
        self.age=self.age+1

    def relocate(self,place):
        self.place= place

    @classmethod
    def year_update(cls):
        cls.year=cls.year+1

    def display(self):
        print("year : "+str(employee_detail.year))
        print("name : "+self.name)
        print("age : "+str(self.age))
        print("place : "+self.place)
        
x=employee_detail("Adhi",20,"tvm")
y=employee_detail("paru",25,"ekm")

x.display()
y.display()
print("_______________________")
#employee_detail.year=employee_detail.year+1
x.add_age()
y.add_age()
x.relocate("calicut")
y.relocate("tvm")
employee_detail.year_update()
x.display()
y.display()


        