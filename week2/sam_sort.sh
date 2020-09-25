#!/bin/bash

for SAMPLE in 11 23 24 27 31 35 39 62 63
do
	samtools sort -o align_${SAMPLE}_sorted.bam ./align_${SAMPLE}.bam
done 
