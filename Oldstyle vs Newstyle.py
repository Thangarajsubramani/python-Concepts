x=10

print type(x)


class test(object):

    def __init__(self):
        pass

obj=test()

print type(obj)

def reverse(num):
    rev=0
    while num != 0:
        rev *= 10
        rev += num % 10
        num /= 10
    return rev

print reverse(1234)

s=([9],[0])
cities = set(s)

s[0][0]=1

print cities
