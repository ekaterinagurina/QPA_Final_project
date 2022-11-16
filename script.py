# First we input the DNA sequence
dna_seq = input(("Enter DNA sequence: "))

# Converting DNA to RNA by replacing "T" to "U"
def convert_dna_to_rna(dna_seq):
    return dna_seq.replace("T", "U")

# Our converted DNA becomes RNA string now
rna_seq = convert_dna_to_rna(dna_seq)

# Converting RNA to protein
def convert_rna_to_protein(rna_seq):
        # Here is a dictionary with RNA codons to aminoacids
        rna_codon = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
                    "UCU": "S", "UCC": "s", "UCA": "S", "UCG": "S",
                    "UAU": "Y", "UAC": "Y", "UAA": ".", "UAG": ".",
                    "UGU": "C", "UGC": "C", "UGA": ".", "UGG": "W",
                    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
                    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
        protein = "" # creating an empty string
        # checking the length of our sequence, considering it's length may not be divisible by triplets completely
        for i in range(0, len(rna_seq) - (3 + len(rna_seq) % 3) + 2, 3):
            protein += rna_codon[rna_seq[i:i + 3]]
        return protein

# Giving our protein string a name
protein_seq = convert_rna_to_protein(rna_seq)

# Printing out our results
print("DNA:", dna_seq)
print("RNA:", rna_seq)
print("Protein:", protein_seq)