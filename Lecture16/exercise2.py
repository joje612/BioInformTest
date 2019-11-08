#!/usr/bin/python3
#import all necessary packages for use throughout the script
import os, sys
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import shutil

#get the fasta file
shutil.copy("/localdisk/data/BPSM/Lecture16_AI/alignment.txt", "alignment.txt")

MSA_input = open('alignment.txt')

aligned_seqs = []
counter =0
# check what length they are as we go
for line in MSA_input:
    counter += 1
    print("Sequence",counter,"was",len(line.rstrip("\n")),"long")
    aligned_seqs.append(line.rstrip("\n"))

align_length = len(aligned_seqs[0])
uniques_per_column = []

print("alignment length = " + str(align_length))

# Look at each column
for col_number in range(align_length):
    column = []
    for seq in aligned_seqs:
        aa = seq[col_number]
        if aa != '-':  # ignore gaps
            column.append(seq[col_number])
         
    uniques = len(set(column))
    print("Uniques are " + str(len(set(column))))
    uniques_per_column.append(uniques)
    
window = 10
numbers_to_plot = []

for start in range(len(uniques_per_column) - window):
    win = uniques_per_column[start:start+window]
    score = sum(win) / len(win)
    numbers_to_plot.append(score)

plt.figure(figsize=(15,8))
plt.xlim(0,len(numbers_to_plot))
plt.plot(numbers_to_plot,linewidth=3,color="green")
plt.title('EXERCISE 2')
plt.ylabel('Unique amino acid residues')
plt.xlabel('Residue position')
plt.savefig("Lecture16_Exercise_2.png",transparent=True)
plt.show()
