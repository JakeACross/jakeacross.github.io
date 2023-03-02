import argparse

# Creating a parser
parser = argparse.ArgumentParser(description="This is a stand-alone Python program to calculate N50 from the FASTA format contigs file")

# Add an argument and option
parser.add_argument('input_file', help="Input file (fasta format)") 
parser.add_argument('-o', '--output_dir', help="Output file directory")

args = parser.parse_args()

# Open the input file
f = open(args.input_file, "r")
lines = f.read().splitlines()
f.close()

# Assign the output directory name to 'path'
if args.output_dir:
    path = args.output_dir + '/'
else:
    path = ''

lst = []
length = 0
total = 0
n50 = 0
comp = 0

# Create a list of the number of contigs
for s in lines:
    if s[0] == ">":
        if length != 0:
            lst.append(length)
            length = 0
    else:
        length += len(s)
lst.append(length)

total = sum(lst)  # get the total number of contigs

lst.sort(reverse=True)  # sort the list 

# Get N50 is a length of a contig that all the contigs of at least the same length together cover at least 50% of the assembly
for e in lst:
    comp += e
    if comp >= (total / 2):
        n50 = e
        break

# Open a file and write a report
report = open(path + "report.txt", "w")
l1 = f"Number of contigs: {len(lst)}\n"
l2 = f"Total lenght of contigs: {total}\n"
l3 = f"Length of the largest contig: {lst[0]}bp\n"
l4 = f"N50: {n50}"
report.writelines([l1, l2, l3, l4])
report.close()
