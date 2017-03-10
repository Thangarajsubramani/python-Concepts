# Built-in namespace
import __builtin__

# Extended subclass
class mystr(list):
    def first_last(self):
        if self:
            return [self[0] , self[-1]]
        else:
            return ''

# Substitute the original str with the subclass on the built-in namespace    
__builtin__.str1 = mystr


print str1([1,2,3,4]).first_last()
#print str(0).first_last()
#print str('').first_last()
#print '0'.first_last()


a=[1,2]
a.insert(0,5)
print a
