# C++ Practice Questions

---

## 1. Setup & Hello World

1. What does `#include <iostream>` do?
2. What is the role of `main()` in a C++ program?
3. What does `std::cout` do, and what is `std::`?
4. What's the difference between `using namespace std;` and writing `std::` explicitly?
5. Write a program that prints your name, age, and favourite language on separate lines.
6. Without `using namespace std;`, write Hello World using full `std::` prefixes.

---

## 2. Drawing a Shape

1. What's the difference between `\n` and `endl`?
2. How do you print multiple lines using `cout`?
3. Print a right-angled triangle of height 5 using `*`.
4. Print a hollow rectangle of width 7, height 4 using `*` for borders and spaces inside.
5. Print this pyramid using only `cout` (no loops):
   ```
      *
     ***
    *****
   *******
   ```

---

## 3. Variables

1. What three things does declaring a variable define?
2. What is the difference between declaring and initializing a variable?
3. What happens if you use a variable before initializing it?
4. List four naming rules for variables in C++.
5. Declare variables for name, age, GPA, and student status. Print them in a sentence.
6. Swap two integer variables without using a third variable.

---

## 4. Data Types

1. List the six primitive data types in C++ and their typical sizes in bytes.
2. What's the difference between `float` and `double`?
3. What is integer overflow? Give an example.
4. How is `bool` represented internally in memory?
5. Declare one variable of each primitive type and print the size of each using `sizeof()`.
6. Demonstrate integer overflow using a `short int` at its maximum value (32767). Add 1 and print the result.

---

## 5. Working With Strings

1. What header do you need to use the `string` type?
2. How do you find the length of a string?
3. How do you access the character at index 3 of a string `word`?
4. What does `.substr(start, length)` do? Give an example.
5. Ask the user for first and last name separately. Print: "Hello, [First] [Last]! Your name has X characters."
6. Given "Hello, World!" — reverse it, print characters at even indices, and count the vowels.
7. Check if a string is a palindrome.

---

## 6. Working With Numbers

1. What is the result of `7 / 2` in C++? How do you get `3.5`?
2. What does `%` do? Give two real-world use cases.
3. What header is needed for `pow()`, `sqrt()`, and `abs()`?
4. What's the difference between prefix (`++i`) and postfix (`i++`) increment?
5. Take an integer and print: whether it's even/odd, its square root, and its absolute value.
6. Compute 2^10 without `pow()`, then verify using `pow()`.

---

## 7. Getting User Input

1. What operator does `cin` use to read input?
2. What's the difference between `cin >> name` and `getline(cin, name)`?
3. What happens to `cin` when the user enters the wrong data type?
4. Why do you sometimes need `cin.ignore()` before `getline()`?
5. Ask the user for name (with spaces), age, and city. Print a greeting using all three.
6. Ask the user to enter 5 numbers. Print their sum and average.

---

## 8. Building a Calculator

1. What control flow structure would you use to branch on an operator (+, -, *, /)?
2. Why must division by zero be explicitly handled?
3. What data type should store the operands, and why?
4. Build a calculator: takes two numbers and an operator, handles division by zero, prints the result.
5. Extend it: add `%` and `^` support. Keep running until the user types `q`.

---

## 9. Building a Mad Libs

1. How do you insert a variable into the middle of a `cout` statement?
2. Why is `getline()` better than `cin >>` for Mad Libs inputs?
3. Build a Mad Libs with at least 6 blanks (noun, verb, adjective, etc.) and print the story.
4. Wrap the game in a loop that continues if the user types `y`.

---

## 10. Arrays

1. What is an array? How does it differ from a regular variable?
2. What is the index of the first element?
3. What happens when you access an out-of-bounds index?
4. How do you find the number of elements using `sizeof()`?
5. Declare an array of 7 integers. Print all elements, their sum, average, max, and min.
6. Reverse an array of 10 integers in-place (no second array).
7. Implement linear search: return the index of a target, or -1 if not found.

