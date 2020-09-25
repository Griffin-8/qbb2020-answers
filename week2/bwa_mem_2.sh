#!/bin/bash

for SAMPLE in 09 11 23 24 27 31 35 39 62 63
do
	bwa mem -R "@RG\tID:${SAMPLE}\tSM:${SAMPLE}" ./sacCer3.fa ./A01_${SAMPLE}.fastq > align_${SAMPLE}.bam
done 
