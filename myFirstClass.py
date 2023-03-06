class workerList:
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self,rate):
        self.pay *= (1 + rate)
    
john = workerList("John Smith", 5000)
ana = workerList("ana sue", 4500)
ana.giveRaise(0.05)
print(john.lastName())
print(ana.pay)

