#!/bin/bash
​
for SAMPLE in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46
do
	python Manhattan_plot_gen.py "./plink_assoc_pheno/plink.P${SAMPLE}.assoc.linear" "P${SAMPLE}_Manhattan.jpg" "P${SAMPLE}"
done 