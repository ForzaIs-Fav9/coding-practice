# ⚔️ The Python Chronicles — A Questbook for the Brave

> *"Every master was once a beginner who refused to quit.  
> Every line of code — a brushstroke on the canvas of tomorrow."*

---

## 📜 Preface

This is not just a problem set. This is a **rite of passage**.  
Each problem is a door. Each solution — a key you forge yourself.  
Progress through four tiers, and face the **Boss Level** when you're ready.

**Languages allowed:** Python 3.x only  
**Judgment:** Standard I/O (stdin/stdout)  
**Format:** Inspired by Codeforces — Input → Output → Glory

---

<br>

---

# 🟤 TIER I — BRONZE: Where the Cursor Blinks First

> *"In the beginning, there was nothing —  
> and then you typed `print`, and the world began."*

---

## Problem 1 — Stairway to Stars

| | |
|---|---|
| **Difficulty** | ⭐ `800` |
| **Time Limit** | 1 second |
| **Memory Limit** | 256 MB |
| **Topics** | `Output` · `Drawing a Shape` · `Loops` |

### Problem Statement

A young astronomer is building a **staircase to the sky**, one row of stars at a time.  
She needs your help to construct a **right-angled triangle** of `*` characters with exactly `n` rows, where the `i`-th row contains exactly `i` stars.

Can you light up her path?

### Input

A single integer `n` — the number of rows in the staircase.

$$1 \leq n \leq 50$$

### Output

Print `n` lines. The `i`-th line (1-indexed) must contain exactly `i` asterisk (`*`) characters.

### Examples

**Input:**
```
5
```
**Output:**
```
*
**
***
****
*****
```

---

**Input:**
```
1
```
**Output:**
```
*
```

### Notes

Think of building the staircase **one step at a time**. A simple loop from `1` to `n` is your best friend here. Notice how the number of stars on each row matches the row number.

---
<br>

## Problem 2 — The Name Echo

| | |
|---|---|
| **Difficulty** | ⭐ `850` |
| **Time Limit** | 1 second |
| **Memory Limit** | 256 MB |
| **Topics** | `Variables` · `Strings` · `Data Types` |

### Problem Statement

> *"A name is the first poem a parent writes."*

The Oracle has a guest. She knows their **name** and their **birth year**.  
The Oracle always speaks in the year **2025**.

Given a person's full name and birth year, the Oracle must greet them with:
- Their name
- Their current age (as of 2025)
- The number of characters in their name *(spaces included)*

Format exactly as shown in the example.

### Input

Two lines:
- Line 1: A non-empty string `name` (may contain spaces)
- Line 2: An integer `birth_year`

$$1900 \leq \text{birth\_year} \leq 2024$$

### Output

A single formatted line:

```
Hello, [name]! You are [age] years old. Your name has [len] characters.
```

### Examples

**Input:**
```
Harshith Vankela
2009
```
**Output:**
```
Hello, Harshith Vankela! You are 16 years old. Your name has 16 characters.
```

---

**Input:**
```
Ada Lovelace
1815
```
**Output:**
```
Hello, Ada Lovelace! You are 210 years old. Your name has 12 characters.
```

### Notes

Use string formatting (f-strings are your best friend). `len()` counts every character including spaces. The age is simply `2025 - birth_year`.

---
<br>

## Problem 3 — The Number Alchemist

| | |
|---|---|
| **Difficulty** | ⭐ `900` |
| **Time Limit** | 1 second |
| **Memory Limit** | 256 MB |
| **Topics** | `Working With Numbers` · `Data Types` |

### Problem Statement

> *"Numbers are not cold things. They breathe, they multiply, they leave remainders —  
> just like us."*

The Alchemist deals in six **fundamental transformations** of two numbers `a` and `b`.  
Given `a` and `b`, output the following six values on separate lines:

1. `a + b` — the **Sum**
2. `a - b` — the **Difference**
3. `a * b` — the **Product**
4. `a // b` — the **Integer Quotient**
5. `a % b` — the **Remainder**
6. `a ** b` — the **Power**

### Input

Two integers `a` and `b` on a single line, space-separated.

$$1 \leq b \leq a \leq 100$$

### Output

Six integers, each on a separate line, in the order above.

### Examples

**Input:**
```
7 3
```
**Output:**
```
10
4
21
2
1
343
```

---

**Input:**
```
10 2
```
**Output:**
```
12
8
20
5
0
100
```

