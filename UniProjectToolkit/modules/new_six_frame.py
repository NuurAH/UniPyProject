from UniProjectToolkit.modules.Translate import find, protein_print
from UniProjectToolkit.modules.Dictionaries import codon_table, acceptable_codons, start_codon, stop_codon, complement_table
from UniProjectToolkit.modules.new_reverse import reverse_complement

def six_frame_forward(codon_table, acceptable_codons, dna=str):

    run_one = find(codon_table, acceptable_codons, dna)
    run_two = find(codon_table,acceptable_codons, dna[1:])
    run_three =find(codon_table,acceptable_codons,dna[2:])
    
    print(f"Forward \n 1 {protein_print(run_one)} \n 2 {protein_print(run_two)} \n 3 {protein_print(run_three)}" )


def six_frame_reverse(codon_table, complement_table, dna=str):
    run_four = reverse_complement(codon_table, complement_table, dna)
    run_five = reverse_complement(codon_table,complement_table, dna[:-1])
    run_six =reverse_complement(codon_table,complement_table,dna[:-2])
    print(f"Reverse \n 4 {protein_print(run_four)} \n 5 {protein_print(run_five)} \n 6 {protein_print(run_six)}" )


if __name__ == "__main__":
    dna = "aggagtaagcccttgcaactggaaatacacccattg"
    six_frame_forward(codon_table,acceptable_codons,dna)
    six_frame_reverse(codon_table,complement_table,dna)
