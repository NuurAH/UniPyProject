from UniProjectToolkit.modules.Translate import find, post_modifications
from UniProjectToolkit.modules.Dictionaries import codon_table, acceptable_codons, start_codon, stop_codon
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

def test_termination_codon_no_termination():
        dna = "aggagttaaaagcccttgcaactggaaatacacccattg" 
        result = find(codon_table, acceptable_codons, dna)
        expected = ['R', 'S', "*", 'K', 'P' , 'L', 'Q', 'L', 'E', 'I', 'H', 'P', 'L']
        logger.info(f"testing for termination codon not flagging {result}")
        assert result == expected


def test_post_modifications_start():
        dna = "aggagtatgaagcccttgcaactggaaatacacccattg" 
        intermediate = find(codon_table, acceptable_codons, dna)
        result = post_modifications(start_codon, stop_codon, intermediate)
        expected = ['M', 'K', 'P' , 'L', 'Q', 'L', 'E', 'I', 'H', 'P', 'L', ]
        logger.info(f"testing for extracting proteins from split dna function {result}")
        assert result == expected

def test_post_modifications_stop():
        dna = "aggagtaagtaacccttgcaactggaaatacacccatt" 
        intermediate = find(codon_table, acceptable_codons, dna)
        result = post_modifications(start_codon, stop_codon, intermediate)
        expected = ['R', 'S', 'K', "*"]
        logger.info(f"testing to see if a stop codon terminates this but only if the relevant argument is added {result}")