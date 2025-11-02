from UniProjectToolkit.modules.GappingDNA import format_dna, split_dna
from UniProjectToolkit.modules.Dictionaries import acceptable_codons, start_codon, stop_codon, codon_table, complement_table
from UniProjectToolkit.modules.Translate import find, protein_print, create_frames, evaluate_frames
from UniProjectToolkit.modules.new_reverse import reverse_complement, reverse_string, complement
from UniProjectToolkit.modules.logger import logger

def create_sequence():
    title = []
    nucleotide_sequence = []
    fileOf = input("Which file would you like to read in?")
    with open(fileOf, "r") as f:
        for line in f:
            if ">" in line:
                title.append(line.strip())
            else:
                nucleotide_sequence.append(line.strip())
    nucleotide_sequence = ("\n".join(nucleotide_sequence))
    nucleotide_sequence = str(nucleotide_sequence)
    return title, nucleotide_sequence

def Forward_ORF(codon_table, acceptable_codons,start_codon, stop_codon, title,  nucleotide_sequence):
    run_one = find(codon_table, acceptable_codons, nucleotide_sequence)
    Orf_finder = evaluate_frames(start_codon, stop_codon, run_one)
    print(f"The largest ORF in forward sequence 1 {title} is {protein_print(Orf_finder)}")
    run_two = find(codon_table, acceptable_codons, nucleotide_sequence[1:])
    Orf_finder_2 = evaluate_frames(start_codon, stop_codon, run_two)
    print(f"The largest ORF in forward sequence 2 {title} is {protein_print(Orf_finder_2)}")
    run_three = find(codon_table, acceptable_codons, nucleotide_sequence[2:])
    Orf_finder_3 = evaluate_frames(start_codon, stop_codon, run_three)
    print(f"The largest ORF in forward sequence 3 {title} is {protein_print(Orf_finder_3)}")

def Reverse_ORF(codon_table, complement_table,start_codon, stop_codon, title,  nucleotide_sequence):
    run_four = reverse_complement(codon_table, complement_table, nucleotide_sequence)
    Orf_finder_4 = evaluate_frames(start_codon, stop_codon, run_four)
    print(f"The largest ORF in reverse sequence 1 of {title} is {protein_print(Orf_finder_4)}")
    run_five = reverse_complement(codon_table, complement_table, nucleotide_sequence[:-1])
    Orf_finder_5 = evaluate_frames(start_codon, stop_codon, run_five)
    print(f"The largest ORF in reverse sequence 2 of {title} is {protein_print(Orf_finder_5)}")
    run_six =reverse_complement(codon_table, complement_table, nucleotide_sequence[:-2])
    Orf_finder_6 = evaluate_frames(start_codon, stop_codon, run_six)
    print(f"The largest ORF in reverse sequence 3 of {title} is {protein_print(Orf_finder_6)}")



if __name__ == "__main__":
    title, nucleotide_sequence = create_sequence()
    Forward_ORF(codon_table, acceptable_codons, start_codon, stop_codon, title, nucleotide_sequence)
    Reverse_ORF(codon_table, complement_table, start_codon, stop_codon, title, nucleotide_sequence)