---
<br>

---

# 🥈 TIER II — SILVER: The Awakening

> *"You have learned to speak.  
> Now learn to ask questions,  
> and to listen to the answers the machine gives back."*

---

## Problem 4 — The String Sculptor

| | |
|---|---|
| **Difficulty** | ⭐⭐ `1000` |
| **Time Limit** | 1 second |
| **Memory Limit** | 256 MB |
| **Topics** | `Strings` · `Data Types` · `If Statements` |

### Problem Statement

A string arrives at your workshop. You are a sculptor. You must reveal its **six hidden faces**:

1. Its **length**
2. Itself in **UPPERCASE**
3. Itself in **lowercase**
4. Itself **reversed**
5. The **count of vowels** (`a, e, i, o, u` — case-insensitive)
6. Whether it is a **palindrome** (`True` or `False`)

### Input

A single string `s` — no spaces, only alphabetic characters.

$$1 \leq |s| \leq 100$$

### Output

Six lines corresponding to the six transformations.

### Examples

**Input:**
```
racecar
```
**Output:**
```
7
RACECAR
racecar
racecar
3
True
```

---

**Input:**
```
Harshith
```
**Output:**
```
8
HARSHITH
harshith
htihsraH
2
False
```

### Notes

A **palindrome** reads the same forward and backward (case-insensitive check recommended). Use string slicing `s[::-1]` for reversal. Count vowels using a loop or `sum()`.

---
<br>

## Problem 5 — The Mad Poet

| | |
|---|---|
| **Difficulty** | ⭐⭐ `1050` |
| **Time Limit** | 1 second |
| **Memory Limit** | 256 MB |
| **Topics** | `User Input` · `Variables` · `Strings` · `Mad Libs` |

### Problem Statement

> *"Every great story is just a template waiting for the right words."*

The Mad Poet has a story template — but it's missing six crucial words.  
Take the following inputs and fill in the blanks:

```
The [ADJECTIVE] [NOUN] decided to [VERB] all the way to [PLACE].
It took [NUMBER] whole hours, and everyone in the crowd felt utterly [EMOTION].
The legend would be told for [NUMBER] * 10 years to come.
```

Note: The last line's number is computed — it equals `NUMBER × 10`.

### Input

Six lines in this order:
1. `noun`
2. `verb`
3. `adjective`
4. `place`
5. `number` (integer)
6. `emotion`

### Output

The completed story — exactly 3 lines.

### Examples

**Input:**
```
robot
sprint
ancient
Moon
42
confused
```
**Output:**
```
The ancient robot decided to sprint all the way to Moon.
It took 42 whole hours, and everyone in the crowd felt utterly confused.
The legend would be told for 420 years to come.
```

---
<br>

## Problem 6 — The Arithmetic Oracle

| | |
|---|---|
| **Difficulty** | ⭐⭐ `1100` |
| **Time Limit** | 1 second |
| **Memory Limit** | 256 MB |
| **Topics** | `Calculator` · `User Input` · `If Statements` · `Data Types` |

### Problem Statement

> *"Division by zero: the only sin mathematics never forgives."*

Build a **calculator** that accepts two numbers and one of seven operators.  
The supported operators are: `+`, `-`, `*`, `/`, `//`, `%`, `**`

- For `/`, output a **float** rounded to 2 decimal places.
- For `//`, `%`, `**` and the others — output an integer where result is whole; otherwise 2dp float.
- If the operator is `/`, `//`, or `%` and the second number is `0`, output `Error: Division by zero`.

### Input

Three lines:
- Line 1: First number `a` (float)
- Line 2: Operator (one of the 7 above)
- Line 3: Second number `b` (float)

### Output

The result, or an error message.

### Examples

**Input:**
```
15
/
4
```
**Output:**
```
3.75
```

---

**Input:**
```
9
/
0
```
**Output:**
```
Error: Division by zero
```

---

**Input:**
```
2
**
10
```
**Output:**
```
1024
```

---
<br>

---

# 🥇 TIER III — GOLD: Where Logic Blooms

> *"To control the flow of a program  
> is to conduct an orchestra of ones and zeros —  
> and you are the maestro."*

---

## Problem 7 — The Verdict Machine

| | |
|---|---|
| **Difficulty** | ⭐⭐⭐ `1300` |
| **Time Limit** | 1 second |
| **Memory Limit** | 256 MB |
| **Topics** | `If Statements` · `User Input` · `Functions` · `Loops` |

