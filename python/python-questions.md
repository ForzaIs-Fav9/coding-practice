# Python Practice Questions

---

## 1. Setup & Hello World

1. How do you print something to the console in Python?
2. What is the Python REPL, and when would you use it?
3. What file extension do Python files use?
4. What does `print("Hello", "World")` output vs `print("Hello" + "World")`?
5. Write a program that prints your name, age, and favourite language on separate lines.
6. What is the difference between Python 2 and Python 3's `print` statement?

---

## 2. Variables & Assignment

1. Do you need to declare a variable's type in Python? Why not?
2. What are the naming rules for variables in Python?
3. What is multiple assignment? Give an example.
4. What does `x = y = z = 0` do?
5. Swap two variables in Python in one line.
6. What is the difference between `=` and `==`?

---

## 3. Data Types

1. List the five core built-in data types in Python.
2. How do you check the type of a variable?
3. What is the difference between `int`, `float`, and `complex`?
4. What does `type(True)` return? What does Python treat `True` as numerically?
5. Declare one variable of each core type and print its type using `type()`.
6. What is `None` in Python? What is it equivalent to in other languages?

---

## 4. Type Casting

1. How do you convert a string to an integer in Python?
2. What happens when you run `int("hello")`?
3. What is the difference between implicit and explicit type conversion?
4. What does `bool(0)`, `bool("")`, and `bool(None)` each return?
5. Ask the user to enter two numbers as strings. Convert them to floats and print their sum.
6. Write a program that takes an integer and prints its binary, octal, and hex representations using built-in functions.

---

## 5. Strings

1. How do you find the length of a string?
2. How do you access the last character of a string without knowing its length?
3. What is string slicing? Give the syntax and an example.
4. What do `.upper()`, `.lower()`, `.strip()`, and `.replace()` do?
5. What is an f-string? Write an example using one.
6. Given `s = "Hello, World!"` — reverse it, print every second character, and count the vowels.
7. Check if a string is a palindrome.

---

## 6. Numbers & Math

1. What is the difference between `/` and `//` in Python?
2. What does `**` do?
3. What does `%` do? Give two real-world use cases.
4. What module do you import for advanced math functions like `sqrt()` and `pow()`?
5. Take an integer from the user and print: whether it's even/odd, its square root (2 decimal places), and its absolute value.
6. Compute 2^10 without `**`, then verify using `**`.

---

## 7. User Input

1. What function do you use to get user input in Python?
2. What type does `input()` always return?
3. How do you prompt the user and read an integer in one line?
4. What happens if the user types "hello" when you expect an integer from `int(input())`?
5. Ask the user for their name, age, and city. Print a greeting using all three.
6. Ask the user to enter 5 numbers one by one. Print their sum and average.

---

## 8. If Statements

1. What is the syntax of an `if-elif-else` block in Python?
2. What values are falsy in Python? List at least five.
3. What is a ternary expression in Python? Write the syntax.
4. Write a program that prints "Positive", "Negative", or "Zero" for a user-entered number.
5. Determine whether a year is a leap year.
6. Write a grade calculator: A (≥90), B (≥80), C (≥70), D (≥60), F (<60).

---

## 9. For Loops

1. What is the syntax of a `for` loop in Python?
2. What does `range(1, 10, 2)` produce?
3. What do `break` and `continue` do inside a loop?
4. What does the `else` clause on a `for` loop do?
5. Print the multiplication table (×1 to ×12) for any number the user enters.
6. FizzBuzz 1–100: multiples of 3 → "Fizz", 5 → "Buzz", both → "FizzBuzz".
7. Find all prime numbers between 1 and 200.

---

## 10. While Loops

1. What is the structure of a `while` loop? When does it stop?
2. What is the difference between `while` and `for` in Python?
3. What is an infinite loop? How do you exit one intentionally?
4. Print a countdown from 10 to 0. Print "Blast off!" at the end.
5. Print the Fibonacci sequence up to the first value exceeding 1000.
6. Keep asking the user for a number between 1 and 100 until they enter a valid one.

---

## 11. Functions

1. How do you define a function in Python?
2. What is the difference between a parameter and an argument?
3. What does a function return if there is no `return` statement?
4. What are default parameter values? Give an example.
5. What is the difference between `*args` and `**kwargs`?
6. Write `is_prime(n)` returning True/False. Test for: 1, 2, 13, 25, 97.
7. Write `repeat_string(s, n)` that returns `s` repeated `n` times. E.g., `repeat_string("ha", 3)` → `"hahaha"`.

---

## 12. Scope

