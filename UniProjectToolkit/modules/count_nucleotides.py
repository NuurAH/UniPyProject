from UniProjectToolkit.modules.GappingDNA import split_dna, format_dna
from UniProjectToolkit.modules.logger import logger
from collections import Counter

def count_nucleotides(dna=str, single_nucleotide=False, double_nucleotide=False, triple_nucleotide=False):
    try:
        if not isinstance(dna, str):
            raise TypeError("DNA sequence needs to be a string!")
        if single_nucleotide == True:
            single_nucleotide = f"Single Nucleotides {Counter(split_dna(dna, block_size=1))}"
        else:
            single_nucleotide = ""
        if double_nucleotide == True:
            double_nucleotide = f"Double Nucleotides {Counter(split_dna(dna, block_size=2))}"
        else:
            double_nucleotide = ""
        if triple_nucleotide == True:
            triple_nucleotide = f"Triple Nucleotides{Counter(split_dna(dna, block_size=3))}"
        else:
            triple_nucleotide = ""
        return single_nucleotide, double_nucleotide, triple_nucleotide
    except TypeError as e:
        logger.error ("Nucleotide count has failed! Check formatting: {}" .format(e))