class mysampleclass:
    def intro(self, n):
        #print("hello")
        self.name=n

    def exit(self):
        #y= self.name
        print("Hi "+self.name)


x=mysampleclass()
name="Adhi"
x.intro(name)
x.exit()