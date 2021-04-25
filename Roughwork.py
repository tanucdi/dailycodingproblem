class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(self.name, 'is eating')
    
    def walk(self,legs):
        self.legs = legs
        print('walking with',self.legs,'number of legs')
    
    def getname(self):
        print(self.name)
    
    def setname(self,newname):
        self.name = newname

dog = Animal('dog')
dog.eat()
dog.setname('gogi')
dog.getname()
dog.walk(4)