#creating a new datatype
class Student:
    #initialize is used to map out what the class must have
    #define components on the parameters 
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    
 #class only defines a data type
    #the things inside the __init__ saves the value that is passed on the function

    def honor(self):
        if self.gpa >= 1.5:
            return True
        else: 
            return False
   
