import pytest
from UniProjectToolkit.modules.Dictionaries import codon_table, complement_table, acceptable_codons
from UniProjectToolkit.modules.Translate import find, protein_print
from UniProjectToolkit.modules.new_reverse import reverse_complement, reverse_string, complement
from UniProjectToolkit.modules.logger import logger


def test_reverse_string():
        dna = "aggagtaagcccttgcaactggaaatacacccattg"
        result = reverse_string(dna)
        expected = "gttacccacataaaggtcaacgttcccgaatgagga"
        logger.info(f"testing for reversing string  before doing reverse_complement{result}")
        assert result == expected

def test_complement():
    dna = "aggagtaagcccttgcaactggaaatacacccattg" 
    result = complement(dna, complement_table)
    expected = "caatgggtgtatttccagttgcaagggcttactcct"
    logger.info(f"testing for dna string when reverse complementing{result}")
    assert result == expected

def test_reverse_complement():
    dna = "aggagtaagcccttgcaactggaaatacacccattg" 
    result = reverse_complement(codon_table, complement_table, dna)
    expected = ['Q', 'W', 'V', 'Y', 'F', 'Q', 'L', 'Q', 'G', 'L', 'T', 'P']
    logger.info(f"testing for overall functionality of reversing string and then finding the protein{result}")
    assert result == expected
