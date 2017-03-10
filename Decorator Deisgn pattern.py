def my_decorator(*args):

    def wrapped(func):

         def wrapped1(*targs):

            if len(targs) == 1:

                return func(targs[0], args[0])
            elif len(targs) == 2:
                value=[]
                value.extend(args)
                value.extend(targs)

                return func(*value)
         return wrapped1

    return wrapped


class my_dec(object):

    def __init__(self,*args):

        self.args = args

    def __call__(self, func):
        self.f = func

        def wrapped(*targs):

            if len(targs) == 1:
                return self.f(targs[0], self.args[0])
            elif len(targs) == 2:

                value = []
                value.extend(self.args)
                value.extend(targs)
                return self.f(*value)
        return wrapped


@my_dec(2)
def pow(x, y):
    return x ** y

print pow(4) #=> 16

@my_dec("/home", "user")
def path(*args):
    return "/".join(args)
print path("videos", "cats.png") #=> "/home/user/videos/cats.png"

a=b=[10,20]

print a, b
