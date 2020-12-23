#assumptions For each function seperate memorise_class object is made
#can also be done using decorator but class provided more flexibility here
#The values are only deleated when they expire and are called,
#however also possible to implement function to check and delete expire values
from datetime import datetime
from datetime import timedelta
class memorise_class:
    def __init__(self):
            self.table = {}
    def memoize( self,func=None , *args,timeout=5000):

        #values are stored as follows , value =cache[(day,month,year)]
        #value retruns a dict with value and time
        #then if value has timed out it will be deleted and function will be called to get new value

        if args in self.table:
             t_timeout=self.table[args]["timeout"]
             time=self.table[args]["time"]
             if(datetime.now()-time > t_timeout):
                 del self.table[args]# if value has expired delete value and make new value(in the end)
                 if (func is None):
                     return None
             else:
                 return(self.table[args]["value"])

        if(func is None):
            return None

        result = func(*args)
        self.table[args] = {"value":result,
                       "time":datetime.now(),
                       "timeout":timedelta(days=0,seconds=0,microseconds=0,milliseconds=timeout)
                       }
        return result