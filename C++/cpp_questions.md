# C++ Question Anthology

> *From zero to boss — one question at a time.*

---

## Chapter 1 — Variables & Data Types
*"Name your data before it names you."*

**Q1.** Store your name, age, height (in cm), and whether you like coding (`true`/`false`) in correctly-typed variables. Print all four on separate lines with labels.

```
Expected output:
Name   : ...
Age    : ...
Height : ... cm
Coder  : ...
```

**Q2.** Store the number `1000000000` (one billion) in an `int`, then in a `long long`. Multiply both by 3 and print the results. Explain the difference you see using a comment in your code.

```
Expected output:
int result : -1294967296   (overflow!)
ll result  : 3000000000   (correct)
```

**Q3.** Declare a `float` and a `double`, both storing the value `3.14159265358979`. Print both with 15 decimal places using `setprecision(15)`. Which one is more accurate?

```
Expected output:
float  : 3.141592741012573
double : 3.141592653589790
```

---

## Chapter 2 — User Input & Working With Numbers
*"The program listens. Then it calculates."*

**Q4.** Ask the user for two integers. Print their sum, difference, product, quotient, and remainder. Handle the case where the second number is 0 — print a warning instead of crashing.

```
Expected output:
Enter two numbers: 17 5
Sum        : 22
Difference : 12
Product    : 85
Quotient   : 3
Remainder  : 2
```

**Q5.** Ask the user for a temperature in Celsius. Convert it to Fahrenheit (`F = C * 9/5 + 32`) and Kelvin (`K = C + 273.15`). Print all three rounded to 2 decimal places.

```
Expected output:
Enter temperature (C): 37
Celsius    : 37.00
Fahrenheit : 98.60
Kelvin     : 310.15
```

**Q6.** Ask the user for the radius of a circle. Compute and print the area and circumference. Use your own approximation of pi (`3.14159`) stored in a `const double`.

```
Expected output:
Enter radius: 7
Area         : 153.94
Circumference: 43.98
```

---

## Chapter 3 — If Statements & Switch
*"The fork in the road is where programs come alive."*

**Q7.** Ask the user for a year. Using `if/else`, determine if it is a leap year. A year is a leap year if it is divisible by 4, except century years which must be divisible by 400.

```
Expected output:
Enter year: 2000
2000 is a leap year.

Enter year: 1900
1900 is NOT a leap year.
```

**Q8.** Ask the user for a single digit (0–9). Using a `switch` statement, print its English word equivalent. If the input is not 0–9, print `"Invalid digit"`.

```
Expected output:
Enter digit: 7
Seven
```

**Q9.** Ask the user for three side lengths. Using `if/else` determine if they form: an equilateral triangle (all equal), isosceles (two equal), scalene (none equal), or not a triangle at all (triangle inequality rule).

```
Expected output:
Enter sides: 5 5 8
Isosceles triangle.

Enter sides: 1 2 10
Not a valid triangle.
```

**Q10.** Write a simple calculator. Ask the user for two numbers and an operator (`+`, `-`, `*`, `/`). Use a `switch` statement to perform the correct operation. Handle division by zero gracefully.

```
Expected output:
Enter: 15 / 0
Error: Division by zero.

Enter: 8 * 9
Result: 72
```

---

## Chapter 4 — For & While Loops
*"Repetition is not monotony — it is power."*

**Q11.** Print the multiplication table for a number entered by the user, from 1 to 12, neatly formatted.

```
Expected output:
Enter number: 7
7  x  1  =   7
7  x  2  =  14
...
7  x 12  =  84
```

**Q12.** Using a `while` loop, keep asking the user to enter a positive number. Compute and print its factorial. Stop when the user enters 0. Count how many factorials were computed.

```
Expected output:
Enter number (0 to quit): 5
5! = 120
Enter number (0 to quit): 3
3! = 6
Enter number (0 to quit): 0
Computed 2 factorial(s).
```

**Q13.** Print a right-angled triangle of stars. Ask the user for the height `n`. Row `i` should have `i` stars. Use a nested for loop.

```
Expected output:
Enter height: 5
*
**
***
****
*****
```

**Q14.** Print all prime numbers between 1 and `n` (user-provided) using nested loops. For each number, check if any integer from 2 to its square root divides it evenly.

```
Expected output:
Enter n: 30
2 3 5 7 11 13 17 19 23 29
```

