class baseclass:
    def set_name(self,name):
        self.name=name

class subclass(baseclass):
    def dis_name(self):
        print("Name : "+self.name)
        

y=subclass()
y.set_name("Akhil")
y.dis_name()
