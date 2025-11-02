#new and improved code!
from UniProjectToolkit.modules.logger import logger

def split_dna(dna, block_size=int):
    try:
        if not isinstance(block_size, int):
            raise TypeError("block size must be an integer")
        dna_list = [dna[base:base+block_size] for base in range (0, len(dna), block_size)]
        return dna_list
    except TypeError as e:
        logger.error( "DNA gapping has failed with exception: {}".format(e) )
        raise

def format_dna(dna, block_size=int):
    try:
        formatted_dna = " ".join(split_dna(dna,block_size))
        return formatted_dna
    except Exception as e:
        logger.error("Formatting DNA failed: {}" .format(e))
        raise