from UniProjectToolkit.modules.count_nucleotides import count_nucleotides
from UniProjectToolkit.modules.logger import logger

def test_count_nucleotides():
     dna = "aggagtaagcccttgcaactggaaatacacccattg" 
     result_1 = count_nucleotides(dna, single_nucleotide=True, double_nucleotide=False, triple_nucleotide=False)
     result_2 = count_nucleotides(dna, single_nucleotide=False, double_nucleotide=True, triple_nucleotide=False)
     result_3 = count_nucleotides(dna, single_nucleotide=False, double_nucleotide=False, triple_nucleotide=True)
     expected_1 =  ("Single Nucleotides Counter({'a': 12, 'c': 9, 'g': 8, 't': 7})", "", "")
     expected_2 = ("", "Double Nucleotides Counter({'aa': 3, 'gc': 2, 'cc': 2, 'at': 2, 'ac': 2, 'ag': 1, 'ga': 1, 'gt': 1, 'tt': 1, 'ct': 1, 'gg': 1, 'tg': 1})", "")
     expected_3 = ("", "", "Triple NucleotidesCounter({'ttg': 2, 'agg': 1, 'agt': 1, 'aag': 1, 'ccc': 1, 'caa': 1, 'ctg': 1, 'gaa': 1, 'ata': 1, 'cac': 1, 'cca': 1})")
     logger.info(f"testing for counting nucleotides")
     assert result_1 == expected_1
     assert result_2 == expected_2
     assert result_3 == expected_3


