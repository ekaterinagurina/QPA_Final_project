from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class DNA_Bases(Base):
    __tablename__ = 'DNA_bases'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(1))
    rna = relationship("RNA_Bases", back_populates="dna")

    def __str__(self):
        return f"{self.name}"


class RNA_Bases(Base):
    __tablename__ = 'RNA_bases'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(1))
    dna_id = Column(Integer, ForeignKey("DNA_bases.id"))
    dna = relationship("DNA_Bases", back_populates="rna")

    def __str__(self):
        return f"{self.name}"


class Codons(Base):
    __tablename__ = "codons"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(3))
    aminoacid = relationship("AminoAcids", back_populates="codon")
    aminoacid_id = Column(Integer, ForeignKey("aminoacids.id"))

    def __str__(self):
        return f'{self.id}'


class AminoAcids(Base):
    __tablename__ = "aminoacids"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(1))
    codon = relationship("Codons", back_populates="aminoacid")

    def __str__(self):
        return f'{self.id} {self.aminoacid_title}'
