#  Salary Prediction

##  Description and Context

This research aims **to find the best fit through an equation that can predict salary according to given features**, with the goal of building a model that can be used to predict the salary of a new employee or groups of employees in line with the most impactful characteristics.

This project uses **Exploratory Data Analysis (EDA)** and **Machine Learning** models to predict salaries based on multiple characteristics.

Due to professional qualifications and length of service, many employees are looking for **a salary consistent with their skills**, whether to position themselves appropriately in the job market or to start over or request a promotion within companies. 

For the business, it is extremely profitable **to stimulate social well-being at work when employees are paid according to their skills and qualifications,** in addition to increased productivity and a sense of belonging and teamwork being leveraged, which directly impacts the company's objectives and mission.

The financial impact on the company depends on the current configuration of how employees are paid. To avoid confirmation bias or distorted value judgments, this analysis aims **to find the most appropriate relationship for employee compensation, considering the characteristics that most impact such compensation.**

It can be used as a reconfiguration of the payroll for all employees or a new vision of how to compensate new employees during their hiring. improving the career plan and people management planning with the HR team.


##  Project Overview: Data

The dataset was obtained from Kaggle:  
https://www.kaggle.com/datasets/algozee/employee-salary-prediction-dataset

- **250,000 rows**
- **10 features**

<details>
<summary> Dataset Description</summary>


##  Dataset Description

The dataset includes:

- **job_title** – Job role  
- **experience_years** – Years of experience  
- **education_level** – Education level  
- **skills_count** – Number of skills  
- **industry** – Industry  
- **company_size** – Company size  
- **location** – Country  
- **remote_work** – Work type (Remote/Hybrid/On-site)  
- **certifications** – Number of certifications  
- **salary** – Target variable

The data does not present missing or any other errors, but it is focused on performing inferences or predictions through machine learning. During EDA or modeling, it is noticeable that we could analyze more precisely the relationship between location and educational level, certifications, and remote work. However, the objective is to focus on predicting salary and not on how location and education are related. Furthermore, the database does not present more information about the specific relationship between education and location to explore how location can influence education, which would affect employee salaries.

Since datasets on Kaggle are used to support training or testing of other skills and programs, this data is subject to change and is consistent with the analysis proposed here.

Regarding the feature industry, this could be removed from the dataset as it doesn't have a strong impact on salary prediction; however, this fact only became evident during the analysis. It's interesting to note that regardless of the type of industry the employee works in, it has little influence on salary. This is clearly due to the fact that IT jobs don't require very significant changes in company structures.


</details>

---

<details>
<summary> Technologies and tools </summary>
---

 
##  Technologies and tools
- The technologies and tools used were Python (Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn, Plotly), Git and Github (version control), machine learning classification algorithms, statistics and Visual Studio Code (project development environment).

##  Data Exploration

###  Data Quality

- No missing values  
- Clean and well-structured dataset  
- Balanced distribution across categories  

---

###  Summary Statistics

- Average salary: **145,718**
- Min salary: **31,867**
- Max salary: **333,046**
- Average experience: **10 years**

</details>

---

<details>
<summary> Exploratory Data Analysis</summary>

##  Exploratory Data Analysis



###  Company Size vs Salary

![Company Size vs Salary](graphics/Company_size_bar.png)

Company size is the most impactful factor in salary. The graph  shows that Enterprise companies pay **169,616** compared to Startups **127,289**, a difference of 42k. This may be due to market experience or investments in trained teams or materials; these factors require further analysis for precise confirmation. However, large companies pay more than small companies and startups.


- Enterprise: **169,616**
- Startup: **127,289**


-> **Most impactful variable**

---

###  Location Analysis

- Dataset is balanced across countries (~25k each)

### Salary by Location

![ Top 10 most frequent locations by salary](graphics/Top_location_salary_bar.png)

- USA: **181,716**
- Canada: **167,391**
- UK: **160,075**
- Germany: **153,377**
- ...
- Singapore: **139,341**
- India: **139,295**

##  Top 10 Most Frequent Locations

| Rank | Location     | Frequency |
|------|--------------|----------|
| 1    | Australia    | 25258    |
| 2    | Canada       | 25165    |
| 3    | Sweden       | 25100    |
| 4    | Remote       | 25065    |
| 5    | Singapore    | 25035    |
| 6    | USA          | 24931    |
| 7    | UK           | 24927    |
| 8    | India        | 24895    |
| 9    | Netherlands  | 24861    |
| 10   | Germany      | 24763    |

