# 📊 Matplotlib Practice Questions

> A progressive question set — from "Hello, Plot" to "Why does my figure look like modern art (unintentionally)."  
> Each level builds on the last. Don't skip. Don't peek at solutions. Struggle is the curriculum.

---

## 🟢 Level 1 — Foundation (Basics & Core Plots)

**Q1. The Classic Line**  
Plot `y = x²` for `x` in the range `[-10, 10]` with 200 evenly spaced points.  
- Label the axes `x` and `y = x²`  
- Add a title: `"Parabola"`  
- Make the line red and dashed  

---

**Q2. Bar Chart — Frequency Table**  
Given the data:
```python
subjects = ["Math", "Physics", "Chemistry", "CS", "English"]
scores   = [92, 88, 79, 95, 74]
```
- Plot a vertical bar chart  
- Color each bar a different color  
- Add value labels on top of each bar  

---

**Q3. Scatter Plot — Random Data**  
Generate 100 random `(x, y)` points using `numpy`.  
- Color the points by their distance from the origin (use a colormap like `viridis`)  
- Add a colorbar  
- Title it `"Distance from Origin"`  

---

**Q4. Histogram — Normal Distribution**  
Generate 1000 samples from a normal distribution (`mean=0`, `std=1`).  
- Plot a histogram with 30 bins  
- Overlay the theoretical PDF curve on top  
- Use `alpha=0.7` for the histogram bars  

---

**Q5. Pie Chart**  
Given:
```python
languages = ["Python", "C++", "Java", "Rust", "Go"]
usage     = [40, 25, 20, 10, 5]
```
- Plot a pie chart  
- Explode the `"Python"` slice by 0.1  
- Show percentages and labels  
- Use a clean pastel colormap  

---

## 🟡 Level 2 — Customization & Styling

**Q6. Multiple Lines on One Plot**  
Plot `sin(x)`, `cos(x)`, and `tan(x)` on the same axes for `x ∈ [0, 2π]`.  
- Clip `tan(x)` to `[-5, 5]` to avoid spikes  
- Add a legend  
- Use different linestyles for each  

---

**Q7. Axis Formatting**  
Plot `y = e^x` for `x ∈ [0, 5]`.  
- Set the y-axis to **log scale**  
- Add a grid with `linestyle='--'` and `alpha=0.5`  
- Format the y-axis ticks to show values like `1e0`, `1e1`, etc.  

---

**Q8. Annotations**  
Plot `y = sin(x)` for `x ∈ [0, 4π]`.  
- Find the maximum point and annotate it with an arrow and the text `"Peak"`  
- Find the minimum point and annotate it with `"Trough"`  
- Use `plt.annotate()` with `arrowprops`  

---

**Q9. Styling with Themes**  
Reproduce Q1 (the parabola), but this time:  
- Use `plt.style.use('ggplot')`  
- Then try `'dark_background'`  
- Then try `'seaborn-v0_8-whitegrid'`  
- Compare how the same data looks across all three. Which is clearest?  

*(No single right answer — the point is to develop an eye for visualization.)*

---

**Q10. Twin Axes**  
Given monthly temperature (°C) and rainfall (mm):
```python
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
temp   = [18, 20, 24, 28, 32, 35, 34, 33, 30, 26, 22, 19]
rain   = [5, 10, 20, 40, 80, 120, 150, 140, 90, 50, 20, 8]
```
- Plot `temp` as a line on the left y-axis (°C)  
- Plot `rain` as bars on the right y-axis (mm)  
- Use `ax.twinx()` to share the x-axis  

---

## 🟠 Level 3 — Subplots & Layout

**Q11. 2×2 Subplot Grid**  
In a single figure with a `2×2` grid, plot:  
- (0,0): Line plot of `sin(x)`  
- (0,1): Bar chart of 5 random values  
- (1,0): Scatter plot of 50 random points  
- (1,1): Histogram of 500 normal samples  

Add a `suptitle` to the figure: `"Four Plots, One Figure, Zero Regrets"`

---

**Q12. GridSpec Layout**  
Use `matplotlib.gridspec.GridSpec` to create this layout:
```
[ Wide plot spanning full top row ]
[ Left plot ] [ Right plot ]
```
- Top: Line plot of `cos(x)`  
- Bottom-left: Scatter plot  
- Bottom-right: Bar chart  

---

