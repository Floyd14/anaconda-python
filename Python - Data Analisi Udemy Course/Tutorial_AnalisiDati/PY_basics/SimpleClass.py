# -*- coding: UTF-8 -*-

# PythonForProgrammers/SimpleClass.py
class Simple:
    def __init__(self, str):
        # IMP __init__() NON RITORNA NULLA, SEMPRE !!
        
        # richiamo metodi.. (__builtins__)
        print "print in __init__ dell'argomento: ",str 
        print 'self in __init__: ',self           # self è una istanza della classe Simple in una locazione di memoria
        
        # setto attributi...
        self.s = str
    
#                     Two methods   
#     Both methods have self as their first argument. 
#     C++ and Java both have a hidden first argument in their class methods, 
#     which points to the object that the method was called for and can be 
#     accessed using the keyword this. Python methods also use a reference 
#     to the current object, but when you are defining a method you must 
#     explicitly specify the reference as the first argument. Traditionally,
#     the reference is called self but you could use any identifier you want
#     (if you do not use self you will probably confuse a lot of people, however).
     
    def show(self):                     # IMP: self lo DEVO mettere perchè usato nel metodo 
        return self.s      
        
    def showMsg(self, msg):
        print msg + ':',self.show()     # Calling another method
        
        # Ritorna NONE !!

#***********************************************************
if __name__ == "__main__":
    # Create an object:
    x = Simple("constructor argument")
    print '\nChiamo metodo Show():\t', x.show()
    print 'Accedo ad un metodo:\t', x.showMsg("A message")
    