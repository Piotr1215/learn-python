# Learning python for C# developer

## Learning resources

- [W3c python tutorial](https://www.w3schools.com/python/default.asp)
- [Exercises](https://www.w3schools.com/python/exercise.asp)
- [DevOps Automation in Python](https://www.coursera.org/learn/devops-build-automation-python?specialization=python-scripting-devops)
- [Python automation in linux](https://linuxcourse.rutgers.edu/html/Lesson_11.html)

## Recommended extensions for VS Code

- Python
- Pylance - a little bit of type checking
- Test explorer UI - not python specific, but great extension for running tests
- Flake8 - linter for Python

## Some random packages

- scrape web pages [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [HTTP stuff](https://docs.python-requests.org/en/master/)

## Goal

The basic goal is to learn python for scripting purposes for DevOps-related tasks.

## C# vs Python comparison

### Imperative vs Procedural

C# leans more to imperative style (although it gets more and more functional updates recently). Python due to its dynamic nature can work reasonably well with different styles.

### Tidbits

- the value of an `input`function is ++always++ a string
- type casting `int()` `float()`
- both tabs and spaces are acceptable for indentation
- collections are zero indexed
- ptyhon has page similar to nuget.org, https://pypi.org/
- standard library functions: https://www.w3schools.com/python/python_ref_functions.asp
- all keywords: https://www.w3schools.com/python/python_ref_keywords.asp

### Syntax

#### Conditional

```python
if statement:
   execute me
elif: another condition:
    execute me instead
else:
    execute if none of the above true
```

#### Loops

While

```python
while condition evaluated to true/false:
    execute code
else:
    other condition executed
```

For

```python
for i in range(x):
    loop logic
    break #exit the loop
for i in "string":
    loop through string #Useful
```

#### Collections

List(mutable)

```python
lista = ["one", "two", "three"]
lista[0] #indexing
print("one" in lista) # find if value is in a list
print("one" not in lista) # find if value is not in a list
```

Tuples (immutable)

```python
tupelek = ("one", "two", "three")
```

Dictionaries (immutable)
Similar to JSON

```python
costam = {
    "key": "value",
    "key2": "value2"
}
```

#### Functions

```python
def metoda(param1, param2 = "costam"): # can have default values
    global varName # this keyword makes variable globally accessible
    return body
```

#### Lambda

```python
x = lambda a, b: a + b
#lambda arguments : expression
```

#### Exception handling

```python
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
```

## OOP

Pretty similar to C#, there are constructors, objects are created without `new` keyword, and methods are called with `.`

Inheritance syntax

```python
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
```

## Style guidelines

Follow pep8.org style guide.

## Virtualize the environment

Use devcontainer to virtualize your environment and install all the dependencies. This is better than venv

## Use click

Parse arguments using decorators with default values

## Resources

Ptyhon institute

## Active recall

### What is the pitput type of `input()` function?

### What are the 2 functions that type cast to numerical values?

### What method is used for indentation?

### From what index collections start

### What method inserts a new item into a list?

### What method adds element into a list?

### Are list copied by reference by default?

### What method to use to crete a new list based on existing list?

### Can a list hold elements of different data types?

### What keyword makes a variable globally accessible?

### What is `pass` keyword and when to use it?

### How to make child class inherit all methods and properties from parent class?