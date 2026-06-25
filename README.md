# 🍽️ Restaurant Data Analysis — Cognifyz Technologies Internship

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Internship](https://img.shields.io/badge/Cognifyz-Data%20Analysis%20Intern-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

> **Internship:** Data Analysis Intern @ [Cognifyz Technologies](https://www.cognifyz.com)  
> **Intern:** Het Ladani  
> **Levels Completed:** Level 1 (Tasks 1–4) · Level 2 (Tasks 1–4)

---

## 📌 About This Project

This repository contains all the data analysis work completed during my **1-month Data Analysis Internship at Cognifyz Technologies**. The project involves **Exploratory Data Analysis (EDA)** on a restaurant dataset, covering cuisine trends, city-level insights, pricing, delivery, ratings, geographic distribution, and restaurant chains.

The analysis is organized into **two levels** with **4 tasks each**, progressively covering deeper analytical questions using Python.

---

## 📁 Repository Structure

```
Cognifyz_Internship_Project/
│
├── Level1_Task1_TopCuisines.py          # Top 3 cuisines & their percentage share
├── Level1_Task1_TopCuisines.png         # Output visualization
│
├── Level1_Task2_CityAnalysis.py         # City with most restaurants & highest avg rating
├── Level1_Task2_CityAnalysis.png        # Output visualization
│
├── Level1_Task3_PriceRangeDistribution.py   # Price range bar chart & percentages
├── Level1_Task3_PriceRangeDistribution.png  # Output visualization
│
├── Level1_Task4_OnlineDelivery.py       # Online delivery % & rating comparison
├── Level1_Task4_OnlineDelivery.png      # Output visualization
│
├── Level2_Task1_RestaurantRatings.py    # Rating distribution & average votes
├── Level2_Task1_RestaurantRatings.png   # Output visualization
│
├── Level2_Task2_CuisineCombination.py   # Top cuisine combos & their avg ratings
├── Level2_Task2_CuisineCombination.png  # Output visualization
│
├── Level2_Task3_GeographicAnalysis.py   # Map of restaurant locations & clusters
├── Level2_Task3_GeographicAnalysis.png  # Output visualization
│
└── Level2_Task4_RestaurantChains.py     # Restaurant chains: ratings & popularity
    Level2_Task4_RestaurantChains.png    # Output visualization
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3** | Core programming language |
| **Pandas** | Data loading, cleaning, aggregation |
| **Matplotlib** | Charts and visualizations |
| **NumPy** | Numerical operations (via Pandas) |

---

## 📊 Level 1 — Foundational Analysis

### ✅ Task 1 — Top Cuisines
**File:** `Level1_Task1_TopCuisines.py`

- Identified the **top 3 most common cuisines** in the dataset by exploding multi-cuisine entries per restaurant
- Calculated the **percentage of restaurants** serving each of those top cuisines

**Approach:** Split the `Cuisines` column (comma-separated), exploded into individual rows, and used `.value_counts()` to rank

**Key Insight:** Certain cuisines dominate the dataset with significantly higher representation than others.

---

### ✅ Task 2 — City Analysis
**File:** `Level1_Task2_CityAnalysis.py`

- Found the **city with the highest number of restaurants**
- Calculated **average ratings per city** and sorted them
- Identified the **city with the highest average rating**

**Approach:** Used `.value_counts()` for restaurant count and `.groupby()` + `.mean()` for average ratings per city

**Key Insight:** The city with the most restaurants is not necessarily the one with the highest average rating.

---

### ✅ Task 3 — Price Range Distribution
**File:** `Level1_Task3_PriceRangeDistribution.py`

- Created a **bar chart** showing distribution of restaurants across price range categories (1–4)
- Calculated the **percentage of restaurants** in each price range

**Approach:** Used `.value_counts()` on the `Price range` column and visualized with Matplotlib bar chart

**Key Insight:** A majority of restaurants fall in the lower price ranges, indicating a budget-friendly market.

---

### ✅ Task 4 — Online Delivery
**File:** `Level1_Task4_OnlineDelivery.py`

- Determined the **percentage of restaurants offering online delivery**
- Compared **average ratings** of restaurants with vs. without online delivery

**Approach:** Boolean filter on `Has Online delivery == "Yes"` and `.groupby()` comparison on ratings

**Key Insight:** Restaurants with online delivery tend to have different average ratings compared to those without.

---

## 📈 Level 2 — Deeper Analysis

### ✅ Task 1 — Restaurant Ratings
**File:** `Level2_Task1_RestaurantRatings.py`

- Plotted a **histogram** of aggregate ratings to visualize distribution
- Used `pd.cut()` to bin ratings into ranges and find the **most common rating range**
- Calculated the **average number of votes** received by restaurants

**Approach:** Histogram with 10 bins using `.hist()` and binning with `pd.cut()` across intervals [0–1, 1–2, 2–3, 3–4, 4–5]

**Key Insight:** Most restaurants cluster around a specific rating range, with average votes revealing overall engagement patterns.

---

### ✅ Task 2 — Cuisine Combination
**File:** `Level2_Task2_CuisineCombination.py`

- Identified the **top 10 most common cuisine combinations** (multi-cuisine pairings)
- Determined which **cuisine combinations tend to have higher average ratings**

**Approach:** Used `.value_counts()` directly on the `Cuisines` column (which includes combos) and `.groupby().mean()` for rating analysis

**Key Insight:** Certain cuisine combos consistently attract higher ratings, suggesting that pairing certain cuisines appeals more to customers.

---

### ✅ Task 3 — Geographic Analysis
**File:** `Level2_Task3_GeographicAnalysis.py`

- Plotted **restaurant locations on a scatter map** using Longitude and Latitude
- Identified **geographic clusters** by grouping restaurants at identical coordinates

**Approach:** Scatter plot with `plt.scatter()` using `Longitude` on X-axis and `Latitude` on Y-axis; grouped by coordinates for cluster analysis

**Key Insight:** Restaurants are heavily concentrated in specific geographic zones, indicating urban density and market saturation in certain regions.

---

### ✅ Task 4 — Restaurant Chains
**File:** `Level2_Task4_RestaurantChains.py`

- Identified **restaurant chains** (names appearing more than once in the dataset)
- Analyzed chains by **average rating** and **total votes** (popularity)

**Approach:** Used `.value_counts()` to find duplicated restaurant names, then `.groupby().agg()` to compute average rating and total votes per chain

**Key Insight:** Well-known chains have significantly higher vote counts, indicating stronger brand recognition and customer engagement.

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

3. **Update the dataset path** in any `.py` file  
   Replace the `file_path` variable at the top of each script with your local path to the dataset CSV:
   ```python
   file_path = "path/to/your/Dataset.csv"
   ```

4. **Run any script**
   ```bash
   python Level1_Task1_TopCuisines.py
   ```

> 📝 The dataset used is a restaurant dataset provided as part of the Cognifyz Technologies internship program. It is not included in this repository.

---

## 📷 Sample Outputs

Each task has a corresponding `.png` file showing the visualization output. You can view them directly in the repository file listing above.

| Task | Output File |
|------|-------------|
| Level 1 – Top Cuisines | `Level1_Task1_TopCuisines.png` |
| Level 1 – City Analysis | `Level1_Task2_CityAnalysis.png` |
| Level 1 – Price Range | `Level1_Task3_PriceRangeDistribution.png` |
| Level 1 – Online Delivery | `Level1_Task4_OnlineDelivery.png` |
| Level 2 – Rating Distribution | `Level2_Task1_RestaurantRatings.png` |
| Level 2 – Cuisine Combos | `Level2_Task2_CuisineCombination.png` |
| Level 2 – Geographic Map | `Level2_Task3_GeographicAnalysis.png` |
| Level 2 – Restaurant Chains | `Level2_Task4_RestaurantChains.png` |

---

## 🤝 Acknowledgements

- **[Cognifyz Technologies](https://www.cognifyz.com)** for the internship opportunity and dataset
- The internship program provided hands-on experience in real-world data analysis workflows

---

## 📬 Connect with Me

- **LinkedIn:** [Het Ladani](https://linkedin.com/in/het-ladani-5001bb29a/)
- **GitHub:** [@ladanihet2410](https://github.com/ladanihet2410)
- **Email:** ladanihet2410@gmail.com

---

*This project was completed as part of the Cognifyz Technologies Data Analysis Internship Program — 2026.*
