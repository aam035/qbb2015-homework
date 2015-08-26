Day 1 hmwk

2. fastqc data
/Users/cmdb/qbb2015-homework/day1 $ fastqc SRR072893.fastq 
/Users/cmdb/qbb2015-homework/day1 $ fastqc 

Filename	SRR072893.fastq
File type	Conventional base calls
Encoding	Sanger / Illumina 1.9
Total Sequences	21892898
Sequences flagged as poor quality	0
Sequence length	40
%GC	53

3. hisat function
/Users/cmdb/qbb2015-homework/day1 $  hisat -p 4 -x /Users/cmdb/qbb2015/genomes/BDGP6 -U /Users/cmdb/qbb2015/day1/SRR072893.fastq -S maps_reads.sam
21892898 reads; of these:
  21892898 (100.00%) were unpaired; of these:
    4868452 (22.24%) aligned 0 times
    16824102 (76.85%) aligned exactly 1 time
    200344 (0.92%) aligned >1 times
77.76% overall alignment rate

4.sam tools
converting .sam to .bam
/Users/cmdb/qbb2015-homework/day1 $ samtools view -bS maps_reads.sam > maps_reads.bam
/Users/cmdb/qbb2015-homework/day1 $ ls -l
total 18513048
-rw-r--r--  1 cmdb  staff  4582672018 Aug 24 16:36 SRR072893.fastq
-rw-r--r--  1 cmdb  staff      391926 Aug 25 21:48 SRR072893_fastqc.html
-rw-r--r--  1 cmdb  staff      527013 Aug 25 21:48 SRR072893_fastqc.zip
-rw-r--r--  1 cmdb  staff           0 Aug 25 22:06 map_reads.sam
-rw-r--r--  1 cmdb  staff   915593524 Aug 25 22:27 maps_reads.bam
-rw-r--r--  1 cmdb  staff  3979489115 Aug 25 22:12 maps_reads.sam

converting .bam to sort
/Users/cmdb/qbb2015-homework/day1 $ samtools sort maps_reads.bam maps_reads.sort.bam
[bam_sort_core] merging from 7 files...
/Users/cmdb/qbb2015-homework/day1 $ ls -l
total 19704608
-rw-r--r--  1 cmdb  staff  4582672018 Aug 24 16:36 SRR072893.fastq
-rw-r--r--  1 cmdb  staff      391926 Aug 25 21:48 SRR072893_fastqc.html
-rw-r--r--  1 cmdb  staff      527013 Aug 25 21:48 SRR072893_fastqc.zip
-rw-r--r--  1 cmdb  staff           0 Aug 25 22:06 map_reads.sam
-rw-r--r--  1 cmdb  staff   915593524 Aug 25 22:27 maps_reads.bam
-rw-r--r--  1 cmdb  staff  3979489115 Aug 25 22:12 maps_reads.sam
-rw-r--r--  1 cmdb  staff   610076021 Aug 25 22:36 maps_reads.sort.bam.bam

converting sort to index
/Users/cmdb/qbb2015-homework/day1 $ samtools index maps_reads.bam.bai
/Users/cmdb/qbb2015-homework/day1 $ ls -l
total 19704608
-rw-r--r--  1 cmdb  staff  4582672018 Aug 24 16:36 SRR072893.fastq
-rw-r--r--  1 cmdb  staff      391926 Aug 25 21:48 SRR072893_fastqc.html
-rw-r--r--  1 cmdb  staff      527013 Aug 25 21:48 SRR072893_fastqc.zip
-rw-r--r--  1 cmdb  staff           0 Aug 25 22:06 map_reads.sam
-rw-r--r--  1 cmdb  staff   915593524 Aug 25 22:27 maps_reads.bam
-rw-r--r--  1 cmdb  staff           0 Aug 25 22:50 maps_reads.bam.bai
-rw-r--r--  1 cmdb  staff  3979489115 Aug 25 22:12 maps_reads.sam
-rw-r--r--  1 cmdb  staff   610076021 Aug 25 22:36 maps_reads.sort.bam.bam

5.quantitate
/Users/cmdb/qbb2015-homework/day1 $ stringtie -p 4 -x maps_reads.sort.bam -e -G maps_reads.quant

6. #!/bin/bash

echo "This Bash script should echo the commands to run FastQC and HISAT on all 24 samples.  e.g."
echo ""
echo "fastqc /Users/cmdb/qbb2015/rawdata/SRR072893.fastq.gz -o /Users/cmdb/qbb2015/assignments/day1-homework"
echo "hisat -p 4 -x /Users/cmdb/qbb2015/genomes/BDGP6 -U /Users/cmdb/qbb2015/rawdata/SRR072893.fastq.gz -S SRR072893.sam"
echo ""
echo "However, there are 6 mistakes!"

FASTQ_DIR="/Users/cmdb/qbb2015/rawdata"
OUTPUT_DIR="/Users/cmdb/qbb2015/assignments/day1-homework"

GENOME_DIR="/Users/cmdb/qbb2015/genomes"
SAMPLE_PREFIX="SRR072"
ANNOTATION="BDGP6"

CORES=4

for i in {893..916}
do
  echo fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i.fastq.gz -o $OUTPUT_DIR
  echo hisat -p 4 -x $GENOME_DIR/$ANNOTATION -U $FASTQ_DIR/$SAMPLE_PREFIX$i.fastq.gz -S $SAMPLE_PREFIX$i.sam
done