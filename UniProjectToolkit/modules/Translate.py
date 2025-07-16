from UniProjectToolkit.modules.Dictionaries import codon_table
#functions   
def find(codon_table, dna_list, extracted_codons):
    for key, value in codon_table.items():
        if dna_list[-1] in value:
            extracted_codons.append(key)

def loop(dna, dna_list, block_size, extracted_codons, start):
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


def protein_print(extracted_codons):
    protein_list = ""
    for base in extracted_codons:
        protein_list += base
    print(protein_list)

#ctrl forward slash comments sections and can uncomment

if __name__ == "__main__":
    dna = "aggagtaagcccttgcaactggaaatacacccattg"
    dna_length = len(dna)
    block_size = 3
    start = 0
    dna_list = []
    extracted_codons = []
    loop(dna,dna_list, block_size, extracted_codons, start)
    protein_print(extracted_codons)



