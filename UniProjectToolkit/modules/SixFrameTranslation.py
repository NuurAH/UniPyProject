from UniProjectToolkit.modules.Dictionaries import codon_table, complement_table
from UniProjectToolkit.modules.ReverseComplement import reverse_complement, complementary, manipulation
from UniProjectToolkit.modules.Translate import find, loop, protein_print

if __name__ == "__main__" :
    dna = "aggagtaagcccttgcaactggaaatacacccattg"
    complement = 0
    block_size = 3
    dna_list = []
    complement_list = []
    extracted_codons = []
    reverseList = []
    rComplement = ""
    start = 0
    #forward
    while start < (2*block_size):
        if start < block_size:
            print (f"forward run {1 + start}")
            loop(dna, dna_list, block_size, extracted_codons, start)
            protein_print(extracted_codons)
            extracted_codons = []
            start +=1
        #reverse
        if start >=block_size:
            print(f"reverse run {1 + start - block_size}")
            complementary(complement, complement_list, dna)
            rComplement = manipulation(rComplement, complement_list)
            loop(rComplement, reverseList, block_size, extracted_codons, start = (start - block_size))
            protein_print(extracted_codons)
            complement_list = []
            extracted_codons = []
            start +=1