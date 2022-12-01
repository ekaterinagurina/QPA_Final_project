import unittest
import script

class DnaToRnaTest(unittest.TestCase):
    def test_basic_sequence(self):
        self.assertEqual(script.convert_dna_to_rna('ATTTGGCTACTAACAATCTA'), 'AUUUGGCUACUAACAAUCUA')
        self.assertEqual(script.convert_dna_to_rna('GTTGTAATGGCCTACATTA'), 'GUUGUAAUGGCCUACAUUA')
        self.assertEqual(script.convert_dna_to_rna('CAGGTGGTGTTGTTCAGTT'), 'CAGGUGGUGUUGUUCAGUU')
        self.assertEqual(script.convert_dna_to_rna('GCTAACTAAC'), 'GCUAACUAAC')
        self.assertEqual(script.convert_dna_to_rna('CCCGTCCTTGATTGGCTTGAAGAGAAGTTT'), 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU')

    def test_lowercase_sequence(self):
        self.assertEqual(script.convert_dna_to_rna('atttggctactaacaatcta'), 'AUUUGGCUACUAACAAUCUA')
        self.assertEqual(script.convert_dna_to_rna('gttgtaatggcctacatta'), 'AUUUGGCUACUAACAAUCUA')
        self.assertEqual(script.convert_dna_to_rna('caggtggtgttgttcagtt'), 'AUUUGGCUACUAACAAUCUA')

    def test_empty_sequence(self):
        self.assertEqual(script.convert_dna_to_rna(''), '')

    def test_trailing_spaces(self):
        self.assertEqual(script.convert_dna_to_rna('  AT  TTGG CTAC TAACA ATCTA  '), 'AUUUGGCUACUAACAAUCUA')
        self.assertEqual(script.convert_dna_to_rna(' C AGG TG GTG  TTGTT  CAG TT'), 'CAGGUGGUGUUGUUCAGUU')


class DnaToRnaTest(unittest.TestCase):
    def test_basic_sequence(self):
        self.assertEqual(script.convert_rna_to_protein('AUUUGGCUACUAACAAUCUA'), 'IWLLTI')
        self.assertEqual(script.convert_rna_to_protein('GUUGUAAUGGCCUACAUUA'), 'VVMAYI')
        self.assertEqual(script.convert_rna_to_protein('CAGGUGGUGUUGUUCAGUU'), 'QVVLFS')
        self.assertEqual(script.convert_rna_to_protein('CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'), 'PVLDWLEEKF')

    def test_stopcodon_sequence(self):
        self.assertEqual(script.convert_rna_to_protein('GCUAACUAAC'), 'ANSTOP')
        self.assertEqual(script.convert_rna_to_protein('GCUAACUAACAUCUUUGGCACUGUU'), 'ANSTOPHLWHC')
        self.assertEqual(script.convert_rna_to_protein('caggtggtgttgttcagtt'), 'AUUUGGCUACUAACAAUCUA')

    def test_empty_sequence(self):
        self.assertEqual(script.convert_rna_to_protein(''), '')

    def test_trailing_spaces(self):
        self.assertEqual(script.convert_rna_to_protein('G UUG UA  AUG GCCU AC AUUA'), 'VVMAYI')
        self.assertEqual(script.convert_rna_to_protein(' C A GG UGG UG UUGUUCA    G UU'), 'QVVLFS')


if __name__ == '__main__':
    unittest.main()
