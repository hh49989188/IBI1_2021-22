import re
file_name=input('give a name to the file :')
# Let users imput file name
output_file = open(file_name,'w')
origin_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
# Open the output and origin file
list1 = {}
for line in origin_file:
    line = line.rstrip()
# Is a copy of the string, and removes leading and postfix characters.
    if line.startswith('>'):
        a=re.search(r'gene:(.+?\s)', line)
        gene_sequence = "\n"+'>'+a.group(1)
        list1[gene_sequence] = ""
#  If the line is gene name, it will become white space
    else:
        list1[gene_sequence] = list1[gene_sequence]+line
# Because gene name will appear after '>', we can utilize it to collect gene sequence

for i in list1.keys():
    if re.search('GAATTC',list1[i]):
        target_DNA = re.findall('GAATTC',list1[i])
# extract DNA swquence can be cut by Ecol1
        fragment = str(len(target_DNA)+1)
# caculate the number of cut DNA fragments
        name_and_number = i+" "+fragment
        name_and_number = name_and_number.strip()
# combine gene name and gene sequence together
        output_file.write(name_and_number+"\n"+list1[i]+'\n')
# output the result