# **Project Title : Exploring Python Functions at Stage 1**
### Team Members :
*Chama Benslimane (leader)* ; GitHub profile : https://github.com/BenslimaneChama
and
*Mohammad Hicham Polo* ; GitHub profile : https://github.com/MohammadHichamPolo
**HackBio Internship - Stage 1 Task**
## Introduction : What's a Python Function 
A functions is a block of code, that only runs when it's called. We can Pass data, known as parameters. A function return data as a parameter. Without a function, we only have a long list of code, so it really help us organize codes, and also can be reusable. 
## Project Description 
In this task, we made four functions for the following objectives:
1. **Analyzing DNA sequences (in a FASTA file) and translating them into amino acid sequences**
2. **Generating bacterial growth curves and simationg it's different phases**
3. **Determinate the density value at 80% of a growth curve**
4. **Calculating the hamming distance between two chains of characters**
## 1st Function : Analyzing a FASTA file abd DNA traduction
This project contains a Python script that allow us to analyze DNA sequences from a FASTA file. It calculates the nucletides composition, the CG content, and translates into RNA and Amino Acids. 
### Functionnalities
- Reading and extracting DNA sequence from a FASTA file.
- Calculating the nucleotids frequence (A,T,C,G)
- Determinating CG percentage.
- Transcription of DNA sequence into RNA
- Translation of RNA into Amino
### Function parameters
In this function, we needed two parameters : 
      `file_location`, which let us open the fasta file that we inputted, and the `strand_type`.
```
def analyze_fasta(file_location,strand_type):
```
### Inputs
- A FASTA file containing a DNA sequence with it's header
- Specify whether the `strand_type`, we have two types of stand type : 
   * "Forward" for the direct translation
   *  "Reverse" for RNA transcription
```
intry example :
analyze_fasta("path/to/fasta.file", "forward")
```
### Outputs
The script shows : The header of FASTA file, the nucletide count, CG_content percentage, and the Translated amino acid sequence
```
FASTA Analysis Results
----------------------
Header: >Sequence1

Nucleotide Counts:
  A: 30
  T: 25
  C: 20
  G: 25

CG Content: 45.00%

Amino Acid Sequences:
  Sequence 1: MFTYAG
```
 

## 2nd Function : Simulationg Bacterial Growth
this project allow us to creat curves that represent the various stages of a bacterial population's development, it simulates bacterial growth. This enables us to animate this evolution over time and visualize those curves on a logarithmic scale. This project is very useful for modeling or conducting research on bacterial proliferation.
### Functionnalities
- Generating multiple growth curves
- Visualization of data in logarithmic scale
- Animating the bacterial growth
### Libraries needed 
In the following, the libraries needed in order to execute our code in python : 
```
pip install pandas matplotlib numpy
```
### Function parameters
In this fonction, we needed 5 parameters, that we are going to expain each of them :
  - `unit_type` (str) : It's for the time unit, whether it's on 's', 'min', or 'h'
  - `time_period` (int) : The total period
  - `col_number` (int) : The number of temporale points
  - `raw_numbers` (int) : The number of growth curves that I want to generate
  - `starting_point` (float) : The initial nuber of cells.
  - `expo_start` (int) : This one is optional, we may or not indicate the beginning of the exponential phase.
  - `expo_end` (int) : This one too is optional, we may or not indicate the end of the exponential phase
```
def generate_growth_curves(unit_type, time_period, col_numbers, raw_numbers, starting_point, expo_start=None, expo_end=None):
```
### Inmput
For the input, you fill in the details of what you want, all the parameters needed and required to generate the curve(s).
For example :
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

data = generate_growth_curves('min', 120, 50, 3, 10)
```
### Output 
After execution, the first lines of the output will be as following, and of course, it'll be a curve, as many as we wanted 
```
       0      1      2      3      4  ...
0   10.0   10.0   12.0   14.4   17.3  ...
1   10.0   10.0   11.5   13.8   16.5  ...
2   10.0   10.0   12.2   14.6   17.8  ...
```
### Phases Explanation 
- **Latency phase** : The bacterias do not divide, they are trying to adapt to their envirenment (in the curve, we only see a stable line)
- **Exponential phase** : Rapid population growth
- **Stationary phase** : Nutrients are lacking, which results a slow growth (again a stable line)
- **Decline phase** : Population declines, due to death
## 3rd function : Calculation of density at 80% of max value 
This Function allow us to deteminate the moment where the bacterial density reaches 80% of it's maximal value from it's growth curve.
This function is independant and at the same time, compatible with function 2. 
### Libraries needed
```
import pandas as pd
```
### Function Parameters 
This function has two parameters that we are going to define : 
  - `data` : it's a dataframe that represents bacterial growth that we have to import, or generate it
  - `time_set` : It's a time interval between measurements, by default, it's 1.
```
def find_80_percent_density(data, time_step=1):
```
### Import
What we have to import here / or to generate is the dataframe, that from it, we are going to calculate the 80% of density in the bacterial growth
```
#Example of input, generating dataframe 
data = pd.DataFrame({
    0: [0.1, 0.2, 0.3],  # Densité à t=0
    1: [0.4, 0.6, 0.8],  # Densité à t=1
    2: [0.9, 1.0, 1.2],  # Densité à t=2
})
```
### Output
Normally, we should have had 3 ouputs : 
- `max_density`
- `time_80_percent`
- `density_at_80`
However, we only had one, and that's because in the return we only asked for one
```
   return max_density, None, None
```
So here is an example of the input
```
Densité max: 1.0
```
## 4th Function :  Calculates the hamming distance between two chains of characters
This function calculates the Hamming distance between two chains of characters, that has the SAME length. The Hamming distance means the number of positions where the characters on the two strings differ.
### Functionnalities 
  - We input two chains of characters
  - This function verfies is the inputs are on the same lenth (else it won't work)
  - Compare the characters
  - Gives us the distance
### Function Parameters 
This Function has Two parameters :
    - `slack_username` : First chain of character 
    - `X_username` : Second chain of character 
```
def hamming_distance(slack_username, X_username):
```
