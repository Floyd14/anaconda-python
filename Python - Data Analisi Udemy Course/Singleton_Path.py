# -*- coding: UTF-8 -*-

class Path:
    instance = None
    def __init__(self, arg):
        if not Path.instance:
            Path.instance = Path.__Path(arg)
        else:
            Path.instance.val = arg
        
    class __Path:
        def __init__(self, arg):
            self.val = arg
        
print Path