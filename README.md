# Quantori Python Academy Project
- [Description](#Description)
- [Project Structure](#Project-Structure)
- [Setup](#Setup)
## Description

Projects for two of three stages of The central dogma of molecular biology:
  1. Transcription - copying a segment of DNA into RNA
  2. Translation - the process of creating proteins from an mRNA template

Also there is script for plotting guanine-cytosine content (GC-content) of DNA molecule. 
*As an example I used CF transmembrane conductance regulator which is located in 7q chromose.*

#### Small note on Cystic Fibrosis

> "The encoded protein functions as a chloride channel, making it unique among members of this protein family, 
> and controls ion and water secretion and absorption in epithelial tissues. 
> Channel activation is mediated by > cycles of regulatory domain phosphorylation, ATP-binding by the nucleotide-binding domains, 
> and ATP hydrolysis. Mutations in this gene cause cystic fibrosis, the most common lethal genetic disorder in 
> populations of Northern European descent. The most frequently occurring mutation in cystic fibrosis, 
> DeltaF508, results in impaired folding and trafficking > of the encoded protein." *National Library of Medicine*

*I chose exactly this gene because I used to work with patients diagnosed with cystic fibrosis.*
FASTA file is taken from https://www.ncbi.nlm.nih.gov/ website.

## Project Structure
``` bash
└── `QPA_Final_project`
    ├── `app`
    │   ├── `data`
    │   │   ├── `gc-content.png` - output file for gc_ratio_plotting in script.py
    │   │   └── `gene.fna` - FASTA file with DNA sequence to plot GC-ratio
    │   ├── `db`
    │   │   ├── `__init__.py`
    │   │   ├── `database.py` - Creating databases with four tables DNA_Bases, RNA_Bases, Codons, AminoAcids and setting one-to-one relation.
    │   │   ├── `filling.py` - filling up the databases with dna, rna, aminoacids bases
    │   │   └── `final_project.db` Database file for the one created above.
    │   ├── `tests`
    │   │   ├── `__init__.py`
    │   │   ├── `test_dna_to_rna.py` - file to run test convertion DNA sequence to RNA sequence using Unittest
    │   │   ├── `test_plotting.py` - file to test plotting GC-ratio using Unittest
    │   │   └── `test_rna_to_protein.py` - file to run test convertion RNA sequence to protein sequence using Unittest
    │   ├── `__init__.py`
    │   ├── `config.py` - configuration file
    │   ├── `script.py` - main file which contents following functions: convert_dna_to_rna, convert_rna_to_protein, gc_ratio_plotting
    │   ├── `docker-comp`ose.yml` - docker compose file
    │   ├── `dockerfile` - docker file for containers
    │   └── `requirements.txt` - list of need extensions to run project   
```

## Setup

### 1. Clone repository

```git clone https://github.com/ekaterinagurina/QPA_Final_project.git```

### 2. Build the project

```docker-compose up -d --build```

### 3. Run the app

```docker-compose run -it finalproject```

### ~ Run Transcription function

Transcripting DNA sequence into RNA sequence

```finalproject trascription <DNA sequence>```

In ```<DNA sequence>``` simply add valid DNA sequence, for example:

```finalproject trascription CAGGTGGTGTTGTTCAGTT```

output:

```CAGGTGGTGTTGTTCAGTT```

### ~ Run Translation function

Translating RNA sequence to build a chain of amino acids

```finalproject traslation <RNA sequence>```

In ```<RNA sequence>``` add valid RNA sequence, for example:

```finalproject trascription CAGGUGGUGUUGUUCAGUU```

output:

```QVVLFS```

### 4. Switch Docker containers off

When you need to close application, run this command:

```docker-compose down```
