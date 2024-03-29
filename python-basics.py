import streamlit as st
from re import sub, IGNORECASE

st.title("Python Programming")

st.write(
    """
Python is among the most popular programming languages in the world. Here, we will go over some basic functionality and syntax in the Python Language needed before starting to apply Python in a Data Science context.

Python is a high-level language, which means it is optimized to be human-readable, instead of machine-readable. Python is an interpreted language, which means it is not compiled directly to machine code. As an interpreted language, it is interactive, meaning Python scripts are run directly by the interpreter and provide immediate feedback.
"""
)

st.subheader("White Space")

st.write(
    """
Python does not make use of semi-colons or curly braces to separate code block as does Javascript or other popular programming languages. Instead, it uses whitespace. To demonstrate this, have a look a the following nested for loop.

```python
for i in range(10):
  print(i)              # code executed in \"i\" loop
  for j in range(2):
    print(j*i+i)        # code executed in \"j\" loop

print(\"out of the loop\")
```

This so called \"whitespace formatting\" is ignored inside of parenthesis and brackets to make it easier to write readable code.

```python
list_of_lists = [ [1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9] ]
```

Using the nested for loops from above, we could do some cool stuff with our `list_of_lists` variable. The code below loops through the items in the outer list, and then loops the the items inside of each nested list, appending them to a flat list.

```python
flat_list = []

for i in list_of_lists:
  for j in i:
    flat_list.append(j)

print(flat_list)          # [1, 2, 3, ..., 9]
```
"""
)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = []

for i in list_of_lists:
    for j in i:
        flat_list.append(j)

flat_list

st.subheader("Declaring Variables")

st.write(
    """
In Python, variables are declined by using the assignment operator `=`. There is also no need for a keyword like `var`. Variables can hold integers, floating point number (decimal) number, strings, lists or dictionaries.
  """
)

st.subheader("Strings and Integers")

st.write(
    """
Python is dynamically typed, that means we can declare a variable as an integer on one line, and then in the next assign it to a string. If we wanted to store two integers in the variables `x` and `y`, then add them together, and then reassign the value of `x` to a string, we could write it like this:

```python
x = 1
y = 1

x + y   # 3

x = "Its a lovely day for a walk in the park"
```
"""
)

x = 1
y = 2
x + y

x = "Its a lovely day for a walk in the park"

x

st.write(
    """
When declaring string variables, there are few idiosyncrasies worth noting. First, to get a multi-line string you use triple quotes.

```python
\"\"\"
This string can span multiple lines.
Which can be helpful when writing docstrings for functions as we will see below.
\"\"\"
```

We might also want to escape certain characters or encode special characters within a string. For example, using a quotation mark inside of a string, or encoding a tab character.

```python
"\\"We can't go in there\\" he said."
"\\t \\"Why not?\\" asked the boy."
```
"""
)

st.subheader("Lists")

st.write(
    """
Lists are ordered collections of information. The information can be of any type and types can even be mixed inside of a list. Most of the time, however, lists only contain data of a single type. To declare a list, square brackets are used `[]`, and the individual values are separated by commas.

We can calculate values from the list, like getting the length of a list by using Python's `len` function, or calculating the sum of all items (only if all items are of type integer) using Python's `sum` function. We can combine the `list()` and `range()` function to generate lists of the length we pass as an argument.

Because lists are ordered collections, each item in a list has an index, starting at zero. Using these indices, we can extract individual values or sub-segments from a list using square brackets. If we only want items from the end of a list, we can use negative indices to count from the back of a list. The last item in a list has index -1. If we want a copy of the original, we just don't specify any indices in the square brackets.

We can check if a value exists in a list by using Python's `in` operator. Or add additional values to the end of a list, a procedure called contatenating, with the list's `extend` method. Beware, the `extend` method will modify your original list. If you don't want that, you can use the `+` operator and assign the result to a new variable.

Python also offers a nice syntax for unpacking values from a list. This is useful when we know the length of the list and want to use the individual values for separate calculations. Sometimes, we only need to use one value from a list, in order to discard the additional values use an underscore as the variable name for the value you want to discard.

```python
integers = [1, 2, 3]
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

integers_len = len(integers)    # 3
lol_len = len(list_of_lists)    # 3

integers_sum = sum(integers)    # 6

ten = list(range(10))       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
six = ten[6]                # 6
six_to_end = ten[6:]        # [6, 7, 8, 9]
start_to_four = ten[:5]     # [0, 1, 2, 3, 4]
three_to_six = ten[3:7]     # [3, 4, 5, 6]
nine = ten[-1]              # 9
last_three = ten[-3:]       # [7, 8, 9]
copy_ten = ten[:]           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

1 in ten                    # True
11 in ten                   # False

ten.extend([10, 11, 12])    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

11 in ten                   # True

seven = list(range(7))
new_ten = seven + [8, 9]

results = [80, 90]
res_one, res_two = results  # res_one equals 80, res_two equals 90

_, important = results      # important equals 90
```
    """
)

