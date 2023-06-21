# Author: WILFRED MAJALIWA
# Session: Morning

# CONDITIONAL LOGIC

# if else
age = 17

if age > 18 or age == 18:
    print('adult')
elif age <= 12:
    print('kid')
else:
    print('teenager')

# Dictionaries
# 1. key-value. 2. key is unique. 3. key is immutable. 
# 4. value is mutable. 5. value can be duplicated. Ordered
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
print(d.get('Michael')) # Another way to get value from dict. But it has a default value of None
print(d.get('Me', -1)) # -1 is default value. Useful when key is not in dict
print(len(d))


# Loops. DO & WHILE
# for loop
names = ['Michael', 'Bob', 'Tracy', 'Bob']
for name in names:
    print(name)

i = len(names) - 1
while i >= 0:
    print(names[i])
    i -= 1

# CONTINUE & BREAK STATEMENTS
names = ['Michael', 'Bob', 'Tracy', 'Bob']

for name in names:
    # if name == 'Bob':
    #     print(name)
    #     continue
    
    if name == 'Bob':
        print(name)
        break
    
# EXCEPTION HANDLING USING TRY & EXCEPT
numbers = [1, 2, 3]

try:
    print(numbers[5])
except IndexError as error:
    print("IndexError: ", error)
finally:
    print("This will always execute")

# 
# 
# EXERCISE ON EXCEPTION HANDLING, DICTIONARIES, LOOPS, AND CONTROL FLOW
#
#
emotion = {
    1: 'Too bad.',
    2: 'Take a walk.',
    3: 'Remember the movie Joy.',
    4: 'Sorrow is a valid emotion.',
    5: 'Not too bad.',
    6: 'Take a deep breath.',
    7: 'You are loved.',
    8: '8 is good. 8 is great.',
    9: 'You are strong.',
    10: 'You are beautiful.',
}
emote = input("On a scale of 1 - 10, how are you feeling today? ")

try:
    emote = int(emote)
except ValueError:
    print("Please enter a number between 1 - 10.")
    exit()

if emote in emotion:
    print(emotion[emote])
else:
    print("Please enter a number between 1 - 10.")








