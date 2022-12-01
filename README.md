# Quantori Python Academy Project

## Description

Projects for two of three stages of The central dogma of molecular biology:
  1. Transcription - copying a segment of DNA into RNA
  2. Translation - the process of creating proteins from an mRNA template

Also there is script for plotting guanine-cytosine content (GC-content) of DNA molecule. As an example I used CF transmembrane conductance regulator which is located in 7q chromose.  

"The encoded protein functions as a chloride channel, making it unique among members of this protein family, and controls ion and water secretion and absorption in epithelial tissues. Channel activation is mediated by cycles of regulatory domain phosphorylation, ATP-binding by the nucleotide-binding domains, and ATP hydrolysis. Mutations in this gene cause cystic fibrosis, the most common lethal genetic disorder in populations of Northern European descent. The most frequently occurring mutation in cystic fibrosis, DeltaF508, results in impaired folding and trafficking of the encoded protein." National Library of Medicine

I chose exactly this gene because I used to work with patients diagnosed with cystic fibrosis. FASTA file is taken from https://www.ncbi.nlm.nih.gov/ website.

## Sctructure
`script.py` Has main function `convert_dna_to_rna`, `convert_rna_to_protein`, `gc_ratio_plotting`
`test.py` Runs Unittests
`data -> database.py` Creating databases with four tables `DNA_Bases`, `RNA_Bases`, `Codons`, `AminoAcids` and setting one-to-one relation.
`data -> filling.py` Filling up the databases.
`data -> final_project.db` Database file for the one created above.
`data -> gene.fna` FASTA file with DNA sequence.
`plots -> gc-content.png` An output for the plotting function.
