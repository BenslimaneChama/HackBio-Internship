'''
Stage 2 raw code - HackBio Internship

This code contains a problem-solving script developed by our team for the Stage 2 task_code_2.6 in the HackBio internship:
- Chama BENSLIMANE (Leader): https://github.com/BenslimaneChama
- Mohammad HICHAM POLO : https://github.com/MohammadHichamPolo
The script generates volcano plots based on the dataset given and finds the top 5 genes that are upregulated and downregulted.
For better visualisation and understanding of interpretation, check the Readme file.

Stage 2 GitHub Repository: https://github.com/BenslimaneChama/HackBio-Internship/tree/main/Stage%202%20
Task_code_2.6 Github Repository: https://github.com/BenslimaneChama/HackBio-Internship/tree/main/Stage%202%20/task_code_2.6
Plots images Github Repository : https://github.com/BenslimaneChama/HackBio-Internship/tree/main/Stage%202%20/task_code_2.6/figures

LinkedIn Video: STILL
'''
#___________________________________________________________________________________________________________________________________________
# Required Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from io import StringIO
#___________________________________________________________________________________________________________________________________________
# Importing the data and dealing with the column issue
url = "https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt"
response = requests.get(url)
data = response.text
df = pd.read_csv(StringIO(data), delimiter=r"\s+", engine="python")
#___________________________________________________________________________________________________________________________________________
# Creating a new variable that contains the -log10 of df p-values
df['neg_log_pvalue'] = -np.log10(df['pvalue'])
#___________________________________________________________________________________________________________________________________________
# VOLCANO PLOT RESPECTING THE THRESHOLD
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

# Add thresholds
plt.axvline(-1, color='gray', linestyle='--')
plt.axvline(1, color='gray', linestyle='--')
plt.axhline(-np.log10(0.01), color='gray', linestyle='--')

plt.title('Volcano Plot of Differential Expression', fontsize=14)
plt.xlabel('log2 Fold Change', fontsize=12)
plt.ylabel('-log10(p-value)', fontsize=12)
plt.legend(title='Regulation', loc='upper right')
plt.show()
#___________________________________________________________________________________________________________________________________________
# Selecting only significant regulations (up and down) respecting the threshold put in the graph
upregulated = df[(df['log2FoldChange'] > 1) & (df['pvalue'] < 0.01)]
downregulated = df[(df['log2FoldChange'] < -1) & (df['pvalue'] < 0.01)]
# Selecting the top 5 genes having the higher log2FoldChange in selected up and down regulated genes
top5_up = upregulated.nlargest(5, 'log2FoldChange')
top5_down = downregulated.nsmallest(5, 'log2FoldChange')
# Displaying these top 5 genes for the 2 sides of regulation 
print("\nTop 5 Upregulated Genes:")
print(top5_up[['Gene', 'log2FoldChange', 'pvalue']].to_string(index=False))

