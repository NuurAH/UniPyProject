import pytest
from UniProjectToolkit.modules.GappingDNA import split_dna, format_dna
from UniProjectToolkit.modules.logger import logger

#test for main functionality
def test_formattedDNA_regular():
        dna = "aggagtaagcccttgcaactggaaatacacccattg"
        expected = "agg agt aag ccc ttg caa ctg gaa ata cac cca ttg"
        result = format_dna(dna, block_size=3)
        logger.info(f"Testing for main functionality: {result}")
        assert result == expected

#test to see if incomplete inputs can be returned
def test_gappingDNA_incomplete():
        dna = "aggagtaagcccttgcaactggaaatacacccatt"
        expected = "agg agt aag ccc ttg caa ctg gaa ata cac cca tt"
        result = format_dna(dna, block_size=3)
        logger.info (f"testing for incomplete inputs {result}")
        assert result == expected

#test to see if different block sizes work
def test_format_DNA_different():
        dna = "aggagtaagcccttgcaactggaaatacacccattg"
        expected = "aggag taagc ccttg caact ggaaa tacac ccatt g"
        result = format_dna(dna, block_size=5)
        logger.info(f"testing for different size inputs {result}")   
        assert result == expected

def test_split_DNA_blocksize_type():
        dna = "aggagtaagcccttgcaactggaaatacacccattg"
        logger.info("Testing with invalid block size parameter, with a type that is not an int should raise type error")
        with pytest.raises(TypeError):
                split_dna(dna, block_size="3")



def test_split_dna():
        dna = "aggagtaagcccttgcaactggaaatacacccattg"
        expected = ["agg", "agt", "aag", "ccc", "ttg", "caa", "ctg", "gaa", "ata", "cac", "cca", "ttg"]
        result = split_dna(dna, block_size=3)
        logger.info(f"Testing list construction {result}")
        assert result == expected

def test_split_dna_upper():
        dna = "aggagtaagcccttgcaactggaaatacacccattg"
        expected = ["AGG", "AGT", "AAG", "CCC", "TTG", "CAA", "CTG", "GAA", "ATA", "CAC", "CCA", "TTG"]
        dna_upper = dna.upper()
        result = split_dna(dna_upper, block_size=3)
        logger.info(f"Testing upper case list construction {result}")
        assert result == expected