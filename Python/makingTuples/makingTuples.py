# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def makeTup(arr):
   list = []
   for i in arr:
    #    print i
    #    print my_dict[i]
       k = (i,my_dict[i])
    #    print k
       list.append(k)
       print list

makeTup(my_dict)
