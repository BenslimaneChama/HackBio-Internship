# **Stage 3 - HackBio Internship: Neuroscience and Psychology**

### Team members:
*Chama Benslimane (leader)* ; GitHub profile : https://github.com/BenslimaneChama

and

*Mohammad Hicham Polo* ; GitHub profile : https://github.com/MohammadHichamPolo

## Project Overview

This project is part of the Stage 3 HackBio Internship, focusing on neuroscience and psychology. The objective is to analyze a dataset and use biostatistical and machine learning techniques to classify and detect signs of depression in university students.

what we did in this project :
   - Data preprocessing and exploration
   - Benchmark of 3 Machine learning classification models
   - Biostatistical analysis of relevant factors
   - Visualization and interpretation of results
## Table of Contents
1. [Project Overview](#project-overview)  

2. [Answering Questions](#Answering-Questions)
   - [Can you build a classification model to accurately predict depressed student?](#Can-you-build-a-classification-model-to-accurately-predict-depressed-student?)
   - [Can you describe what features determine depression in university students?](#Can-you-describe-what-features-determine-depression-in-university-students?)
   - [What would you tell people to watch out for if they were depressed?](#What-would-you-tell-people-to-watch-out-for-if-they-were-depressed?)
3. [How to Use the University Student Depression Prediction System](#How-to-Use-the-University-Student-Depression-Prediction-System)
-------------------

## Answering Questions
### Can you build a classification model to accurately predict depressed student?
The XGBoost model with RFE (6 features) was selected as the most efficient classification model. It achieves nearly the same accuracy as the Logistic Regression model trained on all features while requiring fewer inputs and maintaining the lowest False Positive Rate among all trained models.

Meanwhile the Logistic Regression model trained on all features remains the most accurate overall. Users can opt for this model if they are willing to input all 13 features for prediction. 

However, the user may come from a city or hold a degree that is entirely different from those found in the data used to train the models.

This also explains why the XGBoost model with six selected features is considered the default model, as it requires features that are available for any individual.

### Can you describe what features determine depression in university students?
PCA plots revealed no clear separation between depressed and non-depressed students, highlighting the complexity of depression, which cannot be accurately predicted using just one or two variables. However, certain features show strong correlations with depression. Notably, suicidal thoughts were consistently selected as the most influential predictor when RFE = 1, contributing approximately 78% to model performance.

The most significant features, as identified by XGBoost, include:

Age,
Academic Pressure,
Study Satisfaction,
Dietary Habits,
Suicidal Thoughts,
Financial Stress.

### What would you tell people to watch out for if they were depressed?
Based on this dataset, students already experiencing depression should pay attention to the six key predictive features. However, many of these, such as age and past suicidal thoughts, are unchangeable. Among the selected features, dietary habits stand out as the only modifiable factor.

Improving dietary habits may be a practical step for both managing and preventing depression.
## How to Use the University Student Depression Prediction System

### Requirements
Ensure you have the following Python libraries installed:

```bash
pip install pandas scikit-learn xgboost
```

### Running the Script
Run the script using Python:

```bash
python uni_wellness_predictor.py
```

### Input Requirements
The system provides two models for depression prediction:
1. **XGBoost Model (6 features)** – Selected features for faster evaluation.
2. **Logistic Regression Model (Full Features)** – More detailed analysis.

When prompted, enter your choice:
- Press **Enter** for XGBoost.
- Type `'LR'` and press **Enter** for Logistic Regression.

#### XGBoost Model Inputs
| Feature               | Type   | Valid Range / Values |
|----------------------|--------|----------------------|
| Age                  | `float` | Any positive number |
| Academic Pressure    | `float` | 0-5                 |
| Study Satisfaction   | `float` | 0-5                 |
| Dietary Habits       | `str`   | Healthy, Moderate, Others, Unhealthy |
| Suicidal Thoughts    | `str`   | Yes, No             |
| Financial Stress     | `float` | 0-5                 |

#### Logistic Regression Model Inputs
| Feature                     | Type   | Valid Range / Values |
|----------------------------|--------|----------------------|
| Gender                      | `str`   | Male, Female |
| Age                          | `float` | Any positive number |
| City                         | `str`   | (Choose from list of valid cities) |
| Academic Pressure            | `float` | 0-5 |
| CGPA                         | `float` | Any positive number |
| Study Satisfaction           | `float` | 0-5 |
| Sleep Duration               | `str`   | Less than 5 hours, 5-6 hours, 7-8 hours, More than 8 hours, Others |
| Dietary Habits               | `str`   | Healthy, Moderate, Others, Unhealthy |
| Degree                       | `str`   | (User-defined) |
| Suicidal Thoughts            | `str`   | Yes, No |
| Work/Study Hours             | `float` | Any positive number |
| Financial Stress             | `float` | 0-5 |
| Family History of Mental Illness | `str`   | Yes, No |

### Output
After entering the inputs, the system will display:
- **Prediction Result**: "Likely Depressed" or "Not Likely Depressed"
- **Probability of Depression**: A percentage indicating confidence in the prediction.

### Notes
- Ensure numerical values are entered correctly (e.g., no letters in numerical fields).
- String inputs must match the expected categories exactly.
- Invalid inputs will prompt re-entry.

For any issues, refer to the dataset structure and input expectations.

