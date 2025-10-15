import pytest
from UniProjectToolkit.modules.Translate import find
from UniProjectToolkit.modules.Dictionaries import codon_table
from UniProjectToolkit.modules.logger import logger

def test_find_extracted_proteins():
        dna = "aggagtaagcccttgcaactggaaatacacccattg" 
        result = find(dna, codon_table)
        expected = ['R', 'S', 'K', 'P' , 'L', 'Q', 'L', 'E', 'I', 'H', 'P', 'L']
        logger.info(f"testing for extracting proteins from split dna function {result}")
        assert result == expected

