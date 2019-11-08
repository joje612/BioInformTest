#!/usr/bin/python3
#import all necessary packages for use throughout the script
import os, sys
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import shutil

#get the fasta file
shutil.copy("/localdisk/data/BPSM/Lecture16_AI/ecoli.txt", "ecoli.txt")

#read and check the fasta file
ecoli = open("ecoli.txt").read().replace('\n', '').upper()[0:100000]

window = 1000
a = []

for start in range(len(ecoli) - window):
   win = ecoli[start:start+window]
   a.append((win.count('A') + win.count('T'))/ window)
  
plt.figure(figsize=(20,10))
plt.plot(a, label="AT Content")
plt.ylabel('Proportional fraction of AT Content')
plt.xlabel('Position on genome')
plt.legend()

plt.savefig("Lecture16_ATContent.png",transparent=True)
plt.show()



