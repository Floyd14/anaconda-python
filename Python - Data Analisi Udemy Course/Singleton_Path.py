# -*- coding: UTF-8 -*-
class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)
 
@Singleton
class Path:
    def __init__(self): 
        # __init__ always return NONE !        
        self.path = './Tutorial_AnalisiDati/Temp/'
        self.getPath()
    
    def getPath(self): # Non funziona!
        return self.path
    
    def __str__(self):
        return self.path
   
# EXEMPLE
print Path.Instance()

# The print statement converts each of its arguments to a string 
#(using the __str__ magic method) and writes the result to 
#standard output separated by spaces.

    