---

## Chapter 5 — Functions & Return Statements
*"Write once. Call forever."*

**Q15.** Write four separate functions — `add`, `subtract`, `multiply`, `divide` — each taking two `double`s and returning a `double`. Build a menu-driven calculator that calls the right function based on user choice.

```
Expected output:
1. Add   2. Subtract   3. Multiply   4. Divide
Choice: 3
Enter two numbers: 6 7
Result: 42.00
```

**Q16.** Write a function `isPrime(int n)` that returns `true` if `n` is prime, `false` otherwise. Use it to print all primes up to 100, five per line.

```
Expected output:
 2   3   5   7  11
13  17  19  23  29
...
```

**Q17.** Write a function `reverse(int n)` that returns the digit-reversal of a number (e.g. `1234 → 4321`). Then write `isPalindrome(int n)` that uses `reverse()` to check if a number reads the same forwards and backwards.

```
Expected output:
Enter number: 12321
Reversed    : 12321
Palindrome  : YES

Enter number: 1234
Reversed    : 4321
Palindrome  : NO
```

**Q18.** Write a recursive function `fibonacci(int n)` that returns the nth Fibonacci number. Print the first 15 Fibonacci numbers using a for loop that calls this function.

```
Expected output:
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
```

---

## Chapter 6 — Arrays
*"Many values. One name. Total control."*

**Q19.** Ask the user to enter 10 integers into an array. Without using any built-in sort or min/max functions, find and print the maximum, minimum, sum, and average.

```
Expected output:
Enter 10 numbers: 4 7 2 9 1 5 8 3 6 10
Max     : 10
Min     : 1
Sum     : 55
Average : 5.50
```

**Q20.** Store 8 numbers in an array. Write your own bubble sort to sort them in ascending order. Print the array before and after sorting.

```
Expected output:
Before: 64 34 25 12 22 11 90 45
After : 11 12 22 25 34 45 64 90
```

**Q21.** Ask the user for an array of `n` integers and a target number. Implement linear search — print the index if found, or `"Not found"` if not. Then count how many times the target appears.

```
Expected output:
Array  : 3 7 2 7 9 7 4
Target : 7
First found at index: 1
Appears 3 time(s).
```

---

## Chapter 7 — Strings
*"Characters in sequence. Meaning in context."*

**Q22.** Ask the user for a sentence. Count the number of vowels, consonants, spaces, and digits in it. Print each count on its own line.

```
Expected output:
Enter sentence: Hello World 123
Vowels     : 3
Consonants : 7
Spaces     : 2
Digits     : 3
```

**Q23.** Ask the user for a word. Check if it is a palindrome by comparing characters from both ends moving inward. Do not use any built-in reverse function.

```
Expected output:
Enter word: racecar
racecar is a palindrome.

Enter word: hello
hello is NOT a palindrome.
```

**Q24.** Ask the user for a string. Build and print a new string that contains only the characters at even indices (0, 2, 4...). Then print only the characters at odd indices. Concatenate both and print the final combined string.

```
Expected output:
Input    : Harshith
Even idx : Hrsh
Odd idx  : ait
Combined : Hrshaiti
```

---

## Chapter 8 — 2D Arrays & Nested Loops
*"The grid is where real programs live."*

**Q25.** Fill a 5×5 2D array with values 1–25 row by row. Print it as a neatly formatted grid. Then print the sum of each row and each column separately.

```
Expected output:
 1  2  3  4  5   | Row sum: 15
 6  7  8  9 10   | Row sum: 40
11 12 13 14 15   | Row sum: 65
16 17 18 19 20   | Row sum: 90
21 22 23 24 25   | Row sum: 115
Col sums: 55 60 65 70 75
```

**Q26.** Create a 4×4 matrix using user input. Write a function `transpose(int m[][4], int n)` that swaps rows and columns and prints the transposed matrix.

```
Expected output:
Original:          Transposed:
1  2  3  4         1  5  9  13
5  6  7  8         2  6  10 14
9  10 11 12        3  7  11 15
13 14 15 16        4  8  12 16
```

**Q27.** Create a 5×5 2D array filled with values of your choice (1–9). Without using any diagonal-specific shortcut, find and print the sum of the main diagonal (top-left to bottom-right) and the anti-diagonal (top-right to bottom-left).