1. What is the difference between local and global scope?
2. What does the `global` keyword do?
3. What is the `nonlocal` keyword used for?
4. What is a `NameError`, and when does it occur?
5. Write a program with a global counter that two different functions both increment. Print the final value.
6. Explain what happens here — will it work? Why or why not?
   ```python
   x = 10
   def foo():
       print(x)
       x = 20
   foo()
   ```

---

## 13. Lists

1. How do you create a list in Python? Can it hold mixed types?
2. What is the difference between `.append()` and `.extend()`?
3. What does `.pop()` do with and without an argument?
4. How do you sort a list in-place vs return a new sorted list?
5. What is list slicing? Give three different slicing examples.
6. Declare a list of 7 integers. Print: all elements, sum, average, max, min.
7. Reverse a list in-place. Then reverse it again using slicing.
8. Remove all duplicates from a list while preserving order (no sets).

---

## 14. Tuples

1. What is a tuple? How does it differ from a list?
2. Can you modify a tuple after creation? What happens if you try?
3. What is tuple unpacking? Give an example.
4. Why would you use a tuple over a list?
5. Write a function that returns multiple values as a tuple. Unpack them on the calling side.
6. Count the number of times a value appears in a tuple using a built-in method.

---

## 15. Dictionaries

1. What is a dictionary? What are its keys and values?
2. How do you access a value safely (without risking a `KeyError`)?
3. What does `.items()`, `.keys()`, and `.values()` each return?
4. How do you add, update, and delete a key-value pair?
5. Create a dictionary of 5 students with their grades. Print only students who scored ≥80.
6. Count the frequency of each character in a string using a dictionary.
7. Merge two dictionaries into one (both ways: Python 3.5+ and 3.9+).

---

## 16. Sets

1. What is a set? What makes it different from a list?
2. Can a set contain duplicate values? What happens if you try to add one?
3. What are the set operations for union, intersection, and difference?
4. When would you use a set over a list?
5. Given two lists, use sets to find: elements in both, elements only in the first, elements in either but not both.
6. Remove all duplicates from a list using a set (one line).

---

## 17. List Comprehensions

1. What is the syntax of a list comprehension?
2. How do you add a condition to a list comprehension?
3. Rewrite this loop as a list comprehension:
   ```python
   squares = []
   for i in range(10):
       squares.append(i ** 2)
   ```
4. What is a dictionary comprehension? Give an example.
5. Use a list comprehension to get all even numbers between 1 and 50.
6. Use a list comprehension to flatten a 2D list (list of lists) into a 1D list.

---

## 18. Exception Handling

1. What is the syntax of a `try-except` block?
2. What is the difference between `except Exception` and `except ValueError`?
3. What does the `else` clause do in a try-except block?
4. What does `finally` do? When is it guaranteed to run?
5. Write a program that safely takes an integer from the user, handling `ValueError` if they type non-numeric input. Keep asking until valid.
6. Write a function `safe_divide(a, b)` that handles division by zero and returns `None` in that case.

---

## 19. File I/O

1. What does `open("file.txt", "r")` do? What modes are available?
2. Why should you use `with open(...)` instead of just `open(...)`?
3. What is the difference between `.read()`, `.readline()`, and `.readlines()`?
4. How do you write to a file? What's the difference between `"w"` and `"a"` mode?
5. Write a program that creates a file, writes 5 lines to it, then reads and prints them back.
6. Read a text file and print: the total number of lines, total words, and the most common word.

---

## 20. Modules & Imports

1. What is a module in Python?
2. What is the difference between `import math` and `from math import sqrt`?
3. What does `import math as m` do?
4. What is the `__name__ == "__main__"` pattern used for?
5. Use the `random` module to generate: a random integer between 1–100, a random float, and a random choice from a list.
6. Use the `os` module to: print the current working directory, list all files in it, and check if a file exists.

---

## 21. Classes & Objects

1. How do you define a class in Python?
2. What is `__init__`? When is it called?
3. What is `self`? Why does every method need it as the first parameter?
4. What is the difference between an instance variable and a class variable?
5. Create a `Student` class with `name` and `grade`. Add a method `print_info()`. Create two objects and test.
6. Create a `BankAccount` class with `deposit()`, `withdraw()` (no overdraft), and `get_balance()`. Test with a series of transactions.

---

## 22. Inheritance

1. What is the syntax for a derived class in Python?
2. What does `super()` do? When do you need it?
3. What is method overriding?
4. What is `isinstance()` and when would you use it?
5. Create a base class `Animal` with a `speak()` method. Derive `Dog` and `Cat` with their own sounds. Create a list of animals and call `speak()` on each.
6. Create a `Shape` base class with `area()` and `perimeter()`. Derive `Circle`, `Rectangle`, and `Triangle`. Store them in a list and print the area of each.

---
