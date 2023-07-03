"""
DAY 6:
- REGEX
- GEnerators & Iterators
- Decorators
- Context Managers
- Multithreading & Multiprocessing
"""

# REGEX# Summary of Regular Expression Patterns
# /d - digit 0-9 (any digit) 
# /D - non-digit (any non-digit character)
# /s - whitespace (tab, space, newline, etc.)
# /S - non-whitespace (any non-whitespace character)
# /w - alphanumeric (any letter, digit, or underscore)
# /W - non-alphanumeric (any non-letter, digit, or underscore)
# /b - word boundary (between \w and \W)
# /B - non-word boundary
# /A - beginning of string
# /Z - end of string
# /z - end of string
# /G - end of previous match
# /n - backreference to group number "n"
# /c - matches any character or escape sequence that may be
#      treated like a character
# /Q - quote (disable) pattern metacharacters until /E
# /E - end quote (enable) pattern metacharacters after /Q
# /p{name} - matches the named group
# /P{name} - matches the named group
# /k<name> - backreference to named group
# /k'name' - backreference to named group
# /x - ignore whitespace and comments
# /i - case-insensitive matching
# /L - locale character classes
# /u - unicode character classes
# /8 - use ASCII rules
# /a - ASCII character classes
# /A - POSIX character classes (US-ASCII only)
# /u - unicode character classes
# /U - Unicode character properties
# /X - Unicode character properties
# .: any character except newline
# ^: start of string
# $: end of string
# *: match 0 or more repetitions
# +: match 1 or more repetitions
# ?: match 0 or 1 repetitions
# {m,n}: match m to n repetitions
# {m,n}?: match m to n repetitions, not greedily
# {m,}: match m or more repetitions
# {m,}?: match m or more repetitions, not greedily
# {m}: match exactly m repetitions
# {m}?: match exactly m repetitions, not greedily
# (?#...): comment
# (?:...): non-capturing group
# (?P<name>...): named capturing group
# (?P=name): backreference to named group
# (?=...): positive lookahead assertion
# (?!...): negative lookahead assertion
# (?<=...): positive lookbehind assertion
# (?<!...): negative lookbehind assertion
# (?(id/name)yes-pattern|no-pattern): conditional
# \number: backreference to group number "number"
# \A: start of string
# \b: word boundary
# \B: non-word boundary 
# [ ]: character set (any character in set)
# [^ ]: negated character set (any character except those in set)
# ^: start of string (or line, in multiline mode)
# $: end of string (or line, in multiline mode)


# Matching & Searching using regex
# Match firsst word with regex


import re
# re.match(pattern, string, flags=0)
name = "Wilfred Majaliwa M"
# Match first word
# \w+ - one or more word characters
match = re.match(r'(\w+)', name, re.I)
if match:
    # print("Match:", match.group())
    pass

# I - ignore case
# re.I - ignore case
matches = re.findall(r'(\w+) (\w+)', name, re.I)
if matches:
    # print("Findall:", matches)
    pass


# Validate email address using regex
def validate_email(email):
    # ^[a-zA-Z0-9_.+-] - start with any of these characters
    # + - one or more
    # @ - @ symbol
    # \. - dot
    # [a-zA-Z0-9-] - any of these characters
    # $ - end of string
    # pattern = xxxx@xxxx.xxxx
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    match = re.match(pattern, email)
    if match:
        return True
    return False

email_pass = "wilfredmajaliwa@gmail.com"
email_reject = "wilfredmajaliwa@gmail"

# print(validate_email(email_pass)) # True
# print(validate_email(email_reject)) # False


# Generators & Iterators
# Generators are functions that return an object that can be iterated over
# Generators use yield keyword instead of return
# Generators are memory efficient
# Generators are lazy
# Generators are used to create iterators
# Generators are used to create infinite sequences
# Generators are used to create data pipelines
# Generators are used to create data processing pipelines


# Create a generator
def my_generator():
    yield 1
    yield 2
    yield 3

# print(my_generator()) # <generator object my_generator at 0x7f9b1c0b6f20>
# print(next(my_generator())) # 1
# print(next(my_generator())) # 2
# print(next(my_generator())) # 3
# print(next(my_generator())) # StopIteration


# Create a function that returns the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# Yield the factorial of a range of numbers from 0 to 10 using a generator
def factorial_generator(n, m):
    for i in range(n, m):
        # The yield keyword returns a generator object that can be iterated over
        yield f"The factorial of {i} is {factorial(i)}"
        
# Iterate over the generator object
for factorial_value in factorial_generator(1, 10):
    # print(factorial_value)
    pass


def squares(n, m):
    for i in range(n, m):
        yield f"The square of {i} is {i**2}"

# Create a generator object
squares_generator = squares(1, 6)

# Print the first 5 squares of numbers from 1 to 5
for square in squares_generator:
    # print(square)
    pass


# Decorators
# Decorators are functions that take another function as an argument
# Decorators add functionality to an existing function
# Decorators return another function
# Decorators are used to modify the behavior of a function
# Decorators are used to modify the behavior of a class

# Create a decorator function, my_decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator # Referring to the decorator function, my_decorator
# Extra functionality to add to the wrapper function
def say_hello():
    # This is the implementation to be added to the wrapper function
    print("Hello")

say_hello()