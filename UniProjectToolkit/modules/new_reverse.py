from UniProjectToolkit.modules.Dictionaries import complement_table, acceptable_codons, codon_table
from UniProjectToolkit.modules.Translate import find, protein_print
from UniProjectToolkit.modules.GappingDNA import split_dna, format_dna
from UniProjectToolkit.modules.logger import logger

def reverse_string (dna=str):
    rev_string = dna[::-1]
    return rev_string

def complement (dna=str, default_table=dict):
    try:
        rev_string = reverse_string(dna)
        split_rev = split_dna(rev_string,block_size=1)
        reverse_codons = []
        for base in split_rev:
            nucleotide = None
            for key,value in default_table.items():
                if base in value:
                    nucleotide = key
                    break
            if nucleotide is None:
                logger.warning(f"Unknown nucleotide!: {base}")
                raise
            reverse_codons.append(nucleotide)
            complements = "".join(reverse_codons)
        return complements
    except Exception as e:
            logger.error("failed to reverse and complement the string: {}" .format(e))
            raise

def reverse_complement (codon_table, complement_table, dna=str):
    try:
        reverse_string = complement(dna, complement_table)
        reverse_protein = find(codon_table, acceptable_codons, reverse_string)
        print(reverse_protein)
        return reverse_protein
    except Exception as e:
            logger.error("failed reverse complementing : {}" .format(e))
            raise
