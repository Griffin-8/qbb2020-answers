#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys 
import pandas as pd
import numpy as np

file = sys.argv[1]

gwas = pd.read_csv(sys.argv[1] , sep = "\s+")

gwas['logP'] = -1 * np.log10(gwas['P'])

gwas_sorted = gwas.sort_values(by = "P")
gwas_sorted['uniform_points'] = range(0, len(gwas_sorted))
gwas_sorted['uniform_pval'] = (gwas_sorted['uniform_points'] + 1) / len(gwas_sorted)
gwas_sorted['uniform_logP'] = -1 * np.log10(gwas_sorted['uniform_pval'])

gwas['snp_index'] = range(len(gwas))

fig, ax = plt.subplots()

ax.scatter(gwas_sorted["uniform_logP"], gwas_sorted["logP"])
ax.plot([8,0], [8, 0], color = "black")

plt.xlim([0, 8])
plt.ylim([0, 10])
plt.xlabel("Expected -log10(p-value)")
plt.ylabel("Observed -log10(p-value)")
    

plt.title(sys.argv[3])


plt.savefig(sys.argv[2], dpi=300)  