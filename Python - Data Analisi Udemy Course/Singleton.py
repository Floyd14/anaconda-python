# -*- coding: UTF-8 -*-


#    NOTE
# class MyClass(object):
#      i = 123                   Attributo di Classe
#      def __init__(self):       Costruttore di defoult
#          self.i = 345
# 
# a = MyClass()                  Istanzio una Classe = chiamo il costruttore --> creo un oggetto in cui i vale 345
# print a.i
# 345
# print MyClass.i                Richiamo una variabile definita in un modulo
# 123

class OnlyOne:
    
    #__Classe ausiliaria che ha solo un costruttore.
    class __OnlyOne:
        # Definisco una classe all'interno di un altra...
        def __init__(self, arg):
            self.val = arg
            
        # Implementazione del metodo __str__() -> <__main__.__OnlyOne instance at 0x00B73B98> + self.val
        def __str__(self):
            return repr(self) + self.val
            # repr() metodo di __builtin__ che ritorna la rappresentazione dell'oggetto in stringa
    
    # Di defoult OnlyOne.instance = None --> l'oggetto non esiste, non istanziato   
    instance = None
    
    # Costruttore della classe OnlyOne
    def __init__(self, arg):  
        # Se non esiste l'istanzia della classe..
        if not OnlyOne.instance:
            # ..crea un oggetto __OnlyOne(arg) e settalo come attributo istanza della classe OnlyOne
            # in questo caso mi�  servita la Classe ausiliaria...
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
         
        # Altrimenti prendi l'istanza gi� esistente e cambiagli l'argomento:    
        else:
            OnlyOne.instance.val = arg
            
    #Access comes through delegation, using the __getattr__( ) method to redirect calls 
    #to the single instance. You can see from the output that even though it appears that 
    #multiple objects have been created, the same __OnlyOne object is used for both. 
    #The instances of OnlyOne are distinct but they all proxy to the same __OnlyOne object.        
    def __getattr__(self, name):
        return getattr(self.instance, name)

x = OnlyOne('sausage') #sausage è l'arg
y = OnlyOne('eggs')
print(x)
print(y)
z = OnlyOne('frog')
print(z)
print(x)
print(y)
print(`x`)
print(`y`)
print(`z`)