---

## 11. Functions

1. What are the four main benefits of using functions?
2. What's the difference between a function declaration and a function definition?
3. What are parameters vs arguments?
4. What happens if you call a function before defining it without a prototype?
5. Write `greet(string name)` that prints "Hello, [name]! Welcome to C++." Call it 3 times.
6. Write `isPrime(int n)` returning true/false. Test for: 1, 2, 13, 25, 97.

---

## 12. Return Statement

1. What is the purpose of the `return` statement?
2. What does `void` mean as a return type?
3. Can a function have multiple `return` statements?
4. What's the difference between returning a value and printing it inside a function?
5. Write `max(int a, int b, int c)` returning the largest of three numbers.
6. Write `factorial(int n)` using a loop and return. Test for 0, 1, 5, 10.

---

## 13. If Statements

1. What values are "truthy" and "falsy" in C++?
2. What is short-circuit evaluation?
3. What is a compound condition? Give an example using `&&` and `||`.
4. Write a program that prints "Positive", "Negative", or "Zero" for a user-entered number.
5. Determine whether a year is a leap year (divisible by 4, except centuries unless also divisible by 400).

---

## 14. If Statements (con't)

1. What is an `else if` chain?
2. What is the ternary operator? Write its syntax.
3. What is the dangling else problem?
4. Write a grade calculator: A (≥90), B (≥80), C (≥70), D (≥60), F (<60).
5. Using only the ternary operator, print "Even"/"Odd" and "Pass"/"Fail" (score ≥50).
6. FizzBuzz 1–100: multiples of 3 → "Fizz", 5 → "Buzz", both → "FizzBuzz".

---

## 15. Building a Better Calculator

1. Why use separate functions for each operation instead of one big `main()`?
2. What is the benefit of separating input logic, computation logic, and output logic?
3. Refactor your basic calculator so each operation (+, -, *, /) is its own function. `main()` handles only I/O.
4. Build a calculator that keeps a running total. Type `r` to reset, `q` to quit. Print operation history at the end.

---

## 16. Switch Statements

1. What data types can be used in a `switch` expression?
2. What is fall-through, and how does `break` prevent it?
3. When is intentional fall-through useful?
4. Is the `default` case required?
5. Rewrite a grade printer (A/B/C/D/F) using `switch` (map with `score / 10`).
6. Build a menu-driven program with switch: 1) Say Hello 2) Exit.

---

## 17. While Loops

1. What is the structure of a `while` loop? When does it stop?
2. What is the difference between `while` and `do-while`?
3. What happens if the condition is false from the start?
4. Print a countdown from 10 to 0 using a while loop. Print "Blast off!" at the end.
5. Print the Fibonacci sequence up to the first value exceeding 1000.
6. Keep asking the user for a number between 1 and 100 until they enter a valid one.

---

## 18. Building a Guessing Game

1. How do you generate a random number in C++? What headers do you need?
2. Why do you seed `srand()` with `time(0)`?
3. How do you constrain a random number to [1, N]?
4. Build the classic guessing game: computer picks 1–100, user guesses, prints "Too high"/"Too low"/"Correct!" and attempt count.
5. Add difficulty levels: Easy (1–50, 10 tries), Medium (1–100, 7 tries), Hard (1–200, 5 tries).

---

## 19. For Loops

1. What are the three components of a `for` loop header?
2. What does `break` do? What does `continue` do?
3. What is an off-by-one error? Give an example and fix.
4. Print the multiplication table (×1 to ×12) for any user-entered number.
5. Find all prime numbers between 1 and 200 using nested for loops.
6. Given an array, find the second largest element.

---

## 20. Exponent Function

1. How can exponentiation be implemented using a loop?
2. What edge cases must an exponent function handle?
3. What is exponentiation by squaring, and why is it faster?
4. Write `myPow(double base, int exp)` using a loop. Handle negative exponents.
5. Implement exponentiation by squaring. Verify `myPow(2, 30)` equals `pow(2, 30)`.

