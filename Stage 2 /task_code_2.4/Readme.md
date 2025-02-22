**# **Analysis of deleterious protein mutations** 

### Team members:
*Chama Benslimane (leader)* ; GitHub profile : https://github.com/BenslimaneChama
and
*Mohammad Hicham Polo* ; GitHub profile : https://github.com/MohammadHichamPolo
**HackBio Internship - Stage 2 Task**

---
## **Introduction**
This project enables us to analyze deleterious protein mutations, merging SIFT & FoldX data and visualizing impacted amino acids. The aim is therefore to merge two sets of biological data, to identify mutations that destabilize proteins, and also to visualize the frequency of amino acids involved in these mutations.<br/>
<br/>
`SIFT` and `FoldX` are data sets used to analyze the effect of mutations on proteins:
SIFT Score: predicts whether a mutation is tolerable or deleterious (score < 0.05 = deleterious mutation).<br/>
<br/>
FoldX Score: assesses the effect of a mutation on protein stability (score > 2 = structural instability).<br/>
## **Modules Needed**
```
import pandas as pd
import requests
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns
```
`pandas` is used for dataframe manipulation
`requests` to download online data
`stringIO` for confverting texts to an exploitable file from pandas
`matplotlib.pyplot` and seaborn for graphic creation in order to visualise the results

## **Data Importation**
We download the SIFT file from a Github link, retrieving its raw response.text content, then converting it into a pandas dataframe by reading a .tsv file (tab as separator).
```
sift_url = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv"
response = requests.get(sift_url)
raw_data = response.text
sift_df = pd.read_csv(StringIO(raw_data), delimiter=r"\s+", engine="python")
```
We repeat the same processus for FoldX file :
```
foldx_url = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv"
response = requests.get(foldx_url)
raw_data = response.text
foldx_df = pd.read_csv(StringIO(raw_data), delimiter=r"\s+", engine="python")
```

## **Creating a key column** 
Here, we create a new column called `specific_Protein_aa` by concatenating `(+)` : 
     - Protein name
     - Amino acid mutation
```
sift_df["specific_Protein_aa"] = sift_df["Protein"] + "_" + sift_df["Amino_Acid"]
foldx_df["specific_Protein_aa"] = foldx_df["Protein"] + "_" + foldx_df["Amino_Acid"]
```

## **Merging the two datasets** 
We delete the Protein and Amino_Acid columns in FoldX (as they are already present in SIFT), then merge the two datasets using the specific_Protein_aa column as the key.
```
foldx_dataframe_clean = foldx_df.drop(columns=['Protein', 'Amino_Acid'])
final_dataframe = pd.merge(sift_df, foldx_dataframe_clean, on='specific_Protein_aa')
```

## **Identification of deleterious mutations**
In this step, we filter out mutations with : 
  - A SIFT Score < 0.05 (harmful mutation).
  - FoldX Score > 2 (protein destabilization).
```
deleterious_mutations = final_dataframe[(final_dataframe['sift_Score'] < 0.05) & (final_dataframe['foldX_Score'] > 2)]
```

## **Identification of the amino acids most affected**
We extract the first character in the Amino_Acid to identify the original amino acid, and count how many times each amino acid has been mutated value_counts(). Then rename the columns and sort the results.

## **Results Visualisation**

First, we generate a barplot of the most frequent amino acid mutations: 
<br/>
```
plt.figure(figsize=(10, 6))
sns.barplot(data=frequency_table, x='Original_Amino_Acid', y='Frequency', palette='viridis')
plt.title('Frequency of Original Amino Acids')
plt.xlabel('Amino Acid')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
```
![Frequency of Original Amino Acids](/figures/barplot_AA.png)
<br/>
A pie chart is then produced to see which mutations are most frequent.
<br/>
```
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(frequency_table['Frequency'], labels=frequency_table['Original_Amino_Acid'], autopct='%.1f%%', startangle=90, colors=sns.color_palette('tab20b'))
plt.title('Proportion of Original Amino Acids', fontsize=14)
plt.show()
```
![Proportion of Original Amino Acids](/figures/piechart_AA.png)
