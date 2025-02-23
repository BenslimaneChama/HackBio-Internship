# **Code Analysis: Volcano Plot Generation and Identification of Differentially Regulated Genes**

### Team members:
*Chama Benslimane (leader)* ; GitHub profile : https://github.com/BenslimaneChama
and
*Mohammad Hicham Polo* ; GitHub profile : https://github.com/MohammadHichamPolo
**HackBio Internship - Stage 2 Task**

---
## **Introduction**
This python project was developed as part of the HackBio Internship, stage 2. Its main objective is to generate a volcano plot based on a given dataset and identify the top 5 most overexpressed (upregulated) and underexpressed (downregulated) genes.<br/>
<br/>
A volcano plot : is a graphic representation commonly used in genomic analysis. It displays statistical significance (via the p-value) as a function of the level of expression change (log2 fold change).<br/>
This makes it possible to identify the genes most significantly regulated between two experimental conditions.
<br/>
## **Modules needed**
That is all the librarys needed for the treatment of data and visualisation 
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from io import StringIO
```

- `pandas` for data manipulations as a DataFrame.
- `numpy` for mathematical calculation
- `matplotlib.pyplot` & `seaborn`  for plots generations
- `requests` to dowloas datas from an extern URL
- `StringIO` to convert a text into a readable format with `pandas.read_csv()`


## **Importing the data**
We import the url, which already contains the text file containing the results of a differential gene expression analysis, then download the file and store its contents as plain text. This text will then be converted into a format that can be used by `pandas`.
<br/>
```
url = "https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt"
response = requests.get(url)
data = response.text
df = pd.read_csv(StringIO(data), delimiter=r"\s+", engine="python")
```

## **-log10(p-value)**

p-value, indicates the statistical significance of a gene, but volcano plot often uses `log10(p-value)` to better distinguish significant genes. As a result, p-value is very small in comparison (e.g. `p-value = 0.00001`), but after transformation, these values will become large. This makes it easier to identify statistically significant genes.

```
df['neg_log_pvalue'] = -np.log10(df['pvalue'])
```

## Creating Volcano Plot
with `seaborn.scatterplot()` <br/>
<br/>
We add the condition that if a gene changes expression by more than a factor of 2 (log2FoldChange > 1 or < -1) and p-value < 0.01, it is considered significant.<br/>
<br/>
“Up” in red (overexpressed).<br/>
“Down” in blue (underexpressed).<br/>
“NS” (non-significant) in grey.<br/>
<br/>
```
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, 
                x='log2FoldChange', 
                y='neg_log_pvalue',
                hue=np.where((df['log2FoldChange'].abs() > 1) & (df['pvalue'] < 0.01), 
                              np.where(df['log2FoldChange'] > 1, 'Up', 'Down'), 
                              'NS'),
                palette={'Up': 'red', 'Down': 'blue', 'NS': 'gray'},
                alpha=0.7,
                s=40)
```

We add visual threshold, to identify sigificative genes.
- Upregulated : log2FoldChange > 1 et p-value < 0.01.
- Downregulated : log2FoldChange < -1 et p-value < 0.01.
```
plt.axvline(-1, color='gray', linestyle='--')
plt.axvline(1, color='gray', linestyle='--')
plt.axhline(-np.log10(0.01), color='gray', linestyle='--')

plt.title('Volcano Plot of Differential Expression', fontsize=14)
plt.xlabel('log2 Fold Change', fontsize=12)
plt.ylabel('-log10(p-value)', fontsize=12)
plt.legend(title='Regulation', loc='upper right')
plt.show()
```
Once the thresholds have been set, the volcano plot looks like this: 

![Volcano Plot of Differential Expression](figures/simple_volcano_plot.png)

Now, from all the data we have, we're going to choose the 5 most expressed genes, and the 5 least expressed.

```
top5_up = upregulated.nlargest(5, 'log2FoldChange')
top5_down = downregulated.nsmallest(5, 'log2FoldChange')
```

We then print the results, displaying the top 5 genes (Up & Down) with their log2FoldChange and p-value.
```
#Output
Top 5 Upregulated Genes:

   Gene  log2FoldChange       pvalue
  DTHD1           1.540     0.000056
EMILIN2           1.534     0.000003
   PI16           1.495     0.000130
C4orf45           1.288     0.000247
FAM180B           1.249     0.001146