---

## 21. 2D Arrays & Nested Loops

1. How do you declare a 2D array in C++?
2. How are 2D arrays stored in memory?
3. How do you access row 2, column 3 of array `grid`?
4. How do you pass a 2D array to a function?
5. Declare a 3×3 matrix, fill with 1–9, print in grid format.
6. Write a function that transposes an N×N matrix in-place.
7. Implement multiplication of two 3×3 matrices. Verify using the identity matrix.

---

## 22. Comments

1. What are the two types of comments in C++?
2. What's the difference between a comment explaining *what* code does vs *why*?
3. What makes a comment bad? Give two examples.
4. Take any 20-line program you've written. Add a file-level comment, inline comments for non-obvious lines, and a TODO.
5. Write a Doxygen-style comment block for `isPrime(int n)` with `@param`, `@return`, and `@example`.

---

## 23. Pointers

1. What does a pointer store?
2. What's the difference between `&` (address-of) and `*` (dereference)?
3. What is a null pointer? How do you declare one safely in modern C++?
4. What is pointer arithmetic?
5. Declare `int x = 42`. Print: the value of x, its address, and the value via pointer.
6. Write `swap(int* a, int* b)` that swaps two values using pointers. Verify it modifies originals.
7. Traverse an integer array using only pointer arithmetic (no `arr[i]`). Print each element and its address.

---

## 24. Classes & Objects

1. What's the difference between a class and a struct?
2. What are member variables and member functions?
3. What are the three access specifiers and what does each allow?
4. What is encapsulation?
5. Create a `Student` class with private `name` and `grade`, and public methods to set and print them. Create two objects and test.
6. Create a `BankAccount` class with `deposit()`, `withdraw()` (no overdraft), and `getBalance()`. Test with a series of transactions.

---

## 25. Constructor Functions

1. When is a constructor automatically called?
2. What is a default constructor?
3. What is a constructor initializer list? How does it differ from assignment in the body?
4. Can a class have multiple constructors? What is this called?
5. Create a `Rectangle` class with a default constructor (1×1) and a parameterized one. Add `area()`. Test both.
6. Create a `Counter` class that starts at a given value (default 0), with `increment()`, `decrement()`, `reset()`, `getValue()`. Print a message in the destructor.

---

## 26. Object Functions

1. What is the `this` pointer? When do you need it explicitly?
2. What does `const` after a member function signature mean?
3. What's the difference between a mutator and an accessor?
4. Create a `Circle` class with `area()`, `circumference()`, `isLargerThan(Circle other)`, and `scale(double factor)`.
5. Create a `StringProcessor` class with methods: `toUpperCase()`, `toLowerCase()`, `reverse()`, `wordCount()`, `isPalindrome()`. None should modify the original string.

---

## 27. Getters & Setters

1. Why not just make member variables public?
2. How can setters validate data before storing? Give a real example.
3. Should a getter modify the object? What keyword enforces this?
4. Create a `Temperature` class with a private Celsius double. Add `getCelsius()`, `getFahrenheit()`, `getKelvin()`, and a setter that rejects values below −273.15°C.
5. Create a `Password` class where the setter validates ≥8 chars, at least one digit and one uppercase letter. The getter returns the password masked (e.g., `"pass"` → `"****"`).

---

## 28. Inheritance

1. What problem does inheritance solve?
2. What's the difference between `public`, `protected`, and `private` inheritance?
3. What is method overriding? How does it differ from overloading?
4. What is a virtual function, and why is it needed for polymorphism?
5. Create a base class `Animal` with `speak()`. Derive `Dog` and `Cat` with their own sounds. Store them in an array of `Animal*` and call `speak()` on each.
6. Create a `Shape` base class with virtual `area()`. Derive `Circle`, `Rectangle`, and `Triangle`. Store in a `vector<Shape*>` and print the area of each.

---
