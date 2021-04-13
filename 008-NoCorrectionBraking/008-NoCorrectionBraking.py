# 008-NoCorrectionBraking.py
# "No correction braking" is my best attempt at translating "ブレーキ込め直しなし"

# ブレーキ込め直しなし is an advanced train braking technique.
# Once the train driver applies brakes to a certain maximum level,
# they only release the brake gradually until the train stops.

# This is an example of no correction braking:
# 0 > 1 > 6 > 4 > 2 > 0        
# ^ upon reaching the maximum level of 6, the braking level decreases only.

# This program reads in a LF-separated list of integers,
# and determine whether the array indicates a no correction braking.

isValid = True
lastInp = 0
release = False

while True:
    try:
        thisInp = int(input())
        
        if release and thisInp > lastInp:
            isValid = False
            break
        elif not release and thisInp < lastInp:
            release = True
    
        lastInp = thisInp
    
    except:
        break
    
print(isValid)
