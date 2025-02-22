"""
Stage 2 raw code - HackBio Internship

This code contains functions developed by our team for the Stage 2 Microbiology task in the HackBio internship:
- Chama BENSLIMANE (Leader): https://github.com/BenslimaneChama
- Mohammad HICHAM POLO : https://github.com/MohammadHichamPolo
It includes functions that manipulates the given datas (general data and metadata), and including the FUNCTION3 from stage 1 determining 80% density values.
Interpretation of biostatisticall analysis is Included as comments in the code
Interpretation of Plots is included in Readme file.

Stage 2 GitHub Repository: https://github.com/BenslimaneChama/HackBio-Internship/tree/main/Stage%202%20
Task 1 code Github Repository: https://github.com/BenslimaneChama/HackBio-Internship/tree/main/Stage%202%20/task1
Plost images Github Repository : https://github.com/BenslimaneChama/HackBio-Internship/tree/main/Stage%202%20/task1/figures

LinkedIn Video: STILL
"""
#___________________________________________________________________________________________________________________________________________
# Required Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
#___________________________________________________________________________________________________________________________________________
# Importing data and creating metadata
data = pd.read_csv("mcgc.tsv",  sep='\t')
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
#___________________________________________________________________________________________________________________________________________
# Required functions (FUNCTION3 FROM STAGE1 INCLUDED) : 
# Pivoting data structure so that it can match function 3 when it's time to use : 
"""
    This function converts a DataFrame where columns are curves and rows are time points
    into a structure where rows are curves and columns are time points.

    Args:
        df (pd.DataFrame): Input DataFrame with 'time' column and curve columns (e.g., A1, A2, B1, etc.).

    Returns:
        tuple: 
            - pd.DataFrame: Transposed data with curves as rows and time as columns.
            - np.ndarray: Time values extracted from the 'time' column (used for x-axis in plots).
"""
def convert_to_curve_time_structure(data):
    if 'time' not in data.columns:
        raise ValueError("Input DataFrame must contain a 'time' column.")
    
    # Set 'time' as the index and transpose the DataFrame
    df_time_indexed = data.set_index('time')
    transposed_data = df_time_indexed.transpose()
    
    # Extract time values for plotting
    x_values = data['time'].values
    
    return transposed_data, x_values

# Melting the metadata dataframe so that it can be compatible to the actual data structure
"""This function converts the wide-format metadata to a long-format DataFrame"""
def process_metadata(metadata_df):
    melted = []
    
    for _, row in metadata_df.iterrows():
        strain_rep = row['Strain']
        strain, rep = strain_rep.split('_')
        
        # Process each experiment pair (WT_1/MUT_1, WT_2/MUT_2, etc.)
        for exp_num in [1, 2, 3]:
            wt_col = f'WT_{exp_num}'
            mut_col = f'MUT_{exp_num}'
            
            melted.extend([
                {
                    'curve_id': row[wt_col],
                    'strain': strain,
                    'rep': rep,
                    'type': 'WT',
                    'experiment': exp_num
                },
                {
                    'curve_id': row[mut_col],
                    'strain': strain,
                    'rep': rep,
                    'type': 'MUT',
                    'experiment': exp_num
                }
            ])
    
    return pd.DataFrame(melted)
# We used the same logic we plotted with using FUNCTION2 (not FUNCTION3)in stage 1 
""" This function plots growth curves with improved layout and main title defined by users chosen time unit"""

def plot_strain_curves(converted_data, x_values, unit_type="min"):
    # Process metadata
    curve_metadata = process_metadata(metadata)
    
    # Create 3 plots in one line with adjusted spacing
    fig, axs = plt.subplots(1, 3, figsize=(22, 7))
    fig.subplots_adjust(top=0.85, bottom=0.35, wspace=0.35)
    
    # Main title
    fig.suptitle('OD600 evolution over time by replicate type between WT and MUT in the different strain type', 
                y=1, fontsize=16, fontweight='bold')
    
    # Create plot settings
    type_colors = {'WT': '#2ecc71', 'MUT': '#e74c3c'}  # Green/Red
    rep_styles = {'Rep1': '-', 'Rep2': '--'}  # Solid/Dashed
    
    # Legend elements
    legend_elements = [
        plt.Line2D([0], [0], color=type_colors['WT'], ls=rep_styles['Rep1'], lw=2,
                   label='WT (Rep1)'),
        plt.Line2D([0], [0], color=type_colors['WT'], ls=rep_styles['Rep2'], lw=2,
                   label='WT (Rep2)'),
        plt.Line2D([0], [0], color=type_colors['MUT'], ls=rep_styles['Rep1'], lw=2,
                   label='MUT (Rep1)'),
        plt.Line2D([0], [0], color=type_colors['MUT'], ls=rep_styles['Rep2'], lw=2,
                   label='MUT (Rep2)')
    ]
    
    # Plot each strain
    for idx, strain in enumerate(sorted(curve_metadata['strain'].unique())):
        ax = axs[idx]
        ax.set_title(f"{strain}", fontsize=14, pad=15)
        ax.set_xlabel(f"Time ({'hours' if unit_type == 'h' else 'minutes' if unit_type == 'min' else 'seconds'})", fontsize=12)
        ax.set_ylabel("OD600 (log scale)", fontsize=12)
        ax.set_yscale('log')
        
        strain_data = curve_metadata[curve_metadata['strain'] == strain]
        
        for _, row in strain_data.iterrows():
            ax.plot(
                x_values,
                converted_data.loc[row['curve_id']],
                color=type_colors[row['type']],
                linestyle=rep_styles[row['rep']],
                linewidth=1.5
            )
        
        # Adjusting limits of titles
        y_min = converted_data.loc[strain_data['curve_id']].min().min()
        y_max = converted_data.loc[strain_data['curve_id']].max().max()
        ax.set_ylim(y_min * 0.5, y_max * 2)
        ax.tick_params(axis='both', labelsize=10)
    
    # Adding legend
    fig.legend(handles=legend_elements, 
              loc='lower center',
              ncol=4, 
              fontsize=12,
              frameon=False,
              bbox_to_anchor=(0.5, -0.07))  
    
    plt.tight_layout()
    plt.show()
