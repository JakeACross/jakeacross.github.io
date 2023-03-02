import argparse

parser = argparse.ArgumentParser(description="This is a stand-alone Python program to calculate N50 from the FASTA format contigs file")

parser.add_argument('input_file', help="Input file (fasta format)") 
parser.add_argument('-o', '--output_dir', help="Output file directory")

args = parser.parse_args()

# print(args.input_file)
# print(args.out)

f = open(args.input_file, "r")
lines = f.read().splitlines()
f.close()

if args.output_dir:
    path = args.output_dir + '/'
else:
    path = ''

lst = []
length = 0
total = 0
n50 = 0
comp = 0


for s in lines:
    if s[0] == ">":
        if length != 0:
            lst.append(length)
            length = 0
    else:
        length += len(s)
lst.append(length)

total = sum(lst)
lst.sort(reverse=True)

for e in lst:
    comp += e
    if comp >= (total / 2):
        n50 = e
        break


report = open(path + "report.txt", "w")
l1 = f"Number of contigs: {len(lst)}\n"
l2 = f"Total lenght of contigs: {total}\n"
l3 = f"Length of the largest contig: {lst[0]}bp\n"
l4 = f"N50: {n50}"
report.writelines([l1, l2, l3, l4])
report.close()
