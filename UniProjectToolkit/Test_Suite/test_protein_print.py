from UniProjectToolkit.modules.Translate import find, loop, protein_print
def test_protein_print():
        extracted_codons = ["R", "L", "K", "S", "I", "P" ]
        assert protein_print(extracted_codons)== "RLKSIP"