# THE FUNCTION3 FROM STAGE 1 THAT WE USED TO CALCULATE THE 80% OF MAX OD WITH ITS CORRESPONDING TIME RECORD ;)
"""
    Determines the time point where the bacterial density reaches 80% of the maximum value.

    Parameters:
    data (pd.DataFrame): DataFrame representing bacterial growth.
    time_step (int, optional): Time interval between measurements. Default is 1.

    Returns:
    float: Time at which 80% of maximum density is reached.
"""
def find_80_percent_density(data, time_step=1):
    max_density = data.max().max()
    
    threshold = 0.8 * max_density
    
    for col in data.columns:
        if (data[col] >= threshold).any():
            time_80_percent = int(col) * time_step  
            density_at_80 = data[col].max() 
            return max_density, time_80_percent, density_at_80
    
    return max_density, None, None 
#___________________________________________________________________________________________________________________________________________
# THE MAIN CODE TO EXECUTE THE REQUIRED TASKS
#___________________________________________________________________________________________________________________________________________
# converting the data to match the wanted structure
converted_data, x_values = convert_to_curve_time_structure(data)
#___________________________________________________________________________________________________________________________________________
# ploting all the growth curves of OD600 vs Time for the different Strains respecting the proposed instructions
plot_strain_curves(converted_data, x_values, unit_type='min')
#___________________________________________________________________________________________________________________________________________
# EXTRACTING THE TIME TO REACH 80% OF MAXIMUM OD AND ORGANIZING IT INTO results_df
results = []
for curve_id in converted_data.index:
    # Get curve data and ensure proper formatting
    curve_data = pd.DataFrame(converted_data.loc[curve_id]).transpose()
    
    # Convert columns to integers
    curve_data.columns = curve_data.columns.astype(int)
    
    # Analyze curve
    max_dens, time_80, dens_80 = find_80_percent_density(curve_data, time_step=1)
    
    results.append({
        'curve_id': curve_id,
        'max_density': max_dens,
        'time_to_80%': time_80,
        'density_at_80%': dens_80
    })

results_df = pd.DataFrame(results)
#___________________________________________________________________________________________________________________________________________
# PROCESSING METADATA SO THAT WE MELT IT AND CAN BE MERGED WITH results_df
# Create full metadata mapping
curve_metadata = process_metadata(metadata)

# Merge with your results
results_df = results_df.merge(curve_metadata[['curve_id', 'strain', 'type']], on='curve_id')
#___________________________________________________________________________________________________________________________________________
# GENERATING THE SCATTER PLOT OF THE TIME IT TAKES TO REACH CARRYING CAPACITY FOR THE MUT AND THE WT IN THE DIFFERENT STRAINS
# Create the plot with proper strain labels
plt.figure(figsize=(14, 8))

# Style mappings
color_map = {'WT': '#2ecc71', 'MUT': '#e74c3c'}  # Green/Red
marker_map = {'Strain1': 'o', 'Strain2': 's', 'Strain3': '^'}  # Circle/Square/Triangle

# Plot each strain-type combination
for strain in ['Strain1', 'Strain2', 'Strain3']:
    for t in ['WT', 'MUT']:
        subset = results_df[(results_df['strain'] == strain) & (results_df['type'] == t)]
        if not subset.empty:
            plt.scatter(
                subset['time_to_80%'],
                subset['density_at_80%'],
                c=color_map[t],
                marker=marker_map[strain],
                s=150,
                edgecolor='w',
                alpha=0.9,
                label=f'{strain} {t}'
            )

