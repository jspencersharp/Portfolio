# This approach uses booleans to determine if we've encountered strings or ints

l  = ['magical','unicorns']
sum = 0
T = ""
isstring = False;
isint = False;
for i in range(0,len(l)):
    if(type(l[i]) == str or int or float):
    
        if(type(l[i]) == str ):
            T = T + " " + l[i] 
            isstring = True
            
        elif(type(l[i]) == int or float):
            sum = sum+l[i]
            isint = True
        
if (isstring and isint):
    print ("It's a mixed array")
if (isstring): 
    print ("String:" + str(T))
if (isint):
    print ("Sum:" +str(sum))