import sys
import matplotlib.pyplot as plt
from data.filling import rna_dna_bases, aminoacids_tables
from Bio.SeqIO import parse


# Converting DNA to RNA by replacing "T" to "U"
def convert_dna_to_rna(dna_sequence: str) -> str:
    # rna_sequence = sequence.replace("T", "U") # first variant of the task #1 before database
    dna_sequence = ''.join(dna_sequence.split()).upper()
    rna_sequence = ""
    for base in dna_sequence:
        rna_sequence += rna_dna_bases(base)
    return rna_sequence


# Converting RNA to protein
def convert_rna_to_protein(rna_sequence: str) -> str:
    rna_sequence = ''.join(rna_sequence.split()).upper()
    protein = ""
    # checking the length of our sequence, considering its length may not be divisible by triplets completely
    for i in range(0, len(rna_sequence) - (3 + len(rna_sequence) % 3) + 2, 3):
        protein += aminoacids_tables(rna_sequence[i:i + 3])
    return protein


def gc_ratio_plotting(string, step=100):
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
    plt.savefig('./plots/gc-content.png', dpi=100)
    return plt.show()


plot_seq = parse(open('./data/gene.fna'), 'fasta')
for s in plot_seq:
    plot_seq = s.seq

cftr_gc_ratio = gc_ratio_plotting(plot_seq)




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