print("\nTop 5 Downregulated Genes:")
print(top5_down[['Gene', 'log2FoldChange', 'pvalue']].to_string(index=False))
'''
OUTPUT:
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

CONCLUDING GENE FUNCTION FROM GENECARD : 
Top 5 Upregulated Genes Functions:
DTHD1   :This gene encodes a protein which contains a death domain. Death domain-containing proteins function in signaling pathways and formation of signaling complexes, as well as the apoptosis pathway.
EMILIN2 :Predicted to enable extracellular matrix constituent conferring elasticity. Involved in several processes, including positive regulation of angiogenesis; positive regulation of defense response to bacterium; and positive regulation of platelet aggregation. Located in extracellular region. 
PI16    :Predicted to enable peptidase inhibitor activity. Predicted to be involved in negative regulation of peptidase activity. Predicted to act upstream of or within negative regulation of cell growth involved in cardiac muscle cell development. Predicted to be located in extracellular region. Predicted to be active in extracellular space
C4orf45 :SPMIP2 (Sperm Microtubule Inner Protein 2) is a Protein Coding gene. Diseases associated with SPMIP2 include Hyperekplexia.
FAM180B :Predicted to be located in extracellular region enabling protein bindings.
Top 5 Downregulated Genes Functions:
TBX5    :his gene is a member of a phylogenetically conserved family of genes that share a common DNA-binding domain, the T-box. T-box genes encode transcription factors involved in the regulation of developmental processes. This gene is closely linked to related family member T-box 3 (ulnar mammary syndrome) on human chromosome 12. The encoded protein may play a role in heart development and specification of limb identity. Mutations in this gene have been associated with Holt-Oram syndrome, a developmental disorder affecting the heart and upper limbs. Several transcript variants encoding different isoforms have been described for this gene.
IFITM1  :Interferon-induced transmembrane (IFITM) proteins are a family of interferon induced antiviral proteins. The family contains five members, including IFITM1, IFITM2 and IFITM3 that belong to the CD225 superfamily. The protein encoded by this gene restricts cellular entry by diverse viral pathogens, such as influenza A virus, Ebola virus and Sars-CoV-2. 
TNN     :Predicted to enable integrin binding activity. Involved in positive regulation of sprouting angiogenesis; regulation of cell adhesion; and regulation of cell migration. Part of tenascin complex.
COL13A1 :This gene encodes the alpha chain of one of the nonfibrillar collagens. The function of this gene product is not known, however, it has been detected at low levels in all connective tissue-producing cells so it may serve a general function in connective tissues. Unlike most of the collagens, which are secreted into the extracellular matrix, collagen XIII contains a transmembrane domain and the protein has been localized to the plasma membrane. The transcripts for this gene undergo complex and extensive splicing involving at least eight exons. Like other collagens, collagen XIII is a trimer; it is not known whether this trimer is composed of one or more than one alpha chain isomer. A number of alternatively spliced transcript variants have been described, but the full length nature of some of them has not been determined. 
IFITM3  :nterferon-induced transmembrane (IFITM) proteins are a family of interferon induced antiviral proteins. The family contains five members, including IFITM1, IFITM2 and IFITM3 and belong to the CD225 superfamily. The protein encoded by this gene restricts cellular entry by diverse viral pathogens, such as influenza A virus, Ebola virus and Sars-CoV-2. 
'''
#___________________________________________________________________________________________________________________________________________
# USING top5_up and top5_down dataframes we could add the names of these genes to the plot keeping the same code: 
# VOLCANO PLOT WITH TOP 5 DOWN ADN UP REGULATED GENES NAMES DISPLAYES IN THE CORRESPONDING DATA POINT:
lt.figure(figsize=(10, 6))
sns.scatterplot(data=df, 
                x='log2FoldChange', 
                y='neg_log_pvalue',
                hue=np.where((df['log2FoldChange'].abs() > 1) & (df['pvalue'] < 0.01), 
                              np.where(df['log2FoldChange'] > 1, 'Up', 'Down'), 
                              'NS'),
                palette={'Up': 'red', 'Down': 'blue', 'NS': 'gray'},
                alpha=0.7,
                s=40)

# Add thresholds
plt.axvline(-1, color='gray', linestyle='--')
plt.axvline(1, color='gray', linestyle='--')
plt.axhline(-np.log10(0.01), color='gray', linestyle='--')

plt.title('Volcano Plot of Differential Expression', fontsize=14)
plt.xlabel('log2 Fold Change', fontsize=12)
plt.ylabel('-log10(p-value)', fontsize=12)
plt.legend(title='Regulation', loc='upper right')

#Add labels for top 5 genes
for _, row in pd.concat([top5_up, top5_down]).iterrows():
    plt.text(row['log2FoldChange'], row['neg_log_pvalue'], row['Gene'], 
             fontsize=8, alpha=0.7)

plt.show()
#___________________________________________________________________________________________________________________________________________
'''
FINAL INTERPRETATION :
Upregulated genes suggest increased extracellular matrix remodeling, apoptosis, and cardiovascular regulation.
Downregulated genes point to reduced antiviral response, altered developmental pathways, and potential connective tissue or cardiac implications.
If linked to a specific disease or condition, this pattern might indicate a response to infection, tissue repair mechanisms, or developmental disturbances.
'''
