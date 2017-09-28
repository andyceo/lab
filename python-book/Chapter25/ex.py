class C2(object): pass
class C3(object): pass

class C1(C2, C3):
    def setname(self, who):
        self.name = who

I1 = C1()
I2 = C1()

I1.setname('bob')
I2.setname('mel')

print(I1.name)
print(I2.name)

C1.setname(C1, 'class!') # but C1.setname('class!') not working!
print(C1.name)
