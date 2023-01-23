def Distance(orig):
        def wrapper(v1,v2,t):
            s = v1*t + ((v2-v1)/t * t**2)/2
            orig
            print(s)

        return wrapper

@Distance
def Boost (v1, v2, t):
    a = (v2-v1)/t
    return a

try:
    v1 = float(input())
    v2 = float(input())
    t1 = float(input())
    t2 = float(input())
    t = t2 - t1
    s = v1*t + ((v2-v1)/t * t**2)/2
except ZeroDivisionError:
    print('t2 - t1 = 0, на ноль делить нельзя')
except ValueError:
    print ('нельзя вводить строки')
else:
    Boost(v1, v2, t)
