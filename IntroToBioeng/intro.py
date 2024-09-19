#2.1
#import sequence
with open('Homework_seq.fasta', 'r') as f:
    next(f) #skip header
    seq_str = f.read() #put it in string
    seq_str = seq_str.replace("\n", "") #remove newlines

#number of nt
print("2.1 answers:")
print("The number of nts in the sequence is: ", len(seq_str))

#number of codons
#if we define that ORF is stationary with ATG and ends with TAA then
print("The number of codons in the sequence is: ", int(len(seq_str)/3))

#2.2
print("\n2.2 answers")
print("The number of A nt is: ", seq_str.count("A"))
print("The number of C nt is: ", seq_str.count("C"))
print("The number of G nt is: ", seq_str.count("G"))
print("The number of T nt is: ", seq_str.count("T"))

#2.3
gc_content = (seq_str.count("G") + seq_str.count("C"))/len(seq_str)
print("\n2.3 answers")
print("The GC content is: ", round(gc_content, 2))
print("Because the GC content is only 0.22 and the optimal growth temperature is 35C then most likely it is Nonhalophilic archaea")

#2.4
#generate primary 5`-3` seq
print("\n2.4 answers")
print("5`-3` sequence is: ", seq_str)

#2.5
#generate complementary 3`- 5` seq
comp_str = ""
for i in range(len(seq_str)):
  if seq_str[i] == "A":
    comp_str += "T"
