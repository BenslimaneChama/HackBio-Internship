"""
Stage 1 Library - HackBio Internship

This module contains functions developed by our team for the Stage 1 challenge in the HackBio internship:
- Chama BENSLIMANE (Leader): https://github.com/BenslimaneChama
- Mohammad HICHAM POLO : https://github.com/MohammadHichamPolo
It includes functions for analyzing DNA sequences, generating bacterial growth curves, determining 80% density values and calculating the hamming distance between two str.

GitHub Repository: https://github.com/BenslimaneChama/HackBio-Internship/tree/main/Stage%201
LinkedIn Video: https://www.linkedin.com/feed/update/urn:li:ugcPost:7297001015092932608/
"""
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#FUNCTION NUMBER 1 : Analyzing a FASTA file and translating DNA to an Amino Acid sequence
"""
    Reads a FASTA file, analyzes nucleotide composition, calculates CG content,
    transcribes DNA to RNA, and translates RNA to an amino acid sequence.

    Parameters:
    file_location (str): Path to the FASTA file.
    strand_type (str): 'forward' for forward strand transcription, otherwise reverse.

    Returns:
    None (Prints results to the console)
"""
def analyze_fasta(file_location,strand_type):
        
    with open(file_location, "r") as fasta_file:
        fasta_content = fasta_file.readlines()
    
    header = fasta_content[0].strip()
    dna = ''.join(fasta_content[1:]).replace('\n', '').upper().replace(" ", "")
    
    counts = {"A": 0, "T": 0, "C": 0, "G": 0}
    for nucleotide in dna:
        if nucleotide in counts:
            counts[nucleotide] += 1
    
    total_nucleotides = sum(counts.values())
    percentages = {nt: (counts[nt] / total_nucleotides) * 100 for nt in counts}
    cg_content = percentages["C"] + percentages["G"]
    
    rna_reverse = dna.replace('T', 'U')
    rna_forward = ''.join({'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}[nt] for nt in dna)
    rna = rna_forward if strand_type == 'forward' else rna_reverse
    
    codon_stop = ['UAA', 'UGA', 'UAG']
    codon_start = 'AUG'
    start_index = rna.find(codon_start)
    codon_chains = []
    
    while start_index != -1:
        codons = []
        for i in range(start_index, len(rna), 3):
            codon = rna[i:i+3]
            codons.append(codon)
            if codon in codon_stop:
                break
        codon_chains.append(codons)
        start_index = rna.find(codon_start, start_index + 1)
    
    amino_acids = {
        "G": ["GGU", "GGC", "GGA", "GGG"], "P": ["CCU", "CCC", "CCA", "CCG"], "A": ["GCU", "GCC", "GCA", "GCG"],
        "V": ["GUU", "GUC", "GUA", "GUG"], "L": ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"], "I": ["AUU", "AUC", "AUA"],
        "M": ["AUG"], "C": ["UGU", "UGC"], "F": ["UUU", "UUC"], "Y": ["UAU", "UAC"], "W": ["UGG"], "H": ["CAU", "CAC"],
        "K": ["AAA", "AAG"], "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"], "Q": ["CAA", "CAG"], "N": ["AAU", "AAC"],
        "E": ["GAA", "GAG"], "D": ["GAU", "GAC"], "S": ["UCU", "UCC", "UCA", "UCG"], "T": ["ACU", "ACC", "ACA", "ACG"]
    }
    
    aa_sequences = []
    for codon_sequ in codon_chains:
        aa_sequence = ''
        for codon in codon_sequ:
            for aa, codon_list in amino_acids.items():
                if codon in codon_list:
                    aa_sequence += aa
                    break
            else:
                aa_sequence += 'X' 
        aa_sequences.append(aa_sequence)
    
    print("\nFASTA Analysis Results")
    print("----------------------")
    print(f"Header: {header}\n")
    print("Nucleotide Counts:")
    for nt, count in counts.items():
        print(f"  {nt}: {count}")
    print(f"\nCG Content: {cg_content:.2f}%\n")
    print("Amino Acid Sequences:")
    for i, seq in enumerate(aa_sequences, start=1):
        print(f"  Sequence {i}: {seq}")
#FUNCTION NUMBER 2 : Generates bacterial growth curves based on various input parameters
"""
    Generates simulated bacterial growth curves, including lag, exponential, stationary, and death phases.

    Parameters:
    unit_type (str): 's', 'min', or 'h' for time units.
    time_period (int): Total time period.
    col_numbers (int): Number of time points.
    raw_numbers (int): Number of different growth curves to generate.
    starting_point (float): Initial cell count.
    expo_start (int, optional): Column index where exponential growth starts.
    expo_end (int, optional): Column index where exponential growth ends.

    Returns:
    pd.DataFrame: Simulated bacterial growth data.
"""
def generate_growth_curves(unit_type, time_period, col_numbers, raw_numbers, starting_point, expo_start=None, expo_end=None):
    data = pd.DataFrame()
    colors = plt.cm.tab10(np.arange(raw_numbers) % 10) if raw_numbers > 1 else ['#1f77b4']

    original_time_period = time_period if unit_type != 'h' else time_period / 60

    for _ in range(raw_numbers):
        values = []
        current_value = starting_point

        if expo_start is None:
            expo_start = random.randint(1, col_numbers // 4)
        if expo_end is None:
            expo_end = random.randint(expo_start + 1, col_numbers // 2)

        lag_range = expo_start
        expo_range = expo_end - expo_start
        remaining = col_numbers - expo_end
        stationary_range = random.randint(0, remaining)
        death_range = remaining - stationary_range

        # Lag phase
        values += [current_value] * lag_range

        # Exponential phase
        if expo_range > 0:
            expo_values = [min(current_value * (1.2 ** i), 10000) for i in range(1, expo_range + 1)]
            values += expo_values
            current_value = expo_values[-1] if expo_values else current_value

        # Stationary phase
        if stationary_range > 0:
            values += [current_value] * stationary_range

        # Death phase
        if death_range > 0:
            death_values = [current_value * (0.8 ** i) for i in range(1, death_range + 1)]
            values += death_values
            current_value = death_values[-1] if death_values else current_value

        values = values[:col_numbers] if len(values) > col_numbers else values + [current_value] * (col_numbers - len(values))
        data = pd.concat([data, pd.DataFrame([values])], ignore_index=True)

    data += 1  # Avoid log scale issues
    print(data)

    x_values = np.linspace(0, original_time_period, num=col_numbers)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_yscale('log')

    def update(frame):
        ax.clear()
        ax.set_title(f"Growth Curves (Time Unit: {unit_type})")
        ax.set_xlabel(f"Time ({'hours' if unit_type == 'h' else 'minutes' if unit_type == 'min' else 'seconds'})")
        ax.set_ylabel("Nº of Bacteria cells (log scale)")
        ax.set_yscale('log')
        
        y_min, y_max = data.min().min(), data.max().max()
        y_min = max(y_min, 1)
        y_max = max(y_max, 10)
        
        ax.set_xlim(0, original_time_period)
        ax.set_ylim(y_min * 0.5, y_max * 2)
        
        if raw_numbers == 1:
            ax.plot(x_values[:frame+1], data.iloc[0, :frame+1], color=colors[0])
        else:
            ax.plot(x_values, data.iloc[frame, :], color=colors[frame])
        
        ax.legend([f"Curve {frame+1}"])
        
    ani = animation.FuncAnimation(fig, update, frames=col_numbers if raw_numbers == 1 else raw_numbers, interval=1000, repeat=False)
    plt.show()
    return data
#FUNCTION NUMBER 3 : Calculates the 80% density value from a growth curve
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
#FUNCTION NUMBER 4 : Cslculates the hamming distance between two chains of characters
"""
    Computes the Hamming distance between two strings of equal length.
    
    Parameters:
    slack_username (str): First string.
    X_username (str): Second string.
    
    Returns:
    int: The Hamming distance between the two strings.
"""
def hamming_distance(slack_username, X_username):
    slack_username = slack_username.upper()
    X_username = X_username.upper()
    if len(slack_username) != len(X_username):
        raise ValueError("The two chaines should be in the same length!!")
    distance = 0
    for Pseudo in range(len(slack_username)):
        if slack_username[Pseudo] != X_username[Pseudo]:
            distance += 1
    return distance
