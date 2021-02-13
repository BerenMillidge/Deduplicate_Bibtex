# simple script to parse and deduplicate a bib file -- i.e. remove duplicate entries with the same key

import sys
import os

def create_bibdict(lines):
    key_dict = {}
    for i,line in enumerate(lines):
        if line.startswith("@"):
            splits = line.split("{")
            if len(splits) > 1:
                key = splits[1][0:-2]
                bib_string = str(line)
                ended = False
                j = i
                while not ended:
                    line = lines[j+1]
                    if line.startswith("}"):
                        ended = True
                    bib_string += line
                    j +=1 
                key_dict[key] = bib_string
    return key_dict

def write_to_output_file(output_filename,key_dict):
    f = open(output_filename, "w+")
    for (k,v) in key_dict.items():
        f.write(v)
        f.write("\n")
    
if __name__ == "__main__":
    filename = ""
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    output_filename = "deduped.bib"
    if len(sys.argv) > 2:
        output_filename = sys.argv[2]

    with open(filename) as f:
        lines = f.readlines()
    key_dict = create_bibdict(lines)
    write_to_output_file(output_filename, key_dict)



        
        