### Problem Statement

A student sits across from the Verdict Machine, trembling with five subject scores.  
The Machine must compute and declare, without mercy or favor:

1. **Average** — rounded to 2 decimal places
2. **Grade** — based on average: `A` (≥90), `B` (≥80), `C` (≥70), `D` (≥60), `F` (<60)
3. **Status** — `Passed` if ALL scores ≥ 40, else `Failed`
4. **Rank** — `Distinction` (avg ≥ 90), `Merit` (avg ≥ 75), `Pass` (avg ≥ 40), `Fail` otherwise

### Input

Five integers on separate lines, each between `0` and `100`.

### Output

Four lines: average, grade, status, rank.

### Examples

**Input:**
```
88
92
76
85
90
```
**Output:**
```
86.20
B
Passed
Merit
```

---

**Input:**
```
95
98
91
93
97
```
**Output:**
```
94.80
A
Passed
Distinction
```

---

**Input:**
```
35
72
68
80
55
```
**Output:**
```
62.00
D
Failed
Fail
```

### Notes

Be careful: **Status** depends on whether any single score is below 40 — even if the average looks fine. Logic first, then math.

---
<br>

## Problem 8 — The Season Sage

| | |
|---|---|
| **Difficulty** | ⭐⭐⭐ `1350` |
| **Time Limit** | 1 second |
| **Memory Limit** | 256 MB |
| **Topics** | `Switch/Match Statements` · `If Statements` |

### Problem Statement

> *"The world turns, the seasons change —  
> and the Sage knows exactly where in the circle you stand."*

Given a **month number** (1–12), the Season Sage must reveal:

1. The **month name** (e.g., `July`)
2. The **season** (Northern Hemisphere):
   - `Winter`: December, January, February
   - `Spring`: March, April, May
   - `Summer`: June, July, August
   - `Autumn`: September, October, November
3. The **number of days** in that month *(assume non-leap year)*

### Input

A single integer `m` where `1 ≤ m ≤ 12`.

### Output

Three lines: month name, season, days in month.

### Examples

**Input:**
```
7
```
**Output:**
```
July
Summer
31
```

---

**Input:**
```
2
```
**Output:**
```
February
Winter
28
```

### Notes

Use Python's `match` statement (Python 3.10+) — this is exactly the problem it was born for. February always has 28 days here (non-leap year assumption).

---
<br>

## Problem 9 — The List Architect

| | |
|---|---|
| **Difficulty** | ⭐⭐⭐ `1450` |
| **Time Limit** | 1 second |
| **Memory Limit** | 256 MB |
| **Topics** | `Arrays/Lists` · `For Loops` · `Functions` |

### Problem Statement

> *"A list unsorted is a library unread —  
> potential, paralyzed."*

Given a list of `n` integers, reveal its full structure:

1. The list **sorted ascending**
2. The list **sorted descending**
3. **Maximum** and **minimum** values (space-separated)
4. **Sum** and **average** (average rounded to 2 decimal places, space-separated)
5. The **second largest** unique element
6. All elements at **even indices** (0-indexed) as a list

### Input

- Line 1: integer `n`
- Line 2: `n` space-separated integers

$$2 \leq n \leq 1000 \quad \text{and} \quad -10^6 \leq \text{each element} \leq 10^6$$

### Output

Six lines as described.

### Examples

**Input:**
```
6
4 1 7 2 9 3
```
**Output:**
```
[1, 2, 3, 4, 7, 9]
[9, 7, 4, 3, 2, 1]
9 1
26 4.33
7
[4, 7, 9]
```

### Notes

For the **second largest**, consider only unique values. Even-indexed elements: index 0, 2, 4, ...

---
<br>

## Problem 10 — The Function Forge

| | |
|---|---|
| **Difficulty** | ⭐⭐⭐ `1500` |
| **Time Limit** | 2 seconds |
| **Memory Limit** | 256 MB |
| **Topics** | `Functions` · `Return Statement` · `If Statements` · `While Loops` |

### Problem Statement

> *"A function is a promise —  
> give me input, I will return truth."*

Implement the following **four mathematical functions**:

| Function | Description |
|----------|-------------|
| `is_prime(n)` | Returns `True` if `n` is prime, `False` otherwise |
| `fibonacci(n)` | Returns the `n`-th Fibonacci number (0-indexed: F(0)=0, F(1)=1) |
| `factorial(n)` | Returns `n!` |
| `gcd(a, b)` | Returns the Greatest Common Divisor of `a` and `b` |