```
Expected output:
Grid:
3 1 4 1 5
9 2 6 5 3
5 8 9 7 9
3 2 3 8 4
6 2 6 4 3
Main diagonal sum  : 25
Anti diagonal sum  : 28
```

---

## Chapter 9 — Exponents & Math Functions
*"When arithmetic alone is not enough."*

**Q28.** Write your own power function `myPow(long long base, int exp)` without using `pow()`. Handle negative exponents by returning 0 (integer domain only). Test it with at least 5 cases including edge cases.

```
Expected output:
myPow(2, 10)   = 1024
myPow(-3, 3)   = -27
myPow(5, 0)    = 1
myPow(7, 1)    = 7
myPow(2, -1)   = 0
```

**Q29.** Ask the user for a number `n`. Print a table of `n`, `n²`, `n³`, and the integer square root of `n` (floor) for all values from 1 to `n`. Right-align all columns.

```
Expected output:
n    n^2    n^3   sqrt(n)
1      1      1        1
2      4      8        1
3      9     27        1
4     16     64        2
5     25    125        2
```

**Q30.** Compute compound interest. Ask for principal `P`, annual rate `R` (as a percentage), number of times compounded per year `n`, and years `t`. Use the formula `A = P * (1 + R/100n)^(n*t)` using your own `myPow` function for integer exponents.

```
Expected output:
Principal  : 10000
Rate (%)   : 8
Times/year : 4
Years      : 5
Final amount: 14859.47
```

---

## BOSS LEVEL — The Student Olympiad Tracker
*"Every concept. One program. No hints."*

> **Style:** LeetCode + Story-based + Plain practice — all three.

You are building an Olympiad result tracker. The program handles `n` students across 4 subjects. Your program must run through 7 phases. All scoring logic must live in **separate functions**.

### Constraints
- `2 ≤ n ≤ 6` students
- 4 subjects: Math, Physics, Chemistry, CS
- Scores: 0–100 per subject

---

### Phase 1 — Input
Ask the user for `n`. Then ask for each student's name and their 4 subject scores. Store names in a `string` array and scores in a 2D `int` array of size `n×4`.

---

### Phase 2 — Grade Assignment
Write a function `getGrade(int score)` that uses a `switch` or `if/else` chain to return a `char` grade:
- 90+ → `'A'`
- 80–89 → `'B'`
- 70–79 → `'C'`
- 60–69 → `'D'`
- below 60 → `'F'`

Apply it to every score in the 2D array and store results in a 2D `char` array of the same size.

---

### Phase 3 — Per-Student Report
Write a function `studentAverage(int scores[], int n)` that returns the average score of a student across all subjects. For each student, print their name, all 4 scores with grades, and their average.

```
Expected format:
Alice | Math:95(A)  Phy:88(B)  Chem:76(C)  CS:99(A)  | Avg: 89.50
```

---

### Phase 4 — Leaderboard
Sort students by their overall average in descending order using bubble sort on their averages array. Print the ranked leaderboard with rank number, name, and average.

```
Expected format:
Rank 1: Alice | 89.50
Rank 2: Bob   | 85.25
...
```

---

### Phase 5 — Subject Analysis
For each of the 4 subjects, find and print the highest score, lowest score, and subject average. Also print the name of the student who topped that subject.

```
Expected format:
Math    | High: 95 (Alice) | Low: 52 (Bob) | Avg: 74.33
Physics | High: 91 (Carol) | Low: 48 (Dan) | Avg: 71.00
...
```

---

### Phase 6 — Power Score & Medal String
Compute each student's Power Score using your custom `myPow` function:

```
Power = (number of A grades)^2 + (number of B grades)
```

Build and print a **medal string** for each student — concatenate their grade chars across all subjects (e.g. `"ABCA"`). Print a Power Score leaderboard.

```
Expected format:
Alice | Medals: ABCA | Power Score: 5
Bob   | Medals: BBAB | Power Score: 4
...
```

---

### Phase 7 — Oracle Interrogation
Print the overall topper's name. Then run a guessing game using a `while` loop: ask the user to guess this topper's average (rounded to nearest integer). Give `"Too low"` / `"Too high"` hints. Count attempts. When correct, print the final verdict:

```
"After [ATTEMPTS] attempt(s), the seeker discovered that [NAME]
reigned supreme with an average of [AVG], earning [MEDAL_STRING]
and a Power Score of [POWER] in the [N]-student olympiad."
```

---
