def countGCpercentage(dna):
    dna_length = len(dna)
    dna_lower = dna.lower()
    g_content = dna_lower.count("g")
    c_content = dna_lower.count("c")
    counter = g_content + c_content
    GC_percentage = round((counter / dna_length) * 100)
    return GC_percentage