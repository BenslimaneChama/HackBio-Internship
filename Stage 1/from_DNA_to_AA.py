import pandas as pd
from stage1library import analyze_fasta

file_location = input("Enter the path to the FASTA file: ")
strand_type = input("Is the strand forward or reverse? (Enter 'forward' or 'reverse'): ").strip().lower()
analyze_fasta(file_location,strand_type)