Given `q` queries, answer each.

### Input

- Line 1: integer `q`
- Next `q` lines: each starts with a function name followed by 1 or 2 arguments

```
is_prime <n>
fibonacci <n>
factorial <n>
gcd <a> <b>
```

$$1 \leq q \leq 50 \quad|\quad 0 \leq n \leq 20 \quad|\quad 1 \leq a, b \leq 10^4$$

### Output

`q` lines — one result per query.

### Examples

**Input:**
```
5
is_prime 17
fibonacci 10
factorial 6
gcd 48 18
is_prime 4
```
**Output:**
```
True
55
720
6
False
```

### Notes

Do **not** import any math modules — implement everything from scratch. Use loops, not recursion (recursion is for Tier IV).

---
<br>

---

# 💎 TIER IV — PLATINUM: The Crucible

> *"You have learned the alphabet of the machine.  
> Now write poetry in its language —  
> loops within loops, arrays within arrays,  
> logic folded into logic like an origami of pure thought."*

---

## Problem 11 — The Loop Labyrinth

| | |
|---|---|
| **Difficulty** | ⭐⭐⭐⭐ `1650` |
| **Time Limit** | 2 seconds |
| **Memory Limit** | 256 MB |
| **Topics** | `While Loops` · `For Loops` · `If Statements` · `Functions` |

### Problem Statement

You enter the **Loop Labyrinth**. Three chambers await.

**Chamber 1:** Print all **prime numbers up to `n`**, space-separated.

**Chamber 2:** Print **FizzBuzz** for 1 to `n`:
- Print `FizzBuzz` if divisible by both 3 and 5
- Print `Fizz` if divisible by 3 only
- Print `Buzz` if divisible by 5 only
- Otherwise, print the number

**Chamber 3:** Compute `n²` and print the **sum of its digits**.

### Input

A single integer `n`.

$$2 \leq n \leq 100$$

### Output

Three lines (Chamber 1 result, Chamber 2 result, Chamber 3 result).

### Examples

**Input:**
```
20
```
**Output:**
```
2 3 5 7 11 13 17 19
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz
4
```

*(Note: 20² = 400, digit sum = 4 + 0 + 0 = 4)*

---
<br>

## Problem 12 — Power Without Mercy

| | |
|---|---|
| **Difficulty** | ⭐⭐⭐⭐ `1750` |
| **Time Limit** | 2 seconds |
| **Memory Limit** | 256 MB |
| **Topics** | `Exponent Function` · `For Loops` · `Functions` · `While Loops` |

### Problem Statement

> *"You want power? Then build it yourself, brick by brick —  
> no shortcuts, no `**`, no `pow()`."*

Three sub-problems, all using loops and functions — **no `**` operator or `pow()` allowed**:

**Part A:** Compute `a^b` using a loop.

**Part B:** Compute **compound interest**:
$$A = P \times \left(1 + \frac{r}{100}\right)^t$$
where `P` = principal, `r` = annual rate (%), `t` = time in years. Output rounded to 2 decimal places.

**Part C:** Find the **smallest power of 2** that is ≥ `n`.

### Input

Three lines:
- Line 1: `a b` (integers for Part A)
- Line 2: `P r t` (floats for Part B)
- Line 3: `n` (integer for Part C)

$$1 \leq a, b \leq 15 \quad|\quad 1 \leq P \leq 10^6 \quad|\quad 1 \leq r \leq 50 \quad|\quad 1 \leq t \leq 30 \quad|\quad 1 \leq n \leq 10^6$$

### Output

Three lines: result of A, result of B, result of C.

### Examples

**Input:**
```
3 5
1000 10 3
100
```
**Output:**
```
243
1331.00
128
```

### Notes

For Part C, start with `1` and keep doubling until you reach or exceed `n`. That's it. No logarithms needed.

---
<br>

## Problem 13 — The Grid Whisperer

| | |
|---|---|
| **Difficulty** | ⭐⭐⭐⭐ `1900` |
| **Time Limit** | 2 seconds |
| **Memory Limit** | 256 MB |
| **Topics** | `2D Arrays` · `Nested Loops` · `Functions` |

### Problem Statement

> *"The matrix does not lie.  
> Read its diagonals, transpose its truths,  
> and find the saddle points where tension rests."*

