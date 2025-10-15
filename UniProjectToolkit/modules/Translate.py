from UniProjectToolkit.modules.Dictionaries import acceptable_codons, stop_codon, start_codon
from UniProjectToolkit.modules.Dictionaries import codon_table as default_table
from UniProjectToolkit.modules.GappingDNA import split_dna
from UniProjectToolkit.modules.logger import logger

#functions   
def find(dna, codon_table):
    if codon_table is None:
        codon_table = default_table
    try:
        dna_upper= dna.upper()
        dna_list = split_dna(dna_upper,block_size=3)
        extracted_proteins = []
        for codon in dna_list:
            protein = None
            for key, value in codon_table.items():
                if codon in value:
                    protein = key
                    break
            if protein is None:
                logger.warning(f"Unknown codon: {codon}")
                raise
            extracted_proteins.append(protein) 

        return extracted_proteins
    except Exception as e:
        logger.error("Protein Extraction failed: {}" .format(e))
        raise




# def find(codon_table, dna_list, extracted_codons):
#     for key, value in codon_table.items():
#         if dna_list[-1] in value:
#             extracted_codons.append(key)
#     return(extracted_codons)
# #rewrite code?
# #cr
# def loop(dna, dna_list, extracted_codons):
#     dna_upper = dna.upper() 
#     split_dna(dna_upper,block_size=3)
#     find(codon_table, dna_list, extracted_codons)
#     return dna_list, extracted_codons


def protein_print(extracted_proteins):
    protein_string = ""
    for protein in extracted_proteins:
        protein_string += protein
        if protein not in acceptable_codons:   
            print(f"{protein} is not an acceptable codon!")
        elif protein == stop_codon:
            return (protein_string)
    return(protein_string)

#ctrl forward slash comments sections and can uncomment

# if __name__ == "__main__":
#     dna = "aggagtaagcccttgcaactggaaatacacccattg"
#     dna_length = len(dna)
#     dna_list = []
#     extracted_codons = []
#     loop(dna,dna_list, extracted_codons, find)
#     protein_print(extracted_codons)