# Add plot elements
plt.title('Time to 80% Carrying Capacity by Strain and Type', fontsize=14)
plt.xlabel('Time (minutes)', fontsize=12)
plt.ylabel('density_at_80%', fontsize=12)  
plt.grid(alpha=0.2)


handles = []
for strain in ['Strain1', 'Strain2', 'Strain3']:
    for t in ['WT', 'MUT']:
        handles.append(plt.Line2D(
            [0], [0], 
            marker=marker_map[strain],
            color=color_map[t],
            linestyle='',
            markersize=10,
            label=f'{strain} {t}'
        ))

plt.legend(
    handles=handles,
    title='Strain/Type',
    bbox_to_anchor=(1.05, 1),
    loc='upper left',
    frameon=False,
    fontsize=10
)

plt.tight_layout()
plt.show()
#___________________________________________________________________________________________________________________________________________
# GENERATING THE BOXPLOT THAT SHOWS THE TIMES IT TAKES TO REACH CARRYING CAPACITY FOR THE MUT AND THE WT IN THE DIFFERENT STRAINS
# Filter and aggregate data across strains
valid_df = results_df.dropna(subset=['time_to_80%'])
agg_df = valid_df.groupby(['type', 'strain'])['time_to_80%'].mean().reset_index()

# PLOTTING STARTS HERE
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid", font_scale=1.1)
palette = {'WT': '#2ecc71', 'MUT': '#e74c3c'}

ax = sns.boxplot(
    x='strain',
    y='time_to_80%',
    hue='type',
    data=valid_df,
    palette=palette,
    width=0.7,
    linewidth=1.5
)

plt.title('Time to Reach Carrying Capacity\nby Strain and Mutation Type', pad=20)
plt.xlabel('Strain', labelpad=15)
plt.ylabel('Time (minutes)', labelpad=15)
plt.legend(title='Mutation Type', frameon=False)
sns.despine()
plt.tight_layout()
plt.show()
#___________________________________________________________________________________________________________________________________________
#STATISTICAL ANALYSIS USING MANN-WITHNEY U TEST BECAUSE BASED ON THE DATA WE HAVE LESS THAN 30 RECORDS BY STRAIN
#___________________________________________________________________________________________________________________________________________
#STATISTICAL ANALYSIS BETWEEN MUT AND WT IN GENERAL
# Extract WT and MUT times
wt_times = valid_df[valid_df['type'] == 'WT']['time_to_80%']
mut_times = valid_df[valid_df['type'] == 'MUT']['time_to_80%']

# Perform Mann-Whitney U test
stat, p_value = stats.mannwhitneyu(wt_times, mut_times)

# Compute means
wt_mean = np.mean(wt_times)
mut_mean = np.mean(mut_times)

# Output results
print(f"W statistic: {stat:.2f}")
print(f"P-value: {p_value:.3f}")
print(f"WT Mean Time: {wt_mean:.2f} min")
print(f"MUT Mean Time: {mut_mean:.2f} min")
'''
OUTPUT :
W statistic: 171.50
P-value: 0.775
WT Mean Time: 663.33 min
MUT Mean Time: 644.17 min
'''
'''
INTERPRETATION :
Based on the biostatisticall results we can conclude that, generally, there is no significant difference between mutants and wild-type, in
terms of OD recorded, because P-values is superior than 0,05.
Meaning that the knockout manipulation didn't affect the growth of the bacteria.
'''
#___________________________________________________________________________________________________________________________________________
#STATISTICAL ANALYSIS BETWEEN MUT AND WT BY STRAIN TYPE
strain_results = []

for strain in valid_df['strain'].unique():
    strain_data = valid_df[valid_df['strain'] == strain]
    wt = strain_data[strain_data['type'] == 'WT']['time_to_80%']
    mut = strain_data[strain_data['type'] == 'MUT']['time_to_80%']
    
    # Mann-Whitney U test
    W, p = stats.mannwhitneyu(wt, mut)
    
    strain_results.append({
        'Strain': strain,
        'WT Mean Time (min)': np.mean(wt),
        'MUT Mean Time (min)': np.mean(mut),
        'W statistic': W,
        'p-value': p
    })

# Convert results to DataFrame
results_table = pd.DataFrame(strain_results)

# Display results
print(results_table)
'''
OUTPUT :
Strain | WT Mean Time (min) |  MUT Mean Time (min) |W statistic| p-value
Strain1|       757.5        |          752.5       |    17.5   | 1.000000
Strain2|       682.5        |          615.0       |    25.0   | 0.295406
Strain3|       550.0        |          565.0       |    17.0   | 0.935622
'''
'''
INTERPRTATION : 
Based on the biostatisticall results we can conclude that, even by strain types, there is no significant difference between mutants and wild-type, in
terms of OD recorded, because P-values in the three cases is superior than 0,05.
Meaning that the knockout manipulation didn't affect the growth of the 3 strains.
'''
