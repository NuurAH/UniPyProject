from UniProjectToolkit.modules.Dictionaries import acceptable_codons, stop_codon, start_codon, codon_table
from UniProjectToolkit.modules.GappingDNA import split_dna
from UniProjectToolkit.modules.logger import logger

#functions   
def find(codon_table, acceptable_codons, dna=str, *args):
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
            if protein not in acceptable_codons:
                logger.info (f"this codon is not in our acceptable codons: {codon}")
                break
            elif protein is None:
                logger.warning(f"Unknown codon: {codon}")
                break
            extracted_proteins.append(protein) 
        #give warning that this does not start at start codon
        if extracted_proteins[0] != "M":
            logger.info(f"this does not begin with a start codon!")
        #give warning that this doesn't end in a stop codon
        elif extracted_proteins[-1] != "*":
            logger.info(f"this does not end in a termination codon!")
        #end of the command
        return extracted_proteins
    except Exception as e:
        logger.error("Protein Extraction failed: {}" .format(e))
        raise


def post_modifications(start_codon, stop_codon, any_list=list):
#this changes the sequence so it begins at a start codon and ends at a stop codon
    if start_codon in any_list:
        while any_list and any_list[0] != start_codon:
            del any_list[0]
    if stop_codon in any_list:
        while any_list and any_list[-1] != stop_codon:
            any_list.pop(-1)
        any_list.append(stop_codon)
    return any_list


def protein_print(extracted_proteins=list):
    try:
        if not isinstance(extracted_proteins, list):
            raise TypeError("Issue with previous step, please check log!")
        protein_string = ""
        for protein in extracted_proteins:
            protein_string += protein
        return(protein_string)
    except TypeError as e:
        logger.error ("protein printing has failed with exception: {}" .format(e))