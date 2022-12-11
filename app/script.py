import sys
import matplotlib.pyplot as plt
from db.filling import rna_dna_bases, aminoacids_tables
from config import INPUT_GENE

'''Making a constant value for the Rna_To_Protein Function.
This constant represents an RNA triplet needed to be assign to specific aminoacid'''
TRIPLET = 3


def convert_dna_to_rna(dna_sequence: str) -> str:
    ''' Converting DNA sequence to RNA sequence by replacing "T" base to "U" base'''
    dna_sequence = ''.join(dna_sequence.split()).upper()
    rna_sequence = ""
    for base in dna_sequence:
        rna_sequence += rna_dna_bases(base)
    return rna_sequence


def convert_rna_to_protein(rna_sequence: str) -> str:
    ''' Converting RNA sequence into the amino acid sequence of a protein.
    Using tables of aminoacids from /db/filling,py '''

    rna_sequence = ''.join(rna_sequence.split()).upper()
    protein = ""

    ''' checking the length of our sequence,
    considering its length may not be divisible by triplets completely '''

    for i in range(0, len(rna_sequence) - (3 + len(rna_sequence) % 3) + 2, TRIPLET):
        protein += aminoacids_tables(rna_sequence[i:i + 3])
    return protein


def gc_ratio_plotting(string: str, step=100) -> None:
    '''This is a script to count GC-content of a DNA seqeunce and then to plot GC ratio in a DNA molecule.
    The horizontal axis of this graph is the genome position.
    The vertical axis is the GC ratio in the window.
    Default size of a window be 100 bases.'''
    x_axis = []
    y_axis = []
    for i in range(0, len(string), step):
        genome = string[i:i + step]
        gc_count = genome.count('C') + genome.count('G')
        gc_ratio = round(100 * (gc_count / step))
        x_axis.append(i)
        y_axis.append(gc_ratio)
    plt.plot(x_axis, y_axis, color='#a652ad')
    plt.title('GC-content', style='italic', size=16)
    plt.xlabel('Genome position', size=14)
    plt.ylabel('GC ratio, %', size=14)
    figure = plt.gcf()
    figure.set_size_inches(12, 6)
    plt.savefig('./app/data/gc-content.png', dpi=100)
    return plt.show()


def open_input_file(plot_seq: str) -> str:
    '''Function to open file with genom sequence. Works with FASTA files'''
    plot_seq = INPUT_GENE
    for s in plot_seq:
        plot_seq = s.seq


'''Calling gc_ratio_plotting function to get GC-plot'''
gc_ratio = gc_ratio_plotting(open_input_file)
gc_ratio()


def command_input(input_data):
    if len(sys.argv) == 3:
        command = sys.argv[1].strip()
        input_data = sys.argv[2]
        if command == "trascription":
            print(convert_dna_to_rna(input_data))
        if command == "translation":
            print(convert_rna_to_protein(input_data))
    else:
        print("You must put 3 arguments!")


if __name__ == '__main__':
    command_input(sys.argv)
