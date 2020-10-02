#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys 
import pandas as pd
import numpy as np
file = sys.argv[1]

gwas = pd.read_csv(sys.argv[1] , sep = "\s+")

gwas['logP'] = -1 * np.log10(gwas['P'])
gwas['snp_index'] = range(len(gwas))
df_subset = gwas.query('logP > 5')


gwas['snp_index'] = range(len(gwas))
CHR = ['chrI' , 'chrII', 'chrIII', 'chrIV', 'chrV', 'chrVI', 'chrVII', 'chrVIII','chrIX', '23', 'chrXI', 'chrXII', 
      'chrXIII', 'chrXIV', 'chrXV', 'chrXVI', '26']
fig, ax = plt.subplots()

for chr in CHR: 
    ax.scatter(gwas["snp_index"][gwas["CHR"] == chr], gwas["logP"][gwas["CHR"] == chr], marker = '.')
    ax.scatter(df_subset.snp_index, df_subset.logP, color="black", marker = '.')
plt.xlabel("SNPs")
plt.ylabel("-log10(p-value)")
plt.ylim(0, 50)
plt.title(sys.argv[3])


plt.savefig(sys.argv[2], dpi=300)  
