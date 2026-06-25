# 🍽️ Restaurant Data Analysis — Cognifyz Technologies Internship

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-9cf)
![Internship](https://img.shields.io/badge/Cognifyz-Data%20Analysis%20Intern-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

> **Internship:** Data Analysis Intern @ [Cognifyz Technologies](https://www.cognifyz.com)  
> **Intern:** Het Ladani  
> **Levels Completed:** Level 1 (Tasks 1–4) · Level 2 (Tasks 1–4)

---

## 📌 About This Project

This repository contains all the data analysis work completed during my **1-month Data Analysis Internship at Cognifyz Technologies**. The project involves **Exploratory Data Analysis (EDA)** on a restaurant dataset, covering cuisine trends, city-level insights, pricing, delivery, ratings, geographic distribution, and restaurant chains — using Python and its core data analysis libraries.

---

## 📂 Repository Structure

```
Cognifyz_Internship_Project/
│
├── 📁 source_code/         ← All Python scripts (one per task)
│   ├── Level1_Task1_TopCuisines.py
│   ├── Level1_Task2_CityAnalysis.py
│   ├── Level1_Task3_PriceRangeDistribution.py
│   ├── Level1_Task4_OnlineDelivery.py
│   ├── Level2_Task1_RestaurantRatings.py
│   ├── Level2_Task2_CuisineCombination.py
│   ├── Level2_Task3_GeographicAnalysis.py
│   └── Level2_Task4_RestaurantChains.py
│
└── 📁 outputs/             ← All output charts/visualizations (one per task)
    ├── Level1_Task1_TopCuisines.png
    ├── Level1_Task2_CityAnalysis.png
    ├── Level1_Task3_PriceRangeDistribution.png
    ├── Level1_Task4_OnlineDelivery.png
    ├── Level2_Task1_RestaurantRatings.png
    ├── Level2_Task2_CuisineCombination.png
    ├── Level2_Task3_GeographicAnalysis.png
    └── Level2_Task4_RestaurantChains.png
```

> 💡 **Quick navigation:**
> - Want to read the code? → [`source_code/`](./source_code)
> - Want to see the charts? → [`outputs/`](./outputs)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3** | Core programming language |
| **Pandas** | Data loading, cleaning, aggregation |
| **Matplotlib** | Charts and visualizations |
| **NumPy** | Numerical operations |

---

## 📊 Level 1 — Foundational Analysis

### ✅ Task 1 — Top Cuisines
**Code:** [`source_code/Level1_Task1_TopCuisines.py`](./source_code/Level1_Task1_TopCuisines.py) &nbsp;|&nbsp; **Output:** [`outputs/Level1_Task1_TopCuisines.png`](./outputs/Level1_Task1_TopCuisines.png)

- Identified the **top 3 most common cuisines** by exploding the multi-cuisine entries per restaurant
- Calculated the **percentage of total restaurants** serving each top cuisine

**Key Insight:** A small set of cuisines dominates the market, with a few types accounting for a large share of all restaurant offerings.

---

### ✅ Task 2 — City Analysis
**Code:** [`source_code/Level1_Task2_CityAnalysis.py`](./source_code/Level1_Task2_CityAnalysis.py) &nbsp;|&nbsp; **Output:** [`outputs/Level1_Task2_CityAnalysis.png`](./outputs/Level1_Task2_CityAnalysis.png)

- Found the **city with the highest number of restaurants**
- Calculated **average ratings per city** and ranked them
- Identified the **city with the highest average rating**

**Key Insight:** The most restaurant-dense city is not necessarily the highest-rated one — volume and quality don't always go hand in hand.

---

### ✅ Task 3 — Price Range Distribution
**Code:** [`source_code/Level1_Task3_PriceRangeDistribution.py`](./source_code/Level1_Task3_PriceRangeDistribution.py) &nbsp;|&nbsp; **Output:** [`outputs/Level1_Task3_PriceRangeDistribution.png`](./outputs/Level1_Task3_PriceRangeDistribution.png)

- Created a **bar chart** showing how restaurants are distributed across price range categories (1–4)
- Calculated the **percentage of restaurants** in each price range

**Key Insight:** Most restaurants are concentrated in the lower price ranges, reflecting a predominantly budget-friendly market.

---

### ✅ Task 4 — Online Delivery
**Code:** [`source_code/Level1_Task4_OnlineDelivery.py`](./source_code/Level1_Task4_OnlineDelivery.py) &nbsp;|&nbsp; **Output:** [`outputs/Level1_Task4_OnlineDelivery.png`](./outputs/Level1_Task4_OnlineDelivery.png)

- Calculated the **percentage of restaurants offering online delivery**
- Compared **average ratings** between restaurants with and without online delivery

**Key Insight:** Restaurants that offer online delivery show a noticeable difference in average ratings compared to those that don't.

---

## 📈 Level 2 — Deeper Analysis

### ✅ Task 1 — Restaurant Ratings
**Code:** [`source_code/Level2_Task1_RestaurantRatings.py`](./source_code/Level2_Task1_RestaurantRatings.py) &nbsp;|&nbsp; **Output:** [`outputs/Level2_Task1_RestaurantRatings.png`](./outputs/Level2_Task1_RestaurantRatings.png)

- Plotted a **histogram** of aggregate ratings to visualize the overall distribution
- Used `pd.cut()` to bin ratings and determine the **most common rating range**
- Calculated the **average number of votes** received per restaurant

**Key Insight:** Ratings cluster heavily around mid-to-high values, suggesting a generally positive dining experience across the dataset.

---

### ✅ Task 2 — Cuisine Combination
**Code:** [`source_code/Level2_Task2_CuisineCombination.py`](./source_code/Level2_Task2_CuisineCombination.py) &nbsp;|&nbsp; **Output:** [`outputs/Level2_Task2_CuisineCombination.png`](./outputs/Level2_Task2_CuisineCombination.png)

- Identified the **top 10 most common cuisine combinations** in the dataset
- Determined which **cuisine combos tend to attract higher average ratings**

**Key Insight:** Certain multi-cuisine pairings consistently outperform single-cuisine restaurants in ratings, suggesting customers respond positively to variety.

---

### ✅ Task 3 — Geographic Analysis
**Code:** [`source_code/Level2_Task3_GeographicAnalysis.py`](./source_code/Level2_Task3_GeographicAnalysis.py) &nbsp;|&nbsp; **Output:** [`outputs/Level2_Task3_GeographicAnalysis.png`](./outputs/Level2_Task3_GeographicAnalysis.png)

- Plotted **restaurant locations on a scatter map** using Longitude and Latitude coordinates
- Identified **geographic clusters** by grouping restaurants that share the same coordinates

**Key Insight:** Restaurants are heavily concentrated in specific geographic zones, revealing clear urban density patterns and market saturation in certain areas.

---

### ✅ Task 4 — Restaurant Chains
**Code:** [`source_code/Level2_Task4_RestaurantChains.py`](./source_code/Level2_Task4_RestaurantChains.py) &nbsp;|&nbsp; **Output:** [`outputs/Level2_Task4_RestaurantChains.png`](./outputs/Level2_Task4_RestaurantChains.png)

- Detected **restaurant chains** (names appearing more than once in the dataset)
- Analyzed each chain's **average rating** and **total vote count** as a measure of popularity

**Key Insight:** Well-known chains accumulate significantly more votes, confirming stronger brand recognition and customer engagement compared to standalone restaurants.

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/ladanihet2410/Cognifyz_Internship_Project.git
   cd Cognifyz_Internship_Project
   ```

2. **Install required libraries**
   ```bash
   pip install pandas matplotlib
   ```

3. **Update the dataset path** inside any script in `source_code/`
   ```python
   # Replace this line at the top of each .py file:
   file_path = "path/to/your/Dataset.csv"
   ```

4. **Run any script**
   ```bash
   python source_code/Level1_Task1_TopCuisines.py
   ```

> 📝 The dataset used is a restaurant dataset provided by Cognifyz Technologies as part of the internship program. It is not included in this repository.

---

## 📷 Output Previews

All chart outputs are stored in the [`outputs/`](./outputs) folder. Here's a summary of what each one shows:

| Task | Chart File | What it shows |
|------|-----------|---------------|
| L1 – Top Cuisines | `Level1_Task1_TopCuisines.png` | Bar chart of top 3 cuisines & their share |
| L1 – City Analysis | `Level1_Task2_CityAnalysis.png` | Avg ratings per city, ranked |
| L1 – Price Range | `Level1_Task3_PriceRangeDistribution.png` | Distribution across price categories |
| L1 – Online Delivery | `Level1_Task4_OnlineDelivery.png` | Rating comparison: delivery vs no delivery |
| L2 – Rating Distribution | `Level2_Task1_RestaurantRatings.png` | Histogram of aggregate ratings |
| L2 – Cuisine Combos | `Level2_Task2_CuisineCombination.png` | Top cuisine pairings & avg ratings |
| L2 – Geographic Map | `Level2_Task3_GeographicAnalysis.png` | Scatter map of restaurant locations |
| L2 – Restaurant Chains | `Level2_Task4_RestaurantChains.png` | Chain popularity by votes & rating |

---

## 🤝 Acknowledgements

- **[Cognifyz Technologies](https://www.cognifyz.com)** for the internship opportunity, dataset, and task guidelines.

---

## 📬 Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Het%20Ladani-blue?logo=linkedin)](https://linkedin.com/in/het-ladani-5001bb29a/)
[![GitHub](https://img.shields.io/badge/GitHub-ladanihet2410-black?logo=github)](https://github.com/ladanihet2410)
[![Email](https://img.shields.io/badge/Email-ladanihet2410%40gmail.com-red?logo=gmail)](mailto:ladanihet2410@gmail.com)

---

*Completed as part of the Cognifyz Technologies Data Analysis Internship Program — 2026.*
