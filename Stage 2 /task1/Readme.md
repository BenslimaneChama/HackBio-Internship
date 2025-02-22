# **Task 1 : Microbiology : Analysing curve growth** 

### Team members:
*Chama Benslimane (leader)* ; GitHub profile : https://github.com/BenslimaneChama
and
*Mohammad Hicham Polo* ; GitHub profile : https://github.com/MohammadHichamPolo
**HackBio Internship - Stage 2 Task**

---
## **Introduction**
This project anlyse the growth curves of different bacterian strains from experimental data. It includes the following steps:
        - First process and trasform raw data
        - Viualize growth for different strains
        - Caclulate the time needed to reach 80% of maximum density (OD600)
        - Perform stastical analyses to compare strains and mutations 
As part of this project, we used the same functions we'd done in the HackBio internship **stage 1**, on the same theme. So we used them and rearranged them.
So this project can be divided into two parts, the part where we reuse the functions, with a slight change, and then the part with the main code.

## Packages needed
But before we get started, let's introduce the libraries we've used to execute our code.
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
```
`pandas` : To manipulate the data in dataframe
`numpy` : for advanced calculation
`matplotlib.pyplot` : to trace graphics
`seaborn` : to ameliorate the style of visualisation
`scipy.stats` : for statistical tests on data
## Importing data and creating metadata
Once we've imported the packages we need, we'll import our folder to start work, creating the metadata.
A metadata, is a Dataframe, that is like the data I just imported, but completes it.
```
# Importing data
data = pd.read_csv("mcgc.tsv",  sep='\t')
# Creating metadata
metadata = pd.DataFrame({
    "Strain": [
        "Strain1_Rep1", "Strain1_Rep2", "Strain2_Rep1",
        "Strain2_Rep2", "Strain3_Rep1", "Strain3_Rep2"
    ],
    "WT_1": ["A1", "A3", "A5", "A7", "A9", "A11"],
    "MUT_1": ["A2", "A4", "A6", "A8", "A10", "A12"],
    "WT_2": ["B1", "B3", "B5", "B7", "B9", "B11"],
    "MUT_2": ["B2", "B4", "B6", "B8", "B10", "B12"],
    "WT_3": ["C1", "C3", "C5", "C7", "C9", "C11"],
    "MUT_3": ["C2", "C4", "C6", "C8", "C10", "C12"]
})
```
To better explain, in this tab, the experimenters carried out an experiment with Wild Type (`WT`) bacteria, but changed their environments (A1, B1, C1), so they carried out the same experiment with other bacteria to verify the results. Basically, we'd made replicates.
The same applies to the mutants (`MUT`) : they were subjected to different environments, and replicates were also made.
So, the main reason for this project is to compare mutants and wt, and find out if there are any differences.

---
## I. Functions
As We said earlier, these functions have already been used in Stage 1, the HackBio course, but it's the way they're used that's distinctive.
### *1st Function*
The main purpose of this function : is to convert raw data into a structure that is easier to analyze and plot.
                                   
