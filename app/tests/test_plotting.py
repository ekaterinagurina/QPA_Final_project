import unittest
from os.path import exists as is_file
from script import gc_ratio_plotting
from config import INPUT_GENE


class GCRatioPlottingTest(unittest.TestCase):
    def test_gc_ratio(self):
        gc_ratio_plotting(INPUT_GENE)
        self.assertTrue(is_file('gc-content.png'))


if __name__ == '__main__':
    unittest.main()
