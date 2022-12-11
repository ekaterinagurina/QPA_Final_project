import unittest
from script import convert_dna_to_rna

'''
Testing convert_dna_to_rna function from script.py using UnitTest.
Here we check if function works properly, check lowercase input converted to uppercase, check trailing whitespaces.
'''


class DnaToRnaTest(unittest.TestCase):
    def test_convert_DNA_RNA(self):
        self.assertEqual(convert_dna_to_rna('ATTTGGCTACTAACAATCTA'), 'AUUUGGCUACUAACAAUCUA')
        self.assertEqual(convert_dna_to_rna('GTTGTAATGGCCTACATTA'), 'GUUGUAAUGGCCUACAUUA')
        self.assertEqual(convert_dna_to_rna('CAGGTGGTGTTGTTCAGTT'), 'CAGGUGGUGUUGUUCAGUU')
        self.assertEqual(convert_dna_to_rna('GCTAACTAAC'), 'GCUAACUAAC')
        self.assertEqual(convert_dna_to_rna('CCCGTCCTTGATTGGCTTGAAGAGAAGTTT'), 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU')
        self.assertEqual(convert_dna_to_rna('atttggctactaacaatcta'), 'AUUUGGCUACUAACAAUCUA')
        self.assertEqual(convert_dna_to_rna('gttgtaatggcctacatta'), 'AUUUGGCUACUAACAAUCUA')
        self.assertEqual(convert_dna_to_rna('caggtggtgttgttcagtt'), 'AUUUGGCUACUAACAAUCUA')
        self.assertEqual(convert_dna_to_rna('  AT  TTGG CTAC TAACA ATCTA  '), 'AUUUGGCUACUAACAAUCUA')
        self.assertEqual(convert_dna_to_rna(' C AGG TG GTG  TTGTT  CAG TT'), 'CAGGUGGUGUUGUUCAGUU')


if __name__ == '__main__':
    unittest.main()
