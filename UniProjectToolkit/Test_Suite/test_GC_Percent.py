import pytest
from UniProjectToolkit.modules.GCcontent import countGCpercentage
from UniProjectToolkit.modules.logger import logger

def test_GCP():
        dna = "GAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAGAATTGTTACAAATCACCCCTCAAGGAACCAGGGATGAAATCAGTTTGGATTCTGCAAAAAAGGCTGCTTGTGAATTTTCTGAGACGGATGTAA"
        result = countGCpercentage(dna)
        expected = 43
        logger.info(f"testing for main functionality of GCP: {result}")
        assert result == expected

def test_GCP_dna_type():
        logger.info("Testing with invalid type")
        with pytest.raises(TypeError):
                countGCpercentage(dna=555555555)
                
