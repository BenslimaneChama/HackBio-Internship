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
   - Selecting best trained classifier
   - Develop a terminal interactive script predicting probability of depression
## Table of Contents
[University Student Depression Prediction System](#University-Student-Depression-Prediction-System)
1. [Introduction](#introduction)
2. [Dataset Preprocessing](#dataset-preprocessing)
3. [How to Use the Script](#how-to-use-the-script)
4. [Input Format](#input-format)
   - [Female Model Inputs](#female-model-inputs)
   - [Male Model Inputs](#male-model-inputs)
5. [Output](#output)
6. [Confusion Matrix Analysis](#Confusion_Matrix_Analysis)
   - [Female Model Confusion Matrix](#Female-Model-Confusion-Matrix)
   - [Male Model Confusion Matrix](#Male-Model-Confusion-Matrix)
8. [Dependencies](#dependencies)
9. [Running the Script](#running-the-script)

-------------------
# University Student Depression Prediction System

## Introduction
This script is designed to predict the likelihood of depression in university students based on various factors, including academic pressure, study satisfaction, financial stress, and sleep duration. The models were selected based on logistic regression due to its effectiveness in binary classification problems. The dataset has been preprocessed to include only students while removing irrelevant columns. Feature selection was performed to determine the most relevant predictors for male and female students separately.

## Dataset Preprocessing
- The script reads a dataset from an online source.
- Missing values are removed.
- Irrelevant columns such as `id`, `Profession`, `Job Satisfaction`, and `Work Pressure` are dropped.
- The dataset is filtered to include students from specific valid cities.
- Categorical features are encoded using `LabelEncoder`.
- Sleep duration is mapped to numerical values.
- The dataset is split into separate groups for male and female students.

## How to Use the Script
1. Run the script.
2. The system will prompt you to enter your gender (`female` or `male`).
3. Based on your input, the model will request specific features.
4. Enter the requested values according to the format specified below.
5. The system will output a prediction and the probability of depression.

## Input Format
The following variables need to be inputted:

### Female Model Inputs
| Variable                          | Type   | Description |
|-----------------------------------|--------|-------------|
| Age                               | float  | Age in years |
| Academic Pressure                 | float  | Scale from 0 to 5 |
| CGPA                              | float  | Cumulative Grade Point Average |
| Study Satisfaction                | float  | Scale from 0 to 5 |
| Sleep Duration                    | string | Choose from: `Less than 5 hours`, `5-6 hours`, `7-8 hours`, `More than 8 hours`, `Others` |
| Dietary Habits                    | string | Choose from: `Healthy`, `Moderate`, `Others`, `Unhealthy` |
| Have you ever had suicidal thoughts? | string | Choose `Yes` or `No` |
| Work/Study Hours                  | float  | Number of hours spent on work or studies per day |
| Financial Stress                   | float  | Scale from 0 to 5 |
| Family History of Mental Illness   | string | Choose `Yes` or `No` |

### Male Model Inputs
| Variable                          | Type   | Description |
|-----------------------------------|--------|-------------|
| Age                               | float  | Age in years |
| Academic Pressure                 | float  | Scale from 0 to 5 |
| Study Satisfaction                | float  | Scale from 0 to 5 |
| Dietary Habits                    | string | Choose from: `Healthy`, `Moderate`, `Others`, `Unhealthy` |
| Have you ever had suicidal thoughts? | string | Choose `Yes` or `No` |
| Work/Study Hours                  | float  | Number of hours spent on work or studies per day |
| Financial Stress                   | float  | Scale from 0 to 5 |
| Family History of Mental Illness   | string | Choose `Yes` or `No` |

## Output
The model will generate a prediction based on the provided inputs:
- **Prediction Result:** Displays whether the individual is likely to be depressed or not.
- **Probability of Depression:** Displays the probability percentage.
## Confusion Matrix Analysis
To evaluate the performance of both models, confusion matrices were generated for the male and female models. These matrices provide insight into the model’s accuracy, precision, recall, and F1-score.

### Female Model Confusion Matrix

![Female Confusion Matrix](https://github.com/BenslimaneChama/HackBio-Internship/blob/main/Stage%203/Figures/female_confusion.png)

### Male Model Confusion Matrix

![Male Confusion Matrix](https://github.com/BenslimaneChama/HackBio-Internship/blob/main/Stage%203/Figures/male_confusion.png)

Interpretation remains the same as for the female model. The confusion matrices help determine how well the models distinguish between depressed and non-depressed students. (more details are shown in the notebooks)
## Dependencies
Ensure you have the following Python libraries installed:
```bash
pip install pandas scikit-learn
```
## Running the Script
Run the script using:
```bash
python script.py
```
Follow the prompts to enter the required values.

