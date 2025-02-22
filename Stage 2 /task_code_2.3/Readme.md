# **Metabolic Response Analysis of Pesticide Treatment in WT and Mutant Cells** 

### Team members:
*Chama Benslimane (leader)* ; GitHub profile : https://github.com/BenslimaneChama
and
*Mohammad Hicham Polo* ; GitHub profile : https://github.com/MohammadHichamPolo
**HackBio Internship - Stage 2 Task**

---
## **Introduction**
In this study, the metabolic reactions of wild-type (WT) and mutant cells to pesticide treatment are examined. In addition to highlighting metabolites that show notable fluctuation, the study detects metabolic changes throughout a 24-hour period. The metabolic response of WT and mutant strains is compared in the study using statistical and visual methods.

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
And contains metabolite intensity readings under different conditions:
- `WT_DMSO`: Wild-type cells treated with DMSO (control).
- `WT_24h`: Wild-type cells treated with pesticides for 24 hours.
- `Mutant_DMSO`: Mutant cells treated with DMSO (control).
- `Mutant_24h`: Mutant cells treated with pesticides for 24 hours. <br/>
The dataset is loaded and processed using pandas.

## **Analysis steps**

###  **1. Computing Metabolic Differences (ΔM)**
ΔM (delta M) is calculated for both WT and mutant strains as:
ΔM = Metabolite Intensity after 24h − Metabolite Intensity at 0h
```
deltaM_WT = WT_24h - WT_DMSO
deltaM_Mutant = Mutant_24h - Mutant_DMSO
```

### 
