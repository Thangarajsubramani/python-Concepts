def decoratorFunctionWithArguments(arg1):
    def wrap(f):

        def wrapped_f(*args):
            print arg1
			return f(*args)
        return wrapped_f
    return wrap

@decoratorFunctionWithArguments("addtitionstage")
def add(a1, a2):
    return a1 +a2

@decoratorFunctionWithArguments("substage")
def sub(a1, a2):
    return a1 -a2


print add(40,50)
print sub(66,90)
print add(40,50)


'''def decoratorFunctionWithArguments(f):

        def wrapped_f(*args):
            print "addtion"
            return f(*args)
        return wrapped_f


@decoratorFunctionWithArguments
def add(a1, a2):
    return a1 +a2
@decoratorFunctionWithArguments
def sub(a1, a2):
    return a1 -a2

print add(40,50)
print sub(66,90)'''

