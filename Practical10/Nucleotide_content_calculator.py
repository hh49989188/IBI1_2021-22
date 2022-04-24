DNA_input = input("Please type your DNA sequence here:")
# Let Users imput their DNA sequence
import re
# import reading function
DNA_sequence = ''.join(re.findall(r'[A-Za-z]', DNA_input))
# Extract DNA sequence from the input string and combine them together
A_sequence = ''.join(re.findall(r'A', DNA_sequence))
T_sequence = ''.join(re.findall(r'T', DNA_sequence))
C_sequence = ''.join(re.findall(r'C', DNA_sequence))
G_sequence = ''.join(re.findall(r'G', DNA_sequence))
# Extract A/T/C/G sequence from the DNA string and combine each of them together
def f(x):
    y = x / len(DNA_sequence)
    return y

x = len(A_sequence)
z = f(x)
print(z)
print("is the A percentage")

x = len(T_sequence)
z = f(x)
print(z)
print("is the T percentage")

x = len(C_sequence)
z = f(x)
print(z)
print("is the C percentage")

x = len(G_sequence)
z = f(x)
print(z)
print("is the G percentage")
# Caculate the proportion of each nucleotide in the sequence and print them