-> Difference > **40k**
-> **Strong impact**

The graph highlights that location is the most important factor impacting salary. It shows the 10 highest-paying locations, and it's noticeable that the most frequent location according to EDA (Australia) is not the highest-paying (USA). This can be deduced from the high investment in IT and the presence of giant companies that dominate the market.


---

###  Education vs Salary

![Education vs Salary](graphics/Education_level_salary_box.png)

- PhD: **163,976**
- Master: **153,305**
- Bachelor: **142,410**
- High School: **131,715**


As can be seen in the boxplot graph, there is a high presence of outlines, but overall the average salary increases with the level of education. It is noted that PhD employees receive more than 269,000 reaching up to 333,000, with a similar variation for those with a Master's degree.

-> Higher education → higher salary  
-> Difference ~ **32k**


---
### Education Distribution Across Locations

Education levels are evenly distributed across all locations, with no significant differences between countries.

This indicates that salary variations across regions are not driven by differences in education levels, but are more likely influenced by economic conditions and market demand.

---

#### Key Insight

-> Salary differences are primarily driven by **market conditions**, not by education or certifications.

---

### Experience vs Salary


![Experience vs Salary](graphics/Experience_salary_line.png)

- 0 years: **118,872**
- +9 years: **142,763**


The line graph shows that the relationship between salary and experience is almost directly proportional, reaching a point where an increase of 5 years of experience adds 10,000 or 15,000 to the salary.

-> **Strong upward trend**  
-> Correlation: **0.44 (moderate)**

---


### Correlation Analysis


![Correlation Matrix ](graphics/Corr_matrix_experience_skills_certifications.png)

| Relationship | Correlation |
|-------------|------------|
| Salary vs Experience | **0.44** |
| Salary vs Skills | **0.13** |
| Salary vs Certifications | **0.07** |

Experience is the strongest numerical predictor
---

###  Skills

Regarding skills, a low correlation is observed, but high in comparison with certifications, with a value of **0.13**.

![Number of Skills by Salary](graphics/Number_skills_salary_line.png)

When we analyze the line graph of the relationship with salary, a somewhat linear relationship is noted, with a small but noteworthy impact.

- 1 skill: **137,788**
- +10 skills: **145,163**

 Slight increase (~7k)

---
### Remote Work

![Remote Work vs Salary](graphics/Remote_work_salary_bar.png)

In the comparative analysis between remote and hybrid or in-person work, it is noted that people who work remotely earn more, on average. However, when compared to other variables, the impact is small, around 5,000.

- Remote: **149,279**
- Hybrid: **143,969**
- On-site: **143,932**

-> Slight impact (~5k)

---

###  Certifications

- 0: **141,492**
- 5: **149,607**


Certifications also show a near-linear relationship with salary, but the impact is small compared to other factors. In summary, a correlation matrix was performed with salary, experience, skills, and certifications; it is noted that certifications show a correlation of **0.07** (the lowest of all).

This reinforces the moderate (or strong in this case) relationship with experience.

-> Small impact  
-> Correlation: **0.07 (weak)**


---

### Certifications by Location

In order to complement the study, we analyzed the relationship between certifications and location to assess the impact of one on the other and whether this relationship influenced salary. At EDA, it is observed that certification does not show considerable variation; that is, regardless of where the employee resides, they may have more or fewer certifications.

**Certification by Location**

| Rank | Location     | Average Certification |
|------|--------------|----------------------|
| 1    | Germany      | 2.503493             |
| 2    | Netherlands  | 2.493906             |
| 3    | India        | 2.488371             |
| 4    | Canada       | 2.487145             |
| 5    | Singapore    | 2.485920             |
| 6    | Remote       | 2.485139             |
| 7    | UK           | 2.476110             |
| 8    | Australia    | 2.471771             |

- Range: **2.47 – 2.52**

-> Very small variation across countries


---

### Industry

No significant impact (~145k across all)


---

### Job Role Analysis: Most Common Roles


![Top Most Frequent Job Role](graphics/10_most_freq_job_role_bar.png)

The most frequent job titles are studied, and it is noted that the 10 most frequent (appearing more than 20,000 times) are: 

- Backend Developer  
- Cybersecurity Analyst  
- Product Manager 
- AI Engineer
- Data Scientist
... 
As described in the bar graph.

### Highest Paying Roles

