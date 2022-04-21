import re
# import the function
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
# read the file and transform data into dictionary
list1 = {}
# list1 for the collection of gene name
for line in file:
    line = line.rstrip()
# Is a copy of the string, and removes leading and postfix characters.
    if line.startswith('>'):
            a = re.search(r'gene:(.+?\s)', line)
            gene_sequence = "\n" + '>' + a.group(1)
            list1[gene_sequence] =""
# If the line is gene name, it will become white space
    else:
            list1[gene_sequence] = list1[gene_sequence] + line
# Because gene name will appear after '>', we can utilize it to collect gene sequence
output_file = open('cut_genes.fa', 'w')
for i in list1.keys():
    if re.search('GAATTC',list1[i]):
        target_DNA = re.findall('GAATTC', list1[i])
# extract DNA swquence can be cut by Ecol1
        DNA_length = str(len(list1[i]))
# Caculate the DNA length which can be cut by Ecol1, obtain this cord from http://events.jianshu.io/p/1c81152e445e
        DNA_and_length = i + " " + DNA_length
        DNA_and_number = DNA_and_length.strip()
# combine DNA length and gene sequence togethe
        output_file.write(DNA_and_number + "\n" + list1[i] + '\n')
# combine length and DNA sequence together and out put them in a dictionary