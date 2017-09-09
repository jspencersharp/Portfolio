#Filter by Type Project
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

#Integer
tester = lL

curr_type = type(tester)
if curr_type is int:
    if tester >= 100:
        print "that's a big number"
    else:
        print "that's a small number!"
elif curr_type is str:
        if len(tester) >= 50:
            print "Long sentence."
        else:
            print "short sentence."
elif isinstance(tester, list):
            if len(tester) >= 10:
                print "Big List!"
            else: 
                print "short list!"


