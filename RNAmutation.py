# Ishaq Ibrahim


import random  # imports random


def header(fastaHeader):  # function for header
    gene_name = fastaHeader[41:46]  # splices gene name in string
    print("Gene name is: ", gene_name)  # prints gene name

    gene_id = fastaHeader[81:84]  # splices gene id in string
    print("Gene id is:", gene_id)  # prints gene id

    protein_id = fastaHeader[223:234]  # splices protein id
    print("Protein id: ", protein_id)  # print protein id

    return gene_name, gene_id, protein_id  # returns gene name, gene id, and protein id


def sequence(seqRecord):
    length_seq = len(seqRecord)  # sets variable as length of sequence string
    print("Length of sequence is:", length_seq, "Base pairs")  # prints length of sequence

    g_content = seqRecord.count('G')  # obtains count of how many G bases are in string
    c_content = seqRecord.count('C')  # obtains count of how many C bases are in string
    g_c_content = g_content + c_content  # adds both G and C content together
    print("GC content is:", g_c_content)  # prints the G_C content

    complement_seq = ""  # sets complement sequence as a blank string
    for i in range(0, len(seqRecord)):  # for loop to replace the base at each position in sequence string
        if seqRecord[i] == 'A':  # replaces A base with T base
            complement_seq += 'T'
        elif seqRecord[i] == 'T':  # replaces T base with A base
            complement_seq += 'A'
        elif seqRecord[i] == 'C':  # replaces C base with G base
            complement_seq += 'G'
        elif seqRecord[i] == 'G':  # replaces G base with C base
            complement_seq += 'C'
    print("The complement sequence is: ", complement_seq)  # prints complementary sequence

    reverse_comp_seq = complement_seq[::-1]  # reverses complementary sequence
    print("Reverse complement sequence is:", reverse_comp_seq)  # prints reverse complement sequence

    return length_seq, g_c_content, reverse_comp_seq  # returns length of sequence, GC content, reverse complementary sequence


def sequence_exit(sequence):
    bases = ['A', 'T', 'C', 'G']  # sets list of bases to use
    for i in sequence:  # for loop to check in valid bases
        if i not in bases:  # if any of the positions in the sequence are not in base list exits code
            print('invalid base')
            exit()  # exits code


def num_input():  # function for user input
    while True:  # while loop for checking user input
        try:
            num = int(input("Enter your number of mutation cycles: "))  # user inputs age
        except ValueError:  # checks if user input is correct int type and repeats if not
            print("Invalid Input")
        else:  # continues code if user correctly inputs int type input
            if num < 0:  # checks if user's age input is negative
                print("Uhhhhhhh there's no such thing as a negative numebr of mutations, try again")
            else:  # allows num parameter to be returned if user input is acceptable
                return num  # returns user age input


def lab(seq):  # function to execute mutation string
    sequence = seq  # sets sequence from fasta file
    num = num_input()  # sets number of iterations

    sequence_lower = sequence.lower()  # continues and sets sequence to lower case letters

    iterations = 0  # variable to set count number of iterations so far
    while iterations < num:  # loop to repeat mutations as long as iterations so far are lower than iteration numbers
        random_base = random.randrange(0, len(sequence_lower)) # sets position base as random sequence position
        # random_base_replace = random.choice(bases) would use this to determine random bases if not using transition or transversion
        for y in range(0, len(sequence_lower)):  # for loop for positions in sequence
            if y == random_base: # if the position is the same position with the random base continues to the mutation
                original_base = sequence_lower[y]  # original base to keep track
                change_base = mutation(sequence_lower, y)  # the new base after mutation function using transition and transversion
                sequence_lower = sequence_lower[:y] + change_base + sequence_lower[y + 1:]  # seperates the seqeuence string to insert the new character in their correct position
                print('Position of mutation is: ', y+1, "base", original_base, "and has been replaced with the base", change_base)  # prints the details
        iterations += 1  # increases iterations by 1 for the next loop
    print("Mutation sequence:", sequence_lower)  # prints sequence after mutation, with mutations in upper case
    mutation_sequence_upper = sequence_lower.upper()  # sets entire sequence in upper case
    print("Final sequence is:", mutation_sequence_upper)  # prints the final sequence
    return mutation_sequence_upper


def mutation(sequence_lower, position):  # mutation function to weight the random choice of transversion and transition mutations
    new_base = ''
    mutation_chance = random.randrange(1, 4)  # sets range of choice to 1 through 3 and picks a random number of the three
    if mutation_chance == 1 or mutation_chance == 2:  # sets 2 of the 3 choices as transition function as s 2/3rds chance
        new_base = transition(sequence_lower, position)  # sets new base to result of the transition function
    elif mutation_chance == 3:  #  sets 1 of the 3 choices as transversion as a 1/3rd chance of occuring
        new_base = transversion(sequence_lower, position)  # sets new bases as the result of transversion
    return new_base  # returns new base to be inserted in the new sequence string


def transition(sequence_lower, position):  # transition mutation function, uses .lower() to be able to return a previously mutated base
    new_base = ''  # sets new base as empty string
    if sequence_lower[position].lower() == 'a':
        new_base = 'G'  # sets new base as G
    elif sequence_lower[position].lower() == 'g':
        new_base = 'A'  # sets new base as A
    elif sequence_lower[position].lower() == 'c':
        new_base = 'T'  # sets new base as T
    elif sequence_lower[position].lower() == 't':
        new_base = 'C'  # sets new base as T
    return new_base  # returns to new base


def transversion(sequence_lower, position): # uses .lower() to be able to return a previously mutated base
    new_base = ''  # sets new base as empty string
    one_ring = ['C', 'T']  # sets list of one ring bases
    two_ring = ['A', 'G']  # sets list of two ring bases
    pyrimidine = random.choice(one_ring)  # sets new pyrimidine as random choice
    purine = random.choice(two_ring)  # sets new purine as random choice
    if sequence_lower[position].lower() == 'a':
        new_base = pyrimidine  # sets new base as a random chance of one of the two pyrimidines
    elif sequence_lower[position].lower() == 'g':
        new_base = pyrimidine  # sets new base as a random chance of one of the two pyrimidines
    elif sequence_lower[position].lower() == 'c':
        new_base = purine  # sets new base as a random chance of one of the two purines
    elif sequence_lower[position].lower() == 't':
        new_base = purine  # sets new base as a random chance of one of the two purines
    return new_base  # returns new base


def main():  # main function
    fastaHeader = ">lcl|NG_005905.2_cds_NP_009225.1_1 [gene=BRCA1] [db_xref=CCDS:CCDS11453.1,GeneID:672,LRG:p1] [protein=breast cancer type 1 susceptibility protein isoform 1] [exception=annotated by transcript or proteomic data] [protein_id=NP_009225.1] [gbkey=CDS]"
    seqRecord = "ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTG"

    sequence_exit(seqRecord)
    header(fastaHeader)  # executes header function and passes fastaHeader as argument
    sequence(seqRecord)  # executes sequence function and passes seqRecord as argument
    lab(seqRecord)

# I would like you to write two functions to be called by this main method
# 1. Parse the header string.  Function should return/report a) Gene name b) GeneID c) ProteinID
# 2. Parse the sequence record, return/report a) length of sequence b) GC content c) Reverse complement sequence


if __name__ == "__main__":
    main()
