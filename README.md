# Myquast

myquast is a stand-alone Python program to calculate several values from the FASTA format contigs file which are

* Number of contigs
* Total length of contigs
* Length of the largest contig.
* N50 (length of a contig, such that all the contigs of at least the same length together cover at least 50% of the assembly).

#### System requirements
Python3 (3.7 or higher)

#### Installation
Please download 'myquast.py' file to your local. After you download it, you are all set!!!

#### Usage
    python myquast.py test_data/contigs_1.fasta \
            -o quast_test_output (optinal for output directory)
            -h (showing usage)
            
#### Output
    report.txt      4-line summary
    
You report.txt should look like this
<img src="quast_libs/html_saver/static/img/quast_logo_black.png" width="300" title="QUAST">
    

    

