from Bio.SeqIO import parse

DATABASE_URL = "sqlite:///app/db/final_project.db"
INPUT_GENE = parse(open('./app/data/gene.fna'), 'fasta')
