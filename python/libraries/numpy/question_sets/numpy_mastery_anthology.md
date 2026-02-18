# 🧠 NumPy Mastery — The Question Anthology

---

## 🔷 Chapter 1 — Introduction to NumPy
*"Before you run, you must import."*

**Q1.** You have a regular Python list `[10, 20, 30, 40, 50]`. Convert it into a NumPy array. Now print its **data type**, **shape**, and **number of dimensions**. What story does each of those three tell you about your array?

**Q2.** Create two arrays — one using a Python list, one using NumPy. Multiply each by 2. Time both using Python's `time` module. What did you discover, and *why* does it matter at scale?

---

## 🔷 Chapter 2 — Multidimensional Arrays
*"Flatland was never enough."*

**Q3.** Build a 3×3 NumPy array that represents a **tic-tac-toe board** — use `1` for X, `-1` for O, and `0` for empty. Now print only the **middle row** and the **last column**. Who's winning?

**Q4.** Create a 4×4 array filled with values 1–16. Now reshape it into a 2×8, then a 8×2. What stays the same across all three shapes, and what changes? Write your observation as a comment in code.

**Q5.** What happens when you try to reshape a 3×4 array into a 5×3? Run it, read the error, and explain it in your own words like you're teaching a friend.

---

## 🔷 Chapter 3 — Slicing
*"Don't take the whole cake. Take exactly what you need."*

**Q6.** Given this array:
```
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
```
Using only slicing — no loops — extract the **bottom-right 2×2 block**. Then extract **every other element from the second row**.

**Q7.** Slice the same 4×4 array to get **only the border elements** (top row, bottom row, first column, last column). Can you do it without repeating any element?

**Q8.** Reverse the entire array **row-wise** using slicing only. No `.flip()`, no loops. Just colons and negative steps. Think of it as rewinding a film reel.

---

## 🔷 Chapter 4 — Arithmetic
*"Numbers don't argue. They just calculate."*

**Q9.** You run a small shop. Daily sales for a week are `[1200, 850, 1100, 970, 1300, 760, 1450]`. Your costs each day are `[400, 300, 350, 290, 410, 250, 500]`. Using NumPy arithmetic, find your **daily profit**, **total weekly profit**, and the **day you profited most**.

**Q10.** Create two 3×3 arrays — one with values 1–9, one with values 9–1 (descending). Add them, subtract them, multiply them element-wise. What pattern do you notice in the sum result? Is it always the same number? Why?

**Q11.** Compute the **square root of every even number** from 2 to 20 using NumPy — in a single line. No loops allowed. Welcome to vectorized thinking.

---

## 🔷 Chapter 5 — Broadcasting
*"Not all arrays are born equal — but NumPy makes it work anyway."*

**Q12.** You have a 3×3 grid of temperatures in Celsius:
```
[[22, 25, 19],
 [30, 28, 24],
 [17, 21, 26]]
```
Add `[1, 2, 3]` to it using broadcasting. What happened to each column? Why didn't NumPy complain?

**Q13.** Try to add a `(3,)` array to a `(3,3)` array — it works. Now try to add a `(2,)` array to a `(3,3)` array — it breaks. Explain *why* the rules allow one but not the other. Draw it out if it helps.

**Q14.** You have 5 students' scores across 3 subjects in a `(5,3)` array. Each subject has a different bonus: `[5, 10, 15]`. Add the bonus to every student's score using broadcasting. Now who topped each subject?

---

## 🔷 Chapter 6 — Aggregate Functions
*"One number to rule them all."*

**Q15.** Given a 5×4 array of random integers between 1 and 100 (use `np.random.randint`), find:
- The **maximum of each row**
- The **minimum of each column**
- The **overall mean**
- The **sum along axis 0**

Explain what `axis=0` vs `axis=1` means — in your own words, not the docs.

**Q16.** You have monthly rainfall data (in mm) for 3 cities over 12 months — shape `(3, 12)`. Find the **wettest month** for each city and the **driest city overall**. Use `argmax`, `min`, and `sum`.

**Q17.** What's the difference between `np.mean()` and `np.median()`? Create a dataset where they give **very different** results and explain why. Hint: think about outliers.

---

## 🔷 Chapter 7 — Filtering
*"Not every element deserves to stay."*

**Q18.** Create an array of 20 random integers between 1 and 50. Filter out all **numbers divisible by 3 or 5**. How many survived? What percentage of the array did they represent?

**Q19.** You're a teacher. Scores are `[55, 82, 91, 47, 63, 78, 88, 34, 95, 60]`. Using boolean filtering:
- Find all students who **passed** (≥ 60)
- Find all students who scored between **70 and 90**
- Replace all **failing scores** with exactly 60 (a mercy pass 😅)

**Q20.** Create a 4×4 array. Filter all elements **greater than the mean** of the entire array. What does the result look like — is it still 2D? Why or why not?

---

## 🔷 Chapter 8 — Random Numbers
*"Controlled chaos. NumPy's specialty."*

**Q21.** Simulate rolling **two dice 1000 times** using `np.random.randint`. Count how many times the **sum equals 7**. What probability did you get? How close is it to the mathematical probability of 6/36?

**Q22.** Generate a `(5,5)` array of random floats between 0 and 1. Now **normalize** it so all values fall between 0 and 1 relative to the array's own min and max. Formula: `(x - min) / (max - min)`. This is a skill used in machine learning every single day.

**Q23.** Use `np.random.seed(42)` before generating a random array. Run it twice. What do you notice? Now remove the seed and run again. What changed — and why does this matter in **reproducible research and AI experiments**?

---

## 🏆 The Boss Level — Mixed Challenge
*"Everything. At once. No hints."*

**Q24.** You're a data analyst at a company. Employee salaries across 4 departments and 6 months are stored in a `(4, 6)` array. Use NumPy to:
- Find the **highest-paid department** on average
- Find **months where any department exceeded 80,000**
- Give every department a **10% raise** using arithmetic
- Identify departments earning **below the company average**

Build the array yourself with `np.random.randint`. Make it feel real.

---

*"Every question above is a door. Walk through enough of them, and you won't just know NumPy — you'll think in arrays."* 🚀
