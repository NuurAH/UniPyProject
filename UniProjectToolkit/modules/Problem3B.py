def fileAmino(amino_list, interest):
    fileOf = input("Which file would you like to read in?")
    interest = open(fileOf, "rt")
    amino_acid = input("Put in a 3-letter code for an amino acid, and I'll tell you how many lines contain it")
    with interest:
        for codon,text in enumerate(interest):
            if amino_acid in text:
                amino_list.append(codon)
    amino_count = len(amino_list)
    if amino_count == 0:
        print(f"Warning!, the amino acid, {amino_acid}, does not appear! Have you made an error?")
    elif amino_count == 1:
        print(f"The amino acid, {amino_acid}, appears once")
    elif amino_count >1:
        print(f"The amino acid, {amino_acid}, appears {amino_count} times")


if __name__ == "__main__":
    fileOf = ""
    interest = 0
    amino_List = []
    fileAmino(amino_List, interest)
