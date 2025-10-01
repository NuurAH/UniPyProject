''' In this code, I am finding the length of the DNA sequence, then I am making my block size which is 3 in this case. I have start = 0 
A list is then made, I append the first value and then add blocking which is the same value as block size however
this value will always be greater than the first value by the block size.  I need them to be stored separately so that I can add block size to both start and blocking so that
both values increase by block size. This causes my while loop, which evaluates the length of dna_length, to loop and break up the string by my block size and
add it to the list. The second loop coverts the list back into a string and finally the whitespace at the front is removed using the strip function '''
#redone to make it more modular and also, blocking was a bit redundant so I removed it
#loops
def gapping_dna(dna):
   dna_length = len(dna)
   dna_list = []
   start = 0
   block_size = 3
   for nucleotide in range (start, dna_length):
         dna_list.append(dna[start:start+ block_size]) 
         start += block_size
   split_dna = ""
   for base in dna_list:
      split_dna += (" " + (base) + " ") 
   formatted_dna = split_dna.strip()
   return formatted_dna

