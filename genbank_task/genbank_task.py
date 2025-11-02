from UniProjectToolkit.utils.entrez_fetch import TranscriptIdError, fetch_transcript_record
from UniProjectToolkit.modules.logger import logger
from UniProjectToolkit.modules.Translate import find, protein_print
from UniProjectToolkit.modules.Dictionaries import codon_table, complement_table, stop_codon, start_codon, acceptable_codons
import requests
import os

def DNA_file():
    """What this does, is that it takes the fetch_entrez API and adapts it so that 
      each of the fields is now a variable These variables can have None, to account 
    for the different types of inputs we can have. It then converts all of the fields into
    a dictionary and returns it A second function has also been added to save different types of files
    The aim of this is to ensure that an unedited XML file can be fetched along with a dictionary
    Furthermore, the XML can be parsed to include more information, like protein transcripts"""
        # Example usage: fetch a GenBank transcript record (e.g. COL5A1 mRNA RefSeq)
    record_id = input(f"please input an ID ")
    record = fetch_transcript_record(record_id)

    # Top-level metadata fields from the GenBank record
    GB_Acession_Version = record['GBSeq_accession-version']   # Accession with version, e.g. "NM_000093.5"
    GB_Definition = record['GBSeq_definition']          # Definition line, e.g. "collagen alpha-1(V) chain (COL5A1), mRNA"
    GB_Keyword = record['GBSeq_keywords']         # Keywords list, e.g. ["RefSeq", "mRNA", "collagen"]

    # Print the raw nucleotide sequence in uppercase
    GB_Seq =record['GBSeq_sequence']
    GB_Seq_Upper = GB_Seq.upper()
    GB_Gene = None
    GB_Start_coordinate = None
    GB_End_coordinate = None
    Intermediate_data = find((record['GBSeq_sequence']), codon_table)
    GB_Protein_seq = protein_print(Intermediate_data)
    # Iterate over all annotated features in the feature table
    for line in record['GBSeq_feature-table']['GBFeature']:

        # --- Gene feature ---
        if line['GBFeature_key'] == 'gene':
            # Gene symbol, e.g. "COL5A1"
            GB_Gene = line['GBFeature_quals']['GBQualifier'][0]['GBQualifier_value']
            # HGNC ID (sometimes appears as "HGNC:HGNC:2197", so fix formatting)
            GB_Gene = (line['GBFeature_quals']['GBQualifier'][4]['GBQualifier_value']
                  .replace("HGNC:HGNC:", "HGNC:"))

        # --- Coding sequence (CDS) feature ---
        elif line['GBFeature_key'] == 'CDS':
            # Start coordinate of coding region on the transcript
            GB_Start_coordinate = (line['GBFeature_intervals']['GBInterval']['GBInterval_from'])
            # End coordinate of coding region on the transcript
            GB_End_coordinate =(line['GBFeature_intervals']['GBInterval']['GBInterval_to'])

    #create dictionary of values and keys
    GB_keys = ["Accession", "Definition", "Keyword", "DNA_seq", "Gene", "Start_coord", "End_coord", "Protein_Seq"]
    GB_Values = [GB_Acession_Version, GB_Definition, GB_Keyword, GB_Seq_Upper, GB_Gene, GB_Start_coordinate, GB_End_coordinate, GB_Protein_seq]
    GB_Dict = dict(zip(GB_keys, GB_Values))

    return GB_Dict, GB_Acession_Version

def save_output_to_file(GB_Acession_Version, GB_dict):
    file_type = input(f" Please select 1 if you want to download an XML of your transcript or 2 if you want to download a dictionary ")
    #save XML File
    if file_type == "1":   
            """""This essentially checks the directories for Output and then if it doesn't exist, it creates it
            If the whole xml is requested, it reruns the fetch query for the acession, should always work,
             although now it does run the fetch query twice if you do want to save the file
              For the dictionary file, it essentially just downloads the output, depending on what parameters are added """
            if "Output_files" in os.listdir():
                os.chdir("Output_files")
                location = os.getcwd()
            else:
                os.mkdir("Output_files")
                os.chdir("Output_files")
                location = os.getcwd()
            xml_file = os.path.join(location, f"{GB_Acession_Version}.xml") 
            # Base URL for NCBI Entrez EFetch
            url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
            params = {
            "db": "nucleotide",   # NCBI nucleotide database
            "id": GB_Acession_Version,  # transcript accession
            "retmode": "xml"      # request XML format for easier parsing
        }
            try:
            # Perform GET request to NCBI EFetch
                r = requests.get(url, params=params)
                r.raise_for_status()  # Raise an exception for HTTP errors
                with open(xml_file, "w", encoding="utf-8") as file:
                    file.write(r.text)
                    print ("XML saved")
            except requests.exceptions.RequestException as e:
                logger.error(f"Error fetching transcript {GB_Acession_Version}: {e}")  
    elif file_type == "2":
        if "Output_files" in os.listdir():
            os.chdir("Output_files")
            location = os.getcwd()
        else:
            os.mkdir("Output_files")
            os.chdir("Output_files")
            location = os.getcwd()
        dict_file = os.path.join(location, f"{GB_Acession_Version}.txt") 
        with open(dict_file, "w", encoding="utf-8") as file:
            for key, value in GB_Dict.items():
                 file.write(f"{key}: {value} \n")
            print ("dictionary file saved")
    else:
         logger.error(f"Wrong answer!")

if __name__ == "__main__":
    GB_Dict, GB_Acession_Version = DNA_file()
    save_output_to_file(GB_Acession_Version, GB_Dict)
