#odd/even
"""
def oddEven ():
    for i in range(1, 2001):
        # print i 
        if i % 2 == 1:
            # print i
            print("Number is", i, "This is an odd number")
        else:
            # print i
            print("Number is", i, "This is an even number")

print "test"
"""
#oddEven()

#Multiply
def mult(a, val):
    for x in range(0, len(a)):
        a[x] *= val
    print a

# mult([2,4,10,16], 5)
#hacker challenge

def HackerC(arr):
    print arr
    new_arr = []
    for x in arr:
        print x
        val_arr = []
        for i in range(x):
            val_arr.append(1)
        new_arr.append(val_arr)
    return new_arr

y = HackerC(mult([2,4,5],3))
print y


# this last function DOESN'T work... I'm not sure why. I've talked to someone else and reviewed the code and we think it looks OK but it is hanging on line 29 (for x in arr:)... says TypeError: 'NoneType' object is not iterable