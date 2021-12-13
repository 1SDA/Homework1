
class Students(object):
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def getmarks(self):
        return self.marks

    def getroll(self):
        return self.roll

    def __str__(self):
        return "Name: " + self.name + " Roll: " + str(self.getroll()) + " Marks: " + str(self.getmarks())
