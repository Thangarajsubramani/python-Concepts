class RevIter:

    def __init__(self,iter_obj):
        self.i=0
        self._iter=iter_obj
        self.n=len(iter_obj) -1

    def __iter__(self):

        return self
    def next(self):

        if self.i <= self.n:
            i=self.n
            self.n -=1
            return self._iter[i]
        else:
            raise StopIteration()

obj=RevIter([1,2,3])

print list(obj)

#print "hi"
#print list(obj)

class yrange:
    def __init__(self, iter1):
        self.i = 0
        self.n = len(iter1)-1
        self._iter=iter1

    def __iter__(self):
        return self

    def next(self):
        if self.i <= self.n:
            i = self.n
            self.n -= 1
            return self._iter[i]
        else:
            raise StopIteration()

x=yrange([2, 3])

print x.next()

print x.next()
