# 📊 Multivariate Data Analysis using NumPy & Matplotlib

> A complete implementation of fundamental multivariate statistical analysis techniques using Python, NumPy, and Matplotlib. This project explores descriptive statistics, matrix operations, covariance, correlation analysis, Euclidean distances, and graphical visualization on a real-world sports participation dataset.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![NumPy](https://img.shields.io/badge/NumPy-Matrix_Computing-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green)
![Statistics](https://img.shields.io/badge/Statistics-Multivariate-red)
![Master](https://img.shields.io/badge/Master-MIV-lightgrey)

---

# 📖 Overview

This project presents a complete implementation of the fundamental concepts of **multivariate statistical data analysis** using Python.

The objective is to manipulate and analyze a multivariate dataset describing sports participation rates among young people across twenty different cities.

Rather than relying on specialized statistical software, every operation is implemented directly using **NumPy**, allowing a deeper understanding of matrix algebra and statistical computations.

The project was developed as part of the **Master's Program in Image Processing & Artificial Intelligence (MIV)** at **USTHB**.

---

# ✨ Features

- 📊 Matrix manipulation using NumPy
- 🔄 Matrix transpose computation
- 👥 Individual (city) extraction
- 📈 Variable extraction into vectors
- 📏 Euclidean distance computation
- 📉 Mean, variance and standard deviation calculation
- 🎯 Average individual computation
- ➖ Centered data matrix generation
- 📐 Covariance matrix computation
- 🔗 Correlation matrix computation
- 📊 Scatter plot visualization
- 🧮 Statistical function implementation from scratch

---

# 📑 Project Report

## Project Objective

Multivariate data analysis is one of the most important branches of statistics and machine learning. Before applying advanced algorithms such as Principal Component Analysis (PCA), clustering, or classification, it is essential to understand the statistical properties of the data.

The objective of this practical work is to manipulate a multivariate dataset representing the participation rates of young people in different sports across twenty cities.

Each city is described by six quantitative variables:

- 🤾 Handball
- 🏀 Basketball
- 🎾 Tennis
- 🤸 Gymnastics
- 🏊 Swimming
- ⚽ Football

The project introduces the fundamental statistical concepts required for exploratory data analysis through matrix computations and graphical representations.

---

# 🧠 Why NumPy?

NumPy is the fundamental numerical computing library in Python and provides efficient support for multidimensional arrays and linear algebra operations.

Compared to manually implementing matrix computations using Python lists, NumPy offers:

- Faster execution
- Optimized memory usage
- Powerful vectorized operations
- Built-in linear algebra routines
- High numerical precision

Its efficiency makes it the standard library for scientific computing, machine learning, and data science.

---

# 📚 Statistical Concepts Covered

This project covers several important concepts in descriptive and multivariate statistics.

## Matrix Representation

The dataset is represented as a matrix:

- Rows → Cities (Individuals)
- Columns → Sports (Variables)

This representation allows efficient mathematical manipulation and statistical analysis.

---

## Descriptive Statistics

For every variable, the following statistical measures are computed:

- Arithmetic Mean
- Variance
- Standard Deviation

These indicators summarize the distribution and variability of each sport across the twenty cities.

---

## Euclidean Distance

Distances are computed between selected cities.

The Euclidean distance measures how similar or different two cities are according to their sports participation profiles.

Smaller distances indicate more similar cities.

Larger distances indicate more distinct cities.

---

## Centered Matrix

The centered matrix is obtained by subtracting the mean of each variable from every observation.

Centering is an essential preprocessing step before many multivariate analysis techniques such as:

- PCA
- Factor Analysis
- Clustering
- Linear Regression

---

## Covariance Matrix

The covariance matrix measures how variables vary together.

Positive covariance indicates that two sports tend to increase together.

Negative covariance indicates opposite behavior.

Values close to zero suggest weak linear dependence.

---

## Correlation Matrix

Unlike covariance, correlation standardizes the relationships between variables.

Correlation values range from:

- +1 → Perfect positive correlation
- 0 → No linear correlation
- -1 → Perfect negative correlation

This matrix provides a scale-independent measure of similarity between variables.

---

# ⚙️ Project Workflow

## 1️⃣ Data Preparation

- Load sports participation dataset
- Store data in a NumPy matrix
- Generate matrix transpose
- Create vectors for every variable

---

## 2️⃣ Individual Manipulation

Operations include:

- Listing cities
- Accessing selected cities
- Comparing individuals
- Distance computation

---

## 3️⃣ Statistical Analysis

For every variable:

- Mean
- Variance
- Standard deviation

An average individual is also computed.

---

## 4️⃣ Data Centering

The project computes the centered matrix by subtracting variable means.

This removes the influence of absolute values and prepares the data for covariance analysis.

---

## 5️⃣ Covariance Analysis

The covariance matrix is generated using matrix multiplication.

It describes the joint variability between all pairs of variables.

---

## 6️⃣ Correlation Analysis

The covariance matrix is normalized to obtain the correlation matrix.

This allows direct comparison of relationships between variables regardless of their measurement scales.

---

## 7️⃣ Data Visualization

Scatter plots are generated for several pairs of variables:

- Handball vs Gymnastics
- Basketball vs Swimming
- Tennis vs Football

These visualizations reveal:

- Correlation
- Clustering tendencies
- Outliers
- Dispersion patterns

---

# 📂 Project Structure

```text
Multivariate-Data-Analysis-with-NumPy-and-Matplotlib/

│
├── TP1.py
├── TP1_Report.pdf
├── images/
│   ├── scatter_plot_1.png
│   ├── scatter_plot_2.png
│   ├── scatter_plot_3.png
│   └── covariance_matrix.png
│
├── results/
│   ├── statistics.txt
│   ├── covariance_matrix.csv
│   ├── correlation_matrix.csv
│   └── centered_matrix.csv
│
└── README.md
```

---

# ▶️ Running the Project

Install the required packages

```bash
pip install numpy matplotlib
```

Run the Python program

```bash
python TP1.py
```

---

# 📊 Dataset

The dataset contains observations from **20 cities**, where each city is described using participation rates in six sports.

Variables include:

- Handball
- Basketball
- Tennis
- Gymnastics
- Swimming
- Football

This multivariate dataset serves as a practical example for statistical exploration and matrix-based analysis.

---

# 📈 Output

The program produces:

- Matrix X
- Transposed matrix
- Individual list
- Variable vectors
- Euclidean distances
- Statistical summary table
- Average individual
- Centered matrix
- Covariance matrix
- Correlation matrix
- Scatter plots

---

# ✅ Strengths

- Pure NumPy implementation
- Efficient matrix computations
- Clear statistical methodology
- Well-structured code
- Easy to extend
- Excellent educational project
- Strong mathematical foundation

---

# ⚠️ Limitations

- Small dataset
- Static data input
- No graphical interface
- Limited to descriptive statistics
- No predictive machine learning

---

# 🚀 Future Improvements

Possible extensions include:

- Principal Component Analysis (PCA)
- Hierarchical Clustering
- K-Means Clustering
- Heatmap visualization
- Interactive dashboards
- Statistical hypothesis testing
- Automatic report generation
- Jupyter Notebook version
- Pandas integration
- Seaborn visualizations

---

# 🛠️ Technologies Used

- Python
- NumPy
- Matplotlib
- Linear Algebra
- Descriptive Statistics
- Matrix Computations

---

# 🎓 Learning Outcomes

This project demonstrates practical implementation of:

- Matrix algebra
- Statistical analysis
- Data preprocessing
- Covariance computation
- Correlation analysis
- Exploratory Data Analysis (EDA)
- Scientific computing with NumPy
- Data visualization using Matplotlib

---

# 📚 References

- NumPy Documentation
- Matplotlib Documentation
- Introduction to Statistical Learning (ISLR)
- Applied Multivariate Statistical Analysis
- Python Scientific Computing Documentation
- USTHB – Master MIV Data Analysis Course