![Top 10 Highest Pay Jobs](graphics/Top_10_highest_pay_jobs_bar.png)

Although the most frequent job titles are not necessarily the highest paying, the chart of the top 10 highest-paying jobs shows that the AI ​​Engineer position is the highest paid at **173,498**, followed by ML Engineer, Product Manager, Cloud Engineer, and DevOps Engineer (**149,959**). Notably, these figures are due to other factors beyond the scope of this analysis, such as company size, company type, location, etc. However, it is interesting to note that Backend Developer is the second highest-paid position.

-> Most frequent ≠ highest paid

This section is merely a curiosity for the reader, since the type of position obviously influences the salary, as has been shown, but more data is needed to establish it as one of the factors impacting salary due to its complexity.

---

### Skills & Education

- Skills average ≈ **10 for all education levels**
- Certifications average ≈ **2.5 for all**

No strong relationship between:
- Education ↔ Skills  
- Education ↔ Certifications  

</details>

---
<details>
<summary> Machine Learning</summary>

## Machine Learning

According to the objective of this analysis, the data presents excellent qualities and relationships for creating a linear regression model. We begin with the regression model and then use the Random Forest model to confirm or suggest another model that better fits the data.


### Methodology - ML Pipeline

#### Pre-processing

1) Encoding: One-Hot Encoding (OHE) with drop_first=True
   - Nominal categorical data without hierarchical order.
   - drop_first avoids perfect multicollinearity in linear regression.
  
2) NO scaling (StandardScaler/MinMaxScaler):
   - OLS Linear Regression is invariant to coefficient scale.
   - Random Forest is based on partition decisions, also invariant.
   - Conscious decision to maintain interpretability of coefficients.

3) Hold-out validation (not cross-validation):
   - Dataset large enough (assuming > 10k samples).
   - Simplicity for initial prototype.
   - Next iteration: implement k-fold (k=5) for more robustness.

4) Chosen metrics:
   - MAE (interpretable in original unit: salary in $)
   - R² (proportion of explained variance)

#### Models Used

**Linear Regression** (Default parameters (OLS)): Interpretable baseline showing linear relationships between features and salary.

**Random Forest** (n_estimators=100, random_state=42): Captures non-linear relationships and feature interactions, provides variable importance.

#### Evaluation Metrics

- **MAE (Mean Absolute Error)**: Average absolute error in original units (dollars)
- **R² (Coefficient of Determination)**: Proportion of variance explained by the model

#### Measures Taken Against Data Leakage

- Train/test split BEFORE any transformation
- Random Forest uses only training data to calculate feature importance
- No test set information leaks into training
- Reproducible pipeline with fixed random_state (42)

#### Pipeline Diagram
```text
┌─────────────────────────────────────────────────────────────────┐
│              PIPELINE WITH DATA LEAKAGE PREVENTION              │
└─────────────────────────────────────────────────────────────────┘

  STEP 1: LOAD DATA
  ┌────────────────────────┐
  │  df = pd.read_csv()    │
  │  X = df.drop('salary') │
  │  y = df['salary']      │
  └───────────┬────────────┘
              │
              ▼
  STEP 2: ENCODING (DOES NOT USE y)
  ┌────────────────────────┐
  │  X = pd.get_dummies(X) │
  │  (Features only)       │
  └───────────┬────────────┘
              │
              ▼
  STEP 3: SPLIT (BEFORE ANY FIT)
  ┌────────────────────────┐
  │  X_train, X_test,      │
  │  y_train, y_test       │
  │  random_state=42       │
  └───────────┬────────────┘
              │
      ┌───────┴───────┐
      │               │
      ▼               ▼
┌──────────┐     ┌──────────┐
│ X_train  │     │ X_test   │
│ y_train  │     │ (SEALED) │
└─────┬────┘     └─────┬────┘
      │                │
      ▼                │
┌──────────────┐       │
│ FIT MODELS   │       │
│              │       │
│ lr.fit()     │       │
│ rf.fit()     │       │
└──────┬───────┘       │
       │               │
       │    ┌──────────┘
       │    │
       ▼    ▼
┌────────────────┐
│  PREDICT       │
│  y_pred =      │
│  model.predict │
│  (X_test)      │
└───────┬────────┘
        │
        ▼
┌────────────────┐
│  METRICS       │
│  MAE(y_test,   │
│      y_pred)   │
│  R²(y_test,    │
│     y_pred)    │
└────────────────┘
```

### Reproducibility

All experiments are reproducible thanks to:

