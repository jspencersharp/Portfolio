def grade(score):
    if score > 60 and score < 69:
        print("score:", score,"Your grade is D")
    elif score > 70 and score < 80:
            print("score:", score,"Your grade is C")
    elif score > 80 and score < 90:
            print("score:", score,"Your grade is B")
    elif score >90: 
        print("score:", score, "Your grade is A")
    else:
        print("your grade is not between A-D")
grade(61)

# import random
# random_num = random.random()
# random_num = random.randint()
