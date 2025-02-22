# **Metabolic Response Analysis of Pesticide Treatment in WT and Mutant Cells** 

### Team members:
*Chama Benslimane (leader)* ; GitHub profile : https://github.com/BenslimaneChama
and
*Mohammad Hicham Polo* ; GitHub profile : https://github.com/MohammadHichamPolo
**HackBio Internship - Stage 2 Task**

---
## **Introduction**
This project analyzes the metabolic response of wild-type (WT) and mutant cells to pesticide treatment using Python. We compute metabolic shifts (ΔM), visualize differences with scatter plots, and identify outlier metabolites that show significant variation. Additionally, we track metabolite evolution over time to understand how metabolic pathways are affected. By comparing WT and mutant responses, we gain insights into pesticide impact, metabolic adaptation, and potential resistance mechanisms.

## **Required Module**
This analysis is powered by the following Python libraries:
```
pip install pandas numpy matplotlib seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```
`pandas`: For data loading, manipulation, and preprocessing.
`numpy`: For numerical operations, such as computing metabolic differences (ΔM).
`matplotlib`: For creating visualizations, such as scatter and line plots.
`seaborn`: For enhanced statistical plotting and styling.

## **Dataset**
The dataset is sourced from HackBio-Internship 
```
# Importing data
url = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/Pesticide_treatment_data.txt"
```
## **Extracting Metabolite Values for WT and Mutant Cells**
We extract metabolite intensity values for both wild-type (WT) and mutant cells before and after pesticide treatment.
The dataset’s first column contains labels, so we filter rows using conditions like `df["Unnamed: 0"] == "WT_DMSO_1".`
`.iloc[:, 1:]` selects all metabolite columns, and `.values.flatten()` converts them into 1D arrays.

## **Analysis steps**

### **1. Computing Metabolic Differences (ΔM)**
`metabolites = df.columns[1:]` stores the names of all metabolites for later use.
ΔM (Delta M) is computed by subtracting metabolite intensities before and after treatment:
  - For WT: `WT_24h - WT_DMSO`
  - For Mutants: `Mutant_24h - Mutant_DMSO`

### **2. Scatter Plot of ΔM (WT vs. Mutant)**
- We plot each metabolite’s ΔM in WT vs. ΔM in the mutant as a scatter plot.
- The dashed black line (y = x) represents an equal metabolic response in both strains.
- If a point is above the line, the metabolite increased more in the mutant.
- If a point is below the line, the metabolite decreased more in the mutant.
```
plt.xlabel("ΔM Wild Type")
plt.ylabel("ΔM Mutant")
plt.title("Comparaison de la Réponse Métabolique WT vs Mutant")
plt.legend()
plt.show()
```
![Comparaison de la Réponse Métabolique WT vs Mutant](figures/scatter_plot.png)
This plot visually highlights differences in metabolic responses between WT and mutant strains.

ANSWERING THE QUESTION : How do you explain the trends you see on either direction of the plot? 
The reference line y=x serves as a benchmark to assess whether the metabolic changes (ΔM) in WT and MUT conditions follow a similar trend. 
The distribution of points closely follows this line, indicating a strong positive correlation between ΔM in both conditions. 
However, as ΔM increases, we observe a higher density of points, suggesting that the treatment induces metabolic changes in both WT and MUT to a similar extent. 
This means that while the treatment has a measurable impact, its effect is comparable in both conditions.

### **3. Residuals & Outlier Detection**
We calculate residuals to measure the difference:
```
residuals = deltaM_Mutant - deltaM_WT
```
Threshold = 0.3:
- Grey points: Within threshold (low variation).
- Salmon points: Beyond threshold (high variation, key outliers).
```
plt.plot(x_vals, x_vals, color='black', linestyle='--', label="y = x")
plt.xlabel("ΔM Wild Type")
plt.ylabel("ΔM Mutant")
plt.title("Metabolic difference between WT vs Mutant with residuals threshold at 0,3")
plt.legend()
plt.show()
```
![Metabolic difference between WT vs Mutant with residuals threshold at 0,3](figures/residuals_plot.png)
Outliers represent metabolites with a strong differential response, helping us focus on key biological changes.

### **4. Extracting Outlier Metabolites**
We filter and extract names of metabolites where the residuals exceed the 0.3 threshold.
The output is a list of key metabolites showing strong metabolic shifts.
```
outliers = metabolites[np.abs(residuals) > threshold].tolist()
```
### **5. Time Series Analysis of Selected Metabolites**
This section focuses on how metabolite levels evolve over time after pesticide treatment. Instead of just looking at one time point (24h), we check how metabolic changes progress from 0h to 8h to 24h.<br/>
So first we select metabolites for the time series Plot, because we can't plot all 65 outliers at once. Then we prepare the time series data, because the figure size ensures clear visualization, and different colors help distinguich metabolite trends.<br/>
And on step 3, we plot metabolic changes over time, by looping over the selected metabolites, then we extract the metabolites values at different time points for WT and mutant cells, this let us compare how WT and mutant cells metabolize over time and track trends in metabolic responses.<br/>
On the last step, we Format and siplay the plot 
```
plt.xlabel("Time")
plt.ylabel("Metabolic Intensity")
plt.title("Metabolic Evolution Over 24h for 6 Selected Metabolites (WT vs MUT)")

plt.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.tight_layout()  
plt.show()
```
![Metabolic Evolution Over 24h for 6 Selected Metabolites (WT vs MUT)](figures/metabolic_evolution.png)
