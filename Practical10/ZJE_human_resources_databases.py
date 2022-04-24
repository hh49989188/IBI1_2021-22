class staff() :
    def __init__(self, first_name, last_name, location, role):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.role = role
# Giving the four variables respected attribute
    def f(self):
        z = self.first_name+' '+self.last_name+" "+self.location+" "+self.role
        return z
        print(z)
# integret the information to one single line

# take an example
Robert_Young = staff('Robert','Young','Edinburge','Faculty')
print(staff.f(Robert_Young))