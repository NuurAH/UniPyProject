from UniProjectToolkit.modules.Dictionaries import codon_table, acceptable_codons, stop_codon
#functions   
def find(codon_table, dna_list, extracted_codons):
    for key, value in codon_table.items():
        if dna_list[-1] in value:
            extracted_codons.append(key)
    return(extracted_codons)

def loop(dna, dna_list, extracted_codons):
    start = 0
    dna_length = len(dna)
    dna_upper = dna.upper()
    block_size = 3 
    for nucleotide in range (0, (int(dna_length/block_size) )):
        dna_list.append(dna_upper[start:(start+block_size)]) 
        find(codon_table, dna_list, extracted_codons)
        start += block_size
    return dna_list, extracted_codons


def protein_print(extracted_codons):
    protein_string = ""
    for base in extracted_codons:
        protein_string += base
        if base not in acceptable_codons:   
            print(f"{base} is not an acceptable codon!")
        elif base == stop_codon:
            break
    print(protein_string)
    return(protein_string)

#ctrl forward slash comments sections and can uncomment

# if __name__ == "__main__":
#     dna = "aggagtaagcccttgcaactggaaatacacccattg"
#     dna_length = len(dna)
#     dna_list = []
#     extracted_codons = []
#     loop(dna,dna_list, extracted_codons, find)
#     protein_print(extracted_codons)


