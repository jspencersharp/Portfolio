# This approach 

my_list = ["hi",19,'hello',98.98,'world',9]
sum=0
my_string = ""
output_type = ""
for item in my_list:
    if isinstance(item, int):
        sum =sum + item
        
        if output_type == "string":
           output_type = "mixed"
        else:
            output_type = "number"
    elif isinstance(item, str):
        my_string = my_string + item
        if output_type == "number":
            output_type = "mixed"
        else:
            output_type = "string"
print sum
print my_string
print output_typem