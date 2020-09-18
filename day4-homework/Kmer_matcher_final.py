#!/usr/bin/env python3

import sys 

from fasta_iterator_class import FASTAReader

target_seqs = FASTAReader(open(sys.argv[1]))
droyak_seqs = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3])

kmers = {}

for seq_id, sequence in target_seqs:
    for i in range(0, len(sequence) - k+1):
        kmer = sequence[i:i +k]
        if kmer in kmers:
            kmers[kmer].append(seq_id)
            kmers[kmer].append(i)
        else:
            kmers[kmer] = [seq_id, i]
count = 0
for seq_id, sequence in droyak_seqs:
    for i in range(0, len(sequence) - k+1):
        kmer_q = sequence[i:i + k]
        if kmer_q in kmers:
            print("target seq {},\t query start: {},\t kmer: {}".format(kmers[kmer_q], i, kmer_q))
            count += 1
        if count == 1000:
            break