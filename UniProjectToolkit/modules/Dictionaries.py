complement_table = {
    "A" : "T",
    "T" : "A",
    "G" : "C",
    "C" : "G",
    "a" : "t",
    "t" : "a",
    "g" : "c",
    "c" : "g"
}
codon_table = {
    "F" : ["TTT","TTC"],
    "L" : ["TTA", "TTG", "CTT", "CTA", "CTG" ],
    "I" : ["ATT", "ATC", "ATA"],
    "M" : ["ATG"],
    "V" : ["GTT", "GTC", "GTG", "GTA"],
    "S" : ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
    "P" : ["CCT", "CCC", "CCA", "CCG"],
    "T" : ["ACT", "ACC", "ACA", "ACG"],
    "A" : ["GCT", "GCC", "GCA", "GCG"],
    "Y" : ["TAT", "TAC"],
    "*" : ["TAA", "TAG", "TGA"],
    "H" : ["CAT", "CAC"],
    "Q" : ["CAA", "CAG"],
    "N" : ["AAT", "AAC"],
    "K" : ["AAA", "AAG"],
    "D" : ["GAT", "GAC"],
    "E" : ["GAA", "GAG"],
    "C" : ["TGT", "TGC"],
    "W" : ["TGG"],
    "R" : ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG" ],
    "G" : ["GGT", "GGC", "GGA", "GGG" ]
}

acceptable_codons = ["F", "L", "I", "M", "V", "S", "P", "T", "A", "Y", "*", "H", "Q", "N", "K", "D", "E", "C", "W", "R", "G"]
start_codon = "M"
stop_codon = "*"
