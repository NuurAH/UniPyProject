import pytest
from UniProjectToolkit.modules.Translate import find
from UniProjectToolkit.modules.Dictionaries import codon_table, acceptable_codons
from UniProjectToolkit.modules.logger import logger


def test_find_extracted_proteins():
        dna = "aggagtaagcccttgcaactggaaatacacccattg" 
        result = find(codon_table, acceptable_codons, dna)
        expected = ['R', 'S', 'K', 'P' , 'L', 'Q', 'L', 'E', 'I', 'H', 'P', 'L']
        logger.info(f"testing for extracting proteins from split dna function {result}")
        assert result == expected

def test_acceptable_codons():
        dna = "aggagtaagcccttgcaactggaaatacacccattgabc" 
        result = find(codon_table, acceptable_codons, dna)
        expected = ['R', 'S', 'K', 'P' , 'L', 'Q', 'L', 'E', 'I', 'H', 'P', 'L']
        logger.info(f"testing for unacceptable codons at the end {result}")
        assert result == expected

def test_acceptable_codons_break():
        dna = "aggagtaagxxxcccttgcaactggaaatacacccatt" 
        result = find(codon_table, acceptable_codons, dna)
        expected = ['R', 'S', 'K']
        logger.info(f"testing for unacceptable codons in the middle {result}")
        assert result == expected