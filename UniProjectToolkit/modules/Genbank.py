def NewLine(start, dna, dna_list,genPal):
   GenScale(dna)
   startstring = str(start)
   startstring = len(startstring)
   #I want this to scale so the genPal should create spaces as much as the distance between the leading figure and the last figure
   if start%60 == 0 and genPal - startstring == 1 :
      dna_list.append("\n" + (" " + " " * 2*((genPal-1) - startstring)) + str(start + 1))
   elif start%60 == 0 and genPal - startstring >= 2 :
      dna_list.append("\n" + (" " + " " *((genPal-1) - startstring)) + str(start + 1))
   elif start%60 == 0 and startstring == genPal:
         dna_list.append("\n" + str(start + 1))
        


def GenerateBank(start, dna, dna_list, block_size, genPal):
   dna_length = len(dna)
   while start < dna_length :
      if start == 0:
         dna_list.insert (0, str(1))
      dna_list.append(dna[start:(start+block_size)]) 
      start += block_size
      NewLine(start, dna, dna_list, genPal)

def SplitDNA(dna_list, dna, start, split_dna, genPal):
   GenScale(dna)
   for base in dna_list:
      if start == 0 :
         split_dna += (f"{" "* (genPal-2)} {base} ") 
      elif start%60 == 0:
         split_dna += (f" {base} ") 
   formatted_dna = split_dna
   print(formatted_dna.lower())

def GenScale(dna):
   dna_length = len(dna)
   genPal = len(str(dna_length))
   genPal = int(genPal) 
  
   return genPal

if __name__ == "__main__":
#variable list
   dna = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGG" \
   "GCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAA" \
   "ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAAT" \
   "CTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTT" \
   "GCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAA" \
   "AGTACGAGATTTAGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAAACAGCTATAATTT" \
   "TGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCAAAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCC" \
   "GAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACA" \
   "TTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAG"
   block_size = 10
   start = 0
   dna_list = []
   split_dna = ""
   genPal = 0

   
#    #Chaining function
   genPal = GenScale(dna)
   GenerateBank(start, dna, dna_list, block_size, genPal)
   SplitDNA(dna_list, dna, start, split_dna, genPal)