import re
# import function re
seq = 'ATGCCATCGACTACGATCAATCGAGGGCC'
# set up a DNA sequence
cut_DNA = re.findall(r'GAATTC',seq)
# extract Ecol1 DNA sequence from the string
print('the fragment number =', len(cut_DNA)+1)
# print the fragment DNA number