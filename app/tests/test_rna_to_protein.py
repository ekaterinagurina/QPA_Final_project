import unittest
from script import convert_rna_to_protein

'''
Testing convert_rna_to_protein function from script.py using UnitTest.
Here we check if function works properly, check lowercase input converted to uppercase, check trailing whitespaces.
'''


class RnaToProteinTest(unittest.TestCase):
    def test_RNA_Protein(self):
        self.assertEqual(convert_rna_to_protein('AUUUGGCUACUAACAAUCUA'), 'IWLLTI')
        self.assertEqual(convert_rna_to_protein('GUUGUAAUGGCCUACAUUA'), 'VVMAYI')
        self.assertEqual(convert_rna_to_protein('CAGGUGGUGUUGUUCAGUU'), 'QVVLFS')
        self.assertEqual(convert_rna_to_protein('CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'), 'PVLDWLEEKF')
        self.assertEqual(convert_rna_to_protein('GCUAACUAAC'), 'ANSTOP')
        self.assertEqual(convert_rna_to_protein('GCUAACUAACAUCUUUGGCACUGUU'), 'ANSTOPHLWHC')
        self.assertEqual(convert_rna_to_protein('caggtggtgttgttcagtt'), 'AUUUGGCUACUAACAAUCUA')
        self.assertEqual(convert_rna_to_protein('G UUG UA  AUG GCCU AC AUUA'), 'VVMAYI')
        self.assertEqual(convert_rna_to_protein(' C A GG UGG UG UUGUUCA    G UU'), 'QVVLFS')


if __name__ == '__main__':
    unittest.main()