Given an `n × n` matrix, perform the following operations in order:

1. **Print the matrix** (space-separated rows)
2. **Print its transpose**
3. Print the **sum of the primary diagonal** (top-left to bottom-right)
4. Print the **sum of the secondary diagonal** (top-right to bottom-left)
5. Print the **index and values** of the row with the maximum sum (0-indexed)
6. Print all **saddle points**: an element is a saddle point if it is the **minimum in its row** AND the **maximum in its column**. Print each as `(row, col): value`. If none exist, print `None`.

Separate each section with `---`.

### Input

- Line 1: integer `n`
- Next `n` lines: `n` space-separated integers each

$$2 \leq n \leq 10$$

All values fit in a standard integer.

### Output

Six sections separated by `---`.

### Examples

**Input:**
```
3
1 2 3
4 5 6
7 8 9
```
**Output:**
```
1 2 3
4 5 6
7 8 9
---
1 4 7
2 5 8
3 6 9
---
15
---
15
---
Row 2: [7, 8, 9]
---
(2, 0): 7
```

### Notes

For the saddle point: element `M[i][j]` is a saddle point if `M[i][j] == min(row i)` AND `M[i][j] == max(column j)`. In the example, `7` is the min of row 2 `[7,8,9]` — **wait, no** — `7` is actually the minimum of row 2. And `7` is also the maximum of column 0 `[1,4,7]`. So it qualifies. Both diagonals in the 3×3 example sum to `1+5+9=15` and `3+5+7=15`.

---
<br>

## Problem 14 — Mind Reader

| | |
|---|---|
| **Difficulty** | ⭐⭐⭐⭐ `1950` |
| **Time Limit** | 2 seconds |
| **Memory Limit** | 256 MB |
| **Topics** | `Guessing Game` · `While Loops` · `If Statements` · `Functions` |

### Problem Statement

> *"The machine thinks of a number.  
> You ask. It answers. You guess again.  
> Until silence becomes certainty."*

Simulate a **number guessing game** where the secret number is computed as:

$$\text{secret} = ((\text{seed} \times 1103515245 + 12345) \% 2^{31}) \% \text{high} + \text{low}$$

This is a simple **linear congruential generator** — no `random` imports needed.

Given `seed`, `low`, `high`, and a sequence of guesses, simulate the game:
- For each guess, output `Too low!`, `Too high!`, or `Correct! Found in X guesses.`
- Stop processing guesses once `Correct!` is output.
- If all guesses are exhausted without finding it, output `Game over! The number was [secret].`

Also output the **minimum number of guesses** theoretically needed (using binary search strategy): `⌈log₂(high - low + 1)⌉`.

### Input

- Line 1: `seed low high` (integers)
- Line 2: `q` — number of guesses
- Next `q` lines: each is a guess (integer)

$$0 \leq \text{seed} \leq 10^9 \quad|\quad 1 \leq \text{low} \leq \text{high} \leq 10^6 \quad|\quad 1 \leq q \leq 30$$

### Output

Lines for each guess until correct/game over, then the theoretical minimum.

### Examples

**Input:**
```
42 1 100
5
50
25
37
43
38
```
*(Secret = (42×1103515245+12345) % 2147483648 % 100 + 1 = some number — compute to verify)*

**Output will vary based on secret.** For grading purposes, implement the formula and trust the output.

**Minimum guesses:** For range 1–100, `⌈log₂(100)⌉ = 7`.

```
Minimum guesses needed (binary search): 7
```

### Notes

The theoretical minimum is `math.ceil(math.log2(high - low + 1))` — but implement the ceiling yourself using a while loop: keep doubling from 1 until `2^k ≥ range_size`.

---
<br>

---

# 🔴 BOSS LEVEL — THE ARCHITECT'S TRIAL

> *"You have walked the Bronze path and the Silver road.  
> You have crossed the Gold threshold and survived the Platinum forge.  
> Now — you build something real.*
>
> *Not a solution. A system.*
>
> *Not a function. A world."*

---

## Problem 15 — The Student Codex

| | |
|---|---|
| **Difficulty** | ⭐⭐⭐⭐⭐ `2400` |
| **Time Limit** | 5 seconds |
| **Memory Limit** | 256 MB |
| **Topics** | `EVERYTHING` |

### Problem Statement

You are tasked with building a **Student Records Management System** — a command-line application that processes a series of commands and maintains a student database.