integers = [1, 2, 3]
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

st.subheader("Tuples")

st.write(
    """
Tuples are like lists, only immutable. Immutable means their values cannot be changed.
    """
)

st.subheader("Modules")

st.write(
    """
Python has a lot of built in functionality as well as third party libraries that are not leaded by default. They are made available as modules. For example, if we needed to write regular expression switch out the word \"the\" for the french version \"le\", we could import the `re` module and use its `sub` method.

```python
import re

sentence = \"The quick brown fox jumped over the lazy dog\"

frenchify = re.sub(\"the\", \"le\", sentence, flags=re.IGNORECASE)        # \"le quick brown fox...\"
```

Importing the whole regex module for our use case might be a little overkill, since we are only using a small part of it for this example. We can import specific items from a module like this:

```python
from re import sub, IGNORECASE

sentence = \"The quick brown fox jumped over the lazy dog\"

frenchify = sub(\"the\", \"le\", sentence, flags=IGNORECASE)        # \"le quick brown fox...\"
```
"""
)

sentence = "The quick brown fox jumped over the lazy dog"

frenchify = sub("the", "le", sentence, flags=IGNORECASE)

frenchify

st.write(
    """
We can also rename the modules that we import into our programs. This is especially helpful for modules which we use a lot of when the names are very long. In Data Science, a few packages that are very often used are `numpy`, `pandas` and `matplotlib`. Due to the frequency of use, and in the case of matplotlib, the length of the module name, these packages are often abbreviated.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
"""
)

st.subheader("Functions")

st.write(
    """
Using variables, we are able to store values and perform calculations using those values. Functions give a way to store the calculations themselves inside of variables. Then, anytime we need it to perform an operation, we just call the function by name.

In order to describe what a function does, there is a convention in python called a docstring. Docstrings are surrounded in triple quotes and have a specific syntax of their own to allow to easily auto-generated documentation. Read the [specification for docstrings](https://www.python.org/dev/peps/pep-0257/) for more information.

```python
def add_numbers(x, y=0):
  \"\"\"Return the sum of two numbers.

  Keyword arguments
  x -- the first number
  y -- the second number (default 0)
  \"\"\"
  return x + y

add_numbers(1, 2)
```
"""
)


def add_numbers(x, y):
    """Return the sum of two numbers.

  Keyword arguments
  x -- the first number
  y -- the second number (default 0)
  """
    return x + y


sum = add_numbers(1, 2)

sum

st.subheader("Exceptions")

st.write(
    """
Because Python is not compiled, any errors in your code will cause your program to crash at runtime. One way to handle these errors is with `try` and `except`

```python
def divide_numbers(x, y):
  \"\"\"Divides two numbers

  Keyword arguments
    x -- the first number
    y -- the second number (default 0)
  \"\"\"
  try:
    return x / y
  except ZeroDivisionError:
    return "cannot divide by zero"

quotient = divide_numbers(2, 0)

quotient  # cannot divide by zero
```
  """
)


def divide_numbers(x, y):
    """Divides two numbers

  Keyword arguments
    x -- the first number
    y -- the second number (default 0)
  """
    try:
        return x / y
    except "Divide by zero error":
        return "cannot divide by zero"


quotient = divide_numbers(2, 0)

quotient
