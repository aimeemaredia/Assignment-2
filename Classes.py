from Base import*                                     #import Base file to use 

class inheritingClass(baseClass):                     #create inheritingClass which is a subclass of BaseClass

    def __init__(self):                               #initialize the class and call the init method of the superclass
        super(inheritingClass,self).__init__()
        self.x = 17                                   #override the x variable from baseClass to 17 

class inClassHam(baseClass):                          #create a inheriting class for Ham method 
   
    def __init__(self):                               #initialize the class and call the init method of the superclass
        super(inClassHam,self).__init__()
 
    def printHam(self):                               #override the printHam method from BaseClass to say "Ham 2"
        print("Ham 2")                                #instead of "Ham" 
        
class totalInheritance(inClassHam,inheritingClass):   #create totalInheritance class which inherits from inClassHam
                                                      #and inheritingClass
    def __init__(self):
        super(totalInheritance,self).__init__()       #initialize the class and the superclasses. 
        

        
        
# create an instance of the inheriting class and print the x value which was overridden 
i = inheritingClass()
print("This is the x value from inheritingclass:")
print(i.x)

# create an instance of inClassHam and print the new string stored in the variable 
j = inClassHam()
print("This a the printHam method from inClassHam")
j.printHam() 

# create an instance of totalInheritance and call the printHam method and print the int x 
k = totalInheritance()
print("These are the x value and printHam method from the totalInheritance class:")
print(k.x)
k.printHam()

# print the subclasses of the base class, inheritingClass and inClassHam 
print("This is the inheritance structure of the program:")
print(baseClass.__subclasses__())
print(inheritingClass.__subclasses__())
print(inClassHam.__subclasses__())
