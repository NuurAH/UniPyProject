import pytest
from UniProjectToolkit.modules.GappingDNA import gapping_dna
#from UniProjectToolkit.modules.Genbank import NewLine, GenScale, GenerateBank
from UniProjectToolkit.modules.GCcontent import countGCpercentage
from UniProjectToolkit.modules.Dictionaries import codon_table
#from UniProjectToolkit.modules.ReverseComplement import reverse_complement, complementary, manipulation
from UniProjectToolkit.modules.Translate import find, loop, protein_print
def test_gappingDNA():
        dna = "aggagtaagcccttgcaactggaaatacacccattg"
        gapped_dna = gapping_dna(dna)
        assert gapped_dna == "agg  agt  aag  ccc  ttg  caa  ctg  gaa  ata  cac  cca  ttg"

def test_GCP():
        dna = "GAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAGAATTGTTACAAATCACCCCTCAAGGAACCAGGGATGAAATCAGTTTGGATTCTGCAAAAAAGGCTGCTTGTGAATTTTCTGAGACGGATGTAA"
        GCPercent = countGCpercentage(dna)
        assert GCPercent == 43

@pytest.mark.parametrize("codon_list, expected", [("ATG", ["M"]), ("GTT", ["V"]), ("CAT", ["H"])])
def test_find(codon_list, expected):
        dna_list = [codon_list]
        extracted_codons = []
        result = find(codon_table, dna_list, extracted_codons)
        assert result == expected

def test_loop():
        dna = "aggagtaagcccttgcaactggaaatacacccattg"
        dna_list = []
        extracted_codons = []   
        loop(dna, dna_list, extracted_codons)
        assert extracted_codons == ['R', 'S', 'K', 'P' , 'L', 'Q', 'L', 'E', 'I', 'H', 'P', 'L']
        assert dna_list == ['AGG', 'AGT', 'AAG', 'CCC', 'TTG', 'CAA', 'CTG', 'GAA', 'ATA', 'CAC', 'CCA', 'TTG']

def test_protein_print():
        extracted_codons = ["R", "L", "K", "S", "I", "P" ]
        assert protein_print(extracted_codons)== "RLKSIP"

