from Dictionaries import codon_table
from Dictionaries import complement_table
from Reverse_Complement import reverse_complement


def find(codon_table, dna_list, extracted_codons):
    for key, value in codon_table.items():
        if dna_list[-1] in value:
            extracted_codons.append(key)
def loop(dna, dna_list, block_size, start):
    dna_length = len(dna)
    dna_upper = dna.upper()
    while start <= dna_length :
        dna_list.append(dna_upper[start:(start+block_size)]) 
        find(codon_table, dna_list, extracted_codons)
        start += block_size
    if start == dna_length:
        dna_list.append(dna_upper[start:(start+block_size)]) 
        find(codon_table, dna_list, extracted_codons)
        return dna_list, extracted_codons

#reverse complement manipulations
def manipulation(rComplement, complement_list):
    complement_output = ""
    rComplement = ""
    for plement in complement_list:
        complement_output += plement
        rComplement = complement_output[::-1]
    return rComplement
def protein_print(extracted_codons):
    protein_list = ""
    for base in extracted_codons:
        protein_list += base
    print(protein_list)

def complementary(complement, complement_list):
    commence = 0
    dna_length = len(dna)
    dna_upper = dna.upper()
    and_list =[]
    while commence < dna_length:
        and_list.append(dna_upper[commence])
        complement = reverse_complement(and_list[-1])
        for key, value in complement_table.items():
            if complement in value :
                complement_list.append(key)
        commence+=1
    if commence == dna_length:
        # print(complement_list)
        return complement_list

if __name__ == "__main__" :
    dna = "aggagtaagcccttgcaactggaaatacacccattg"
    complement = 0
    block_size = 3
    dna_list = []
    complement_list = []
    extracted_codons = []
    tList = []
    rComplement = ""
    start = 0
    #forward
    while start < (2*block_size):
        if start < block_size:
            print (f"forward run {1 + start}")
            loop(dna, dna_list, block_size, start)
            protein_print(extracted_codons)
            extracted_codons = []
            start +=1
        #reverse
        if start >=block_size:
            print(f"reverse run {1 + start - block_size}")
            complementary(complement, complement_list)
            rComplement = manipulation(rComplement, complement_list)
            loop(rComplement, tList, block_size, start = (start - block_size))
            protein_print(extracted_codons)
            complement_list = []
            extracted_codons = []
            start +=1