Top 5 Downregulated Genes:

   Gene  log2FoldChange       pvalue
   TBX5          -2.129     5.655000e-08
 IFITM1          -1.687     3.735000e-06
    TNN          -1.658     8.973000e-06
COL13A1          -1.647     1.394000e-05
 IFITM3          -1.610     1.202000e-05
```

 
In the last step, we add their names to the top 5 genes, whether up or down, for easier visualization. 
```
for _, row in pd.concat([top5_up, top5_down]).iterrows():
    plt.text(row['log2FoldChange'], row['neg_log_pvalue'], row['Gene'], 
             fontsize=8, alpha=0.7)

plt.show()
```

![Volcano Plot of Differential Expression](figures/volcano_plot_with_top5.png)

## **Conclusind gene function from `Genecard`** 

### **Top 5 Upregulated Genes Functions:** 

`DTHD1`   :This gene encodes a protein which contains a death domain. Death domain-containing proteins function in signaling pathways and formation of signaling complexes, as well as the apoptosis pathway.
<br/>
<br/>
`EMILIN2` :Predicted to enable extracellular matrix constituent conferring elasticity. Involved in several processes, including positive regulation of angiogenesis; positive regulation of defense response to bacterium; and positive regulation of platelet aggregation. Located in extracellular region. <br/>
<br/>
`PI16 `   :Predicted to enable peptidase inhibitor activity. Predicted to be involved in negative regulation of peptidase activity. Predicted to act upstream of or within negative regulation of cell growth involved in cardiac muscle cell development. Predicted to be located in extracellular region. Predicted to be active in extracellular space<br/>
<br/>
`C4orf45 `:SPMIP2 (Sperm Microtubule Inner Protein 2) is a Protein Coding gene. Diseases associated with SPMIP2 include Hyperekplexia.<br/>
<br/>
`FAM180B` :Predicted to be located in extracellular region enabling protein bindings.
<br/>
<br/>
### **Top 5 Downregulated Genes Functions:**

`TBX5`    :his gene is a member of a phylogenetically conserved family of genes that share a common DNA-binding domain, the T-box. T-box genes encode transcription factors involved in the regulation of developmental processes. This gene is closely linked to related family member T-box 3 (ulnar mammary syndrome) on human chromosome 12. The encoded protein may play a role in heart development and specification of limb identity. Mutations in this gene have been associated with Holt-Oram syndrome, a developmental disorder affecting the heart and upper limbs. Several transcript variants encoding different isoforms have been described for this gene.<br/>
<br/>
`IFITM1`  :Interferon-induced transmembrane (IFITM) proteins are a family of interferon induced antiviral proteins. The family contains five members, including IFITM1, IFITM2 and IFITM3 that belong to the CD225 superfamily. The protein encoded by this gene restricts cellular entry by diverse viral pathogens, such as influenza A virus, Ebola virus and Sars-CoV-2. 
`TNN  `   :Predicted to enable integrin binding activity. Involved in positive regulation of sprouting angiogenesis; regulation of cell adhesion; and regulation of cell migration. Part of tenascin complex. <br/>
<br/>
`COL13A1` :This gene encodes the alpha chain of one of the nonfibrillar collagens. The function of this gene product is not known, however, it has been detected at low levels in all connective tissue-producing cells so it may serve a general function in connective tissues. Unlike most of the collagens, which are secreted into the extracellular matrix, collagen XIII contains a transmembrane domain and the protein has been localized to the plasma membrane. The transcripts for this gene undergo complex and extensive splicing involving at least eight exons. Like other collagens, collagen XIII is a trimer; it is not known whether this trimer is composed of one or more than one alpha chain isomer. A number of alternatively spliced transcript variants have been described, but the full length nature of some of them has not been determined. <br/>
<br/>
`IFITM3 ` :nterferon-induced transmembrane (IFITM) proteins are a family of interferon induced antiviral proteins. The family contains five members, including IFITM1, IFITM2 and IFITM3 and belong to the CD225 superfamily. The protein encoded by this gene restricts cellular entry by diverse viral pathogens, such as influenza A virus, Ebola virus and Sars-CoV-2. <br/>
<br/>
## **FINAL INTERPRETATION :**
Upregulated genes suggest increased extracellular matrix remodeling, apoptosis, and cardiovascular regulation.
Downregulated genes point to reduced antiviral response, altered developmental pathways, and potential connective tissue or cardiac implications.
If linked to a specific disease or condition, this pattern might indicate a response to infection, tissue repair mechanisms, or developmental disturbances.
