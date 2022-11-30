from data.database_tables import Base, DNA_Bases, RNA_Bases, Codons, AminoAcids
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///final_project.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()


def rna_dna_bases():
    rna_a = RNA_Bases(name="A")
    rna_u = RNA_Bases(name="U")
    rna_c = RNA_Bases(name="C")
    rna_g = RNA_Bases(name="G")

    dna_a = DNA_Bases(name="A", rna=[rna_a])
    dna_t = DNA_Bases(name="T", rna=[rna_u])
    dna_c = DNA_Bases(name="C", rna=[rna_c])
    dna_g = DNA_Bases(name="G", rna=[rna_g])

    dna_bases = [dna_a, dna_t, dna_c, dna_g]

    with Session() as session:
        session.add_all(dna_bases)
        session.commit()


def aminoacids_tables():
    triplets_to_aminoacids = {'A': ['GCC', 'GCU', 'GCA', 'GCG'], 'C': ['UGU', 'UGC'],
                              'D': ['GAU', 'GAC'], 'E': ['GAA', 'GAG'],
                              'F': ['UUU', 'UUC'], 'G': ['GGU', 'GGC', 'GGA', 'GGG'],
                              'H': ['CAU', 'CAC'], 'I': ['AUU', 'AUC', 'AUA'],
                              'K': ['AAA', 'AAG'], 'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
                              'M': ['AUG'], 'N': ['AAU', 'AAC'], 'P': ['CCU', 'CCC', 'CCA', 'CCG'],
                              'Q': ['CAA', 'CAG'], 'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
                              'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
                              'STOP': ['UAA', 'UGA', 'UAG'], 'T': ['ACU', 'ACC', 'ACA', 'ACG'],
                              'V': ['GUU', 'GUC', 'GUA', 'GUG'], 'W': ['UGG'], 'Y': ['UAU', 'UAC']}

    for codon, amino_acid in triplets_to_aminoacids.items():
        aminoacid = AminoAcids(name=amino_acid)
        codons = Codons(name=codon, aminoacid=aminoacid)
        session.add(codons)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    rna_dna_bases()
    aminoacids_tables()
