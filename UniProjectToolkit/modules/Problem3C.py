from UniProjectToolkit.modules.Problem3B import fileAmino

def aminoAppear(amino_list, amino_acids):
    new_list = []
    counter = 0
    set_list = []
    counter_list = []
    
#need to clean the data, so I have to strip it and remove all the spaces        
    stripped_amino = [x.strip() for x in amino_list]
#print(stripped_amino)

# check inside of each string without a space to see if the amino acid code is in there
    for x in stripped_amino:
        for y in amino_acids:
            if y in x:
                new_list.append(y)
#checking to see if the list printed the right output
#print(new_list)

#now I need to see how many times each amino acid has appeared pretty much the same method as exercise 2
    new_set = set(new_list)
    set_list = list(new_set)
    while counter < len(new_set):
        if new_set & set(counter_list):
          counter+=1
        else:
            counter_list.append(new_list.count(set_list[counter]))
            counter+=1
    final_list = zip(set_list,counter_list)
    print(dict(final_list))


if __name__ == "__main__":
#List of variables
    amino_acids = [ "ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", "HIS", "ILE", "LEU", "LYS", "MET", "PHE", "PRO", 
               "SER", "THR", "TRP", "TYR", "VAL"]
    amino_list = fileAmino()
    aminoAppear(amino_list, amino_acids)