**Q13. Shared Axes**  
Plot 3 subplots stacked vertically with a **shared x-axis**:  
- Row 1: `sin(x)`  
- Row 2: `cos(x)`  
- Row 3: `sin(x) * cos(x)`  
- Use `plt.subplots(3, 1, sharex=True)`  
- Only show x-axis tick labels on the bottom subplot  

---

## 🔵 Level 4 — Statistical & Scientific Plots

**Q14. Box Plot**  
Generate 4 datasets, each with 100 samples:
```python
import numpy as np
data = [np.random.normal(loc, 1, 100) for loc in [0, 1, 2, 3]]
```
- Plot a side-by-side box plot  
- Label groups as `["A", "B", "C", "D"]`  
- Color each box differently using `patch_artist=True`  

---

**Q15. Heatmap from Scratch**  
Create a 10×10 matrix where `M[i][j] = sin(i) * cos(j)`.  
- Display it using `plt.imshow()` with the `RdBu` colormap  
- Add a colorbar  
- Show row and column indices as tick labels  

---

**Q16. Error Bars**  
Simulate an experiment: 5 trials, each with a mean and standard deviation:
```python
means = [3.2, 4.5, 2.8, 5.1, 3.9]
stds  = [0.3, 0.5, 0.4, 0.6, 0.2]
```
- Plot the means as a bar chart with error bars  
- Use `capsize=5`  
- Label x-axis as `"Trial"`, y-axis as `"Value"`  

---

**Q17. Stacked Bar Chart**  
Given:
```python
categories = ["Q1", "Q2", "Q3", "Q4"]
product_A  = [20, 35, 30, 25]
product_B  = [15, 25, 20, 30]
product_C  = [10, 15, 25, 20]
```
- Create a stacked bar chart  
- Add a legend for each product  
- Add value labels in the center of each stack segment  

---

**Q18. Contour Plot**  
Define `z = sin(√(x² + y²))` over a grid `x, y ∈ [-5, 5]`.  
- Plot both `plt.contour()` (lines only) and `plt.contourf()` (filled) side by side  
- Add contour labels using `plt.clabel()`  
- Use the `plasma` colormap  

---

## 🔴 Level 5 — Advanced

**Q19. Animated Line Plot**  
Use `matplotlib.animation.FuncAnimation` to animate `y = sin(x + t)` as `t` goes from `0` to `2π`.  
- The wave should scroll smoothly  
- Save as a `.gif` using `PillowWriter`  

---

**Q20. Custom Colormap**  
Create a custom colormap that transitions:  
`black → deep blue → cyan → white`  
- Use `LinearSegmentedColormap.from_list()`  
- Apply it to a heatmap of `z = x² - y²` over `[-3, 3]`  

---

**Q21. Broken Axis**  
Plot a dataset that has values clustered near `0–10` and a single outlier at `1000`.  
- Use `brokenaxes` (or simulate the effect with `GridSpec` + hidden spines)  
- The break should be clearly marked with diagonal tick marks  

---

**Q22. Figure as a Dashboard**  
Build a single figure that mimics a minimal analytics dashboard:  
- Title bar with text: `"Monthly Analytics — 2025"`  
- Top half: Line chart of monthly active users  
- Bottom-left: Pie chart of traffic sources  
- Bottom-right: Bar chart of revenue by region  
- Use `tight_layout()` and a dark theme  
- No `plt.show()` junk — save directly as `dashboard.png` at 300 DPI  

---

**Q23. Polar Plot**  
Plot a rose curve: `r = cos(4θ)` for `θ ∈ [0, 2π]` using a **polar projection**.  
- Fill the curve with a semi-transparent color  
- Remove the radial tick labels  
- Title: `"Rose Curve: r = cos(4θ)"`  

---

**Q24. Plot from a CSV (Real Data)**  
Download any dataset from [Our World in Data](https://ourworldindata.org/) or use a built-in `seaborn` dataset.  
- Load it with `pandas`  
- Choose 2–3 meaningful columns  
- Plot something **insightful** — not just a scatter plot of everything  
- Add a text box inside the plot with a key insight (use `ax.text()` with `bbox`)  

---

**Q25. Reproduce a Famous Plot**  
Reproduce (approximately) one of the following:  
- Florence Nightingale's Rose Diagram  
- Minard's Napoleon March (simplified version — just the troop count over geography)  
- Anscombe's Quartet (4 datasets, same statistics, different shapes)  

*This is the final boss. Flex your matplotlib muscles.*