Each student has:
- A **name** (unique, single word)
- **5 subject scores** (integers, 0–100)

The system supports the following commands:

| Command | Description |
|---------|-------------|
| `ADD <name> <s1> <s2> <s3> <s4> <s5>` | Add student with 5 scores |
| `REPORT <name>` | Print average, grade, pass/fail status, rank |
| `LEADERBOARD` | Print all students sorted by average (descending) |
| `TOPN <n>` | Print top `n` students by average |
| `CLASSAVG` | Print average of all students' averages (2dp) |
| `GRADECOUNT` | Print count of students per grade (A/B/C/D/F) |
| `FINDGRADE <grade>` | List students who achieved the given grade |
| `PRIMES <name>` | List which of the student's scores are prime |
| `PATTERN <n>` | Print a diamond of `*` with middle width `2n-1` |
| `EXIT` | Terminate processing |

**Grade thresholds** (based on average): A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, F < 60  
**Rank:** Distinction (≥90), Merit (≥75), Pass (≥40), Fail (<40)  
**Pass condition:** ALL scores ≥ 40

If `ADD` is called with an existing name, **update** the student's scores.  
If any command references a non-existent student, print `Student not found.`

### Input

A series of commands (at most 200), one per line, terminated by `EXIT`.

### Output

Output corresponding to each command (except `ADD` and `EXIT` which produce no output).

### Example

**Input:**
```
ADD Alice 88 92 76 85 90
ADD Bob 55 60 48 70 65
ADD Carol 95 98 91 93 97
ADD Dave 35 72 68 80 55
REPORT Alice
LEADERBOARD
CLASSAVG
GRADECOUNT
PRIMES Alice
FINDGRADE B
PATTERN 3
TOPN 2
EXIT
```

**Output:**
```
Name: Alice | Average: 86.20 | Grade: B | Status: Passed | Rank: Merit
---
1. Carol  | Avg: 94.80 | Grade: A
2. Alice  | Avg: 86.20 | Grade: B
3. Bob    | Avg: 59.60 | Grade: F
4. Dave   | Avg: 62.00 | Grade: D
---
Class Average: 75.65
---
A: 1
B: 1
C: 0
D: 1
F: 1
---
Alice's prime scores: [none]
---
Students with grade B: Alice
---
  *
 ***
*****
 ***
  *
---
Top 2 Students:
1. Carol  | Avg: 94.80 | Grade: A
2. Alice  | Avg: 86.20 | Grade: B
```

### Notes

- Scores like 88, 92, 76, 85, 90 — none are prime. Note: `2` is the only even prime.
- The diamond for `PATTERN 3` has rows: 1, 3, 5, 3, 1 stars, centered.
- Bob's average: (55+60+48+70+65)/5 = 59.6 → Grade F (since <60... wait, 59.6 < 60, so F). Status: Passed (all ≥ 40). Rank: Pass.
- Dave's average: (35+72+68+80+55)/5 = 62.0 → Grade D. Status: Failed (35 < 40). Rank: Fail.
- This is your **capstone**. Write clean, modular code with functions. Use 2D arrays (list of lists) to store the student matrix. Use every construct you've learned.

---

### Grading Rubric (Self-Assessment)

| Criteria | Points |
|----------|--------|
| All basic commands work correctly | 40 |
| Edge cases handled (student not found, duplicate ADD) | 15 |
| Code uses functions with return statements | 15 |
| No repeated logic (DRY principle) | 10 |
| Diamond pattern is correct for all `n` | 10 |
| PRIMES correctly identifies prime scores | 10 |
| **Total** | **100** |

---

## 🏁 The Path You Have Walked

```
Bronze  → Variables, Strings, Numbers, Output
Silver  → User Input, Mad Libs, Calculator, String Ops
Gold    → If Statements, Switch/Match, Lists, Functions
Platinum → While/For Loops, Exponents, 2D Arrays, Nested Loops
Boss    → Everything. All at once. Like a real project.
```

> *"The journey of a thousand functions begins with a single `print`.*
>
> *You began. You struggled. You debugged.*
>
> *And somewhere between a syntax error and a working output,*
> *you became a programmer."*

---

*Built for the coding-practice repository. Push your solutions. Commit your growth.*  
*The only rule: no looking at solutions before you try.*

---

**Good luck, Architect. The cursor blinks and waits for you.** ⚡