- Fixed random seeds: random_state=42 in all random operations.
- Deterministic pipeline: Same transformations applied to each execution.
- Library versions specified in requirements.txt.

### Model 1: Linear Regression

- MAE: **5,436**
- R²: **0.963**

-> Excellent performance  
-> Low prediction error  

---

### Model 2: Random Forest

- MAE: **5,693**
- R²: **0.961**

---

##  Model Comparison

| Model | MAE | R² |
|------|-----|----|
| Linear Regression | **5,436** | **0.963** |
| Random Forest | 5,693 | 0.961 |

---

###  Key Insight

-> Linear Regression performed slightly better  

-> Indicates **strong linear relationships** in the dataset  

### Equation

salary = 146756.08 + (41971.55 * location_USA) + (27941.45 * location_Canada) + (21532.27 * education_level_PhD) + (20967.21 * location_UK) + (13988.38 * location_Germany) + (10829.82 * education_level_Master) + (5338.89 * remote_work_Yes) + (2698.57 * experience_years) + (1613.18 * certifications) + (857.19 * skills_count)

</details>

---

<details>
<summary> Feature Importance </summary>

## Top 10 Most Important Features (Random Forest)

| Rank | Feature                     | Importance |
|------|----------------------------|-----------|
| 1    | experience_years           | 0.2003    |
| 2    | location_India             | 0.1818    |
| 3    | location_USA               | 0.0757    |
| 4    | company_size_Startup       | 0.0611    |
| 5    | education_level_PhD        | 0.0607    |
| 6    | company_size_Small         | 0.0508    |
| 7    | job_title_Data Analyst     | 0.0446    |
| 8    | company_size_Medium        | 0.0437    |
| 9    | job_title_Business Analyst | 0.0425    |
| 10   | location_Canada            | 0.0344    |

The model identified experience, location, and company size as the most important features for predicting salary.
This confirms the insights obtained during the exploratory data analysis.

Note: The evidenced features presented here are intended only to highlight the most impactful features obtained through random forest analysis, which aligns with the features obtained through linear regression. However, as shown, random forest analysis does not represent the best approximation of the prediction.

</details>

---

<details>
<summary> Final Conclusions </summary> 

## Final Conclusions

The analysis shows that salary is primarily driven by market-related factors (location and company size) rather than individual attributes such as skills or certifications.

1) Company size and location are the strongest factors influencing salary
2) Experience is a strong and consistent predictor
3) Education has a moderate impact on salary
4) Skills, certifications, and remote work have limited influence
5) Industry shows almost no impact on salary variation
6) The dataset is highly structured with low noise
7) Simpler models outperform complex ones due to strong linear relationships

</details>

---

<details>
<summary> Reference </summary> 

## Reference

BRYNJOLFSSON, Erik; MCAFEE, Andrew. Big data: the management revolution. Harvard Business Review, vol. 90, no. 10, p. 60–68, 2012.

BRYNJOLFSSON, Erik; HITT, Lorin M.; KIM, Heekyung H. Strength in numbers: how does data-driven decision making affect firm performance? 2011. Available as working paper (MIT / NBER).

BECKER, Gary. Human capital: a theoretical and empirical analysis, with special reference to education. 3rd ed. Chicago: University of Chicago Press, 1993.

AKERLOF, George A.; YELLEN, Janet L. The fair wage-effort hypothesis and unemployment. The Quarterly Journal of Economics, vol. 105, no. 2, p. 255–283, 1990.

DECI, Edward L.; RYAN, Richard M. Intrinsic motivation and self-determination in human behavior. New York: Plenum, 1985.

PORTER, Michael E. Competitive advantage: creating and sustaining superior performance. New York: Free Press, 1985.

AKERLOF, George A. Labor contracts as partial gift exchange. The Quarterly Journal of Economics, vol. 97, no. 4, p. 543–569, 1982.

MINCER, Jacob. Schooling, experience, and earnings. New York: National Bureau of Economic Research, 1974.

DECI, Edward L. Effects of externally mediated rewards on intrinsic motivation. Journal of Personality and Social Psychology, vol. 18, no. 1, p. 105–115, 1971.

VROOM, Victor H. Work and motivation. New York: Wiley, 1964.

ADAMS, John Stacey. Toward an understanding of inequality. In: BERKOWITZ, L. (ed.). Advances in experimental social psychology. New York: Academic Press, 1963. p. 267–299.
</details>


</details>
