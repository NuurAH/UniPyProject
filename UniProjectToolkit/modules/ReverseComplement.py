from Dictionaries import complement_table
from Translate import loop , find, protein_print

#reverse complement manipulations

def reverse_complement(nucleotide):
    if nucleotide in complement_table:
        return nucleotide
    else:
        print(f"this is not a base {nucleotide} ")
        return " "

def complementary(complement, complement_list, dna):
    commence = 0
    dna_length = len(dna)
    dna_upper = dna.upper()
    and_list =[]
    for commence in range (0, dna_length):
        and_list.append(dna_upper[commence])
        complement = reverse_complement(and_list[-1])
        for key, value in complement_table.items():
            if complement in value :
                complement_list.append(key)
        commence+=1
    if commence == dna_length:
        # print(complement_list)
        return complement_list

def manipulation(rComplement, complement_list):
    complement_output = ""
    rComplement = ""
    for plement in complement_list:
        complement_output += plement
        rComplement = complement_output[::-1]
    return rComplement



if __name__ == "__main__":
    dna = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGXGGGTTTCTCAGATAACTGGGCCXCCTGCGCTCAGGAGGCCTTCACCCTCXTGCTCTGGGTAAAGTTCAXTTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
    start = 0
    dna_list = []
    complement_list = []
    complement = 0
    complement_output = ""
    rComplement = ""

    complementary(complement, complement_list, dna)
    rComplement = manipulation(rComplement, complement_list)
    protein_print(rComplement)