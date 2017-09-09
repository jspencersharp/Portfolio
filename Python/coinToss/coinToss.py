def coinToss():
    print("Coin Toss")
    count = 0
    headCount = 0
    tailCount = 0
    for i in range(0,5001):
        from random import randint
        flip_rounded = randint(0,1)
        # print flip_rounded
        # flip = random(0, 1)
        # flip_rounded = round(flip)
        if flip_rounded == 0:
            print("Attempt #",count,": Throwing a coin... It's a head!... Got",headCount," head(s) so far and ",tailCount, "tails(s) so far")
            count = count+1
            headCount = headCount+1
        elif flip_rounded == 1:
            print("Attempt #",count,": Throwing a coin... It's a tale!... Got",tailCount," tails(s) so far and ",headCount, "head(s) so far")
            count = count+1
            tailCount = tailCount+1



coinToss()