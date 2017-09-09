#part 1 
# def draw_stars():
#     x = [4,6,1,3,5,7,25]
#     for i in range(0,len(x)):
#         temp = x[i]
#         print("*" * temp)

# draw_stars()
#part 2
import string 

def star2(arr):
    for i in arr:
        if isinstance(i, int):
            print "*" * i
        elif isinstance(i, str):
            length =len(i)
            letter =i[0].lower()
            print letter * length
        
star2([4,"Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
