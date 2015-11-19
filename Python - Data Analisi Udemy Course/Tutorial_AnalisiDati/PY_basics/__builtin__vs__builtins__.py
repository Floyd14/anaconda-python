import __builtin__

print "\n Run in current.py"
print "__name__ is:\t\t\t", __name__
print "__builtin__ is __builtins__:\t", __builtin__ is __builtins__
print "type(__builtin__):\t\t", type(__builtin__)
print "type(__builtins__):\t\t", type(__builtins__)

import __built_ExempleA

print '''
Il modulo __builtin__ viene caricato in automatico dall'interprete:
si hanno a disposizione metodi e variabili ovunque...

Using __builtin__ is better than __builtins__. 

The type, and thus behavior, of __builtins__ changes based 
on the context of where it's being executed, while the type
and behavior of __builtin__ is constant.

Infatti quando importo il modulo A.py, __builtins__ diventa un dict..
 
 '''