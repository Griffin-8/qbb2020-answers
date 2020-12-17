#!/bin/bash
for SAMPLE in 83 86 88 89 90 93 94 97
do
    cut -c 11- SRR4921${SAMPLE}.kraken |awk '{gsub(";","\t"); print}' > day_${SAMPLE}_tab.kraken
done