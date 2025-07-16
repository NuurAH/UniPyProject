from Dictionaries import complement_table
#reverse complement manipulations

def reverse_complement(nucleotide):
    if nucleotide in complement_table:
        return nucleotide
    else:
        print("This is not a base" + " " + nucleotide)
        return " "

#remade the while loop so that it is more efficient, went from outputting 8x the wrong value (dummy nucleotides not in the dictionary) to outputting the exact amount
def reversing(start, dna, dna_list):
    dna_length = len(dna)
    while start < dna_length:
        dna_list.append(dna[start])
        complement = reverse_complement(dna_list[-1])
        for key, value in complement_table.items():
            if complement in value :
                complement_list.append(key)
        start+=1
        if start == dna_length:
            print(complement_list)
            return complement_list
    #Reversing the string

def reverse_print (complement_output, complement_list):   
    for base in complement_list:
        complement_output += base
    complement_output = complement_output[::-1]
    print(complement_output)

if __name__ == "__main__":
    dna = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGXGGGTTTCTCAGATAACTGGGCCXCCTGCGCTCAGGAGGCCTTCACCCTCXTGCTCTGGGTAAAGTTCAXTTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
    start = 0
    dna_list = []
    complement_list = []
    complement = 0
    complement_output = ""

    reversing(start, dna, dna_list)
    reverse_print(complement_output, complement_list)