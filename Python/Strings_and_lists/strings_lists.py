"""
#find and replace
words = "It's thanksgiving day. It's my birthday, too!"
print words
print words.find("day")
words = words.replace("day","month")
print words
"""
"""
#min and max
x = [2,54,-2,7,12,98]
print x
print min(x)
print max(x)
"""
"""
#first and last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x)-1]
"""

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
list_1 = x[:len(x)/2]
list_2 = x[len(x)/2:]
print "first list", list_1
print "second list", list_2
list_2.insert(0,list_1)
print list_2

