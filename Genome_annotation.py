# Ishaq Ibrahim
# BINF 6111
# iibrahim@uncc.edu

def choice():  # function for user to choose which search option to use
    while 1:  # try except block to obtain user choice
        try:
            user_choice = int(input('Please choose for the following options\n1: Gene ID\n2:GO ID\n3:Keyword search\nOption:'))
        except ValueError:
            print('Please only choose 1, 2, or 3 for the choices')
        else:
            if user_choice not in range(1, 4): # ensures user option is between 1 and 3
                print('Please only choose between 1, 2, or 3')
            else:
                return user_choice  # returns user choice as variable for user search function


def user_search():  # function to match user choice with search
    search = 'yes'  # intial search is yes to go through while loop
    result = ""  # blank result string to add to later
    while search == 'yes':  # while loop for while user still wants to search again
        option = choice()  # obtains user choice to determine which search function
        if option == 1:
            geneID = input("Please insert gene ID ")  # user enters gene ID
            result += searchGeneID(geneID, result)  # executes search gene ID function
        elif option == 2:
            GOID = input("Please insert Gene Ontology ID: ")  # user enters GO ID
            result += searchGOID(GOID, result)  # executes search GO ID function
        elif option == 3:
            keyword = input("Please insert keyword: ")  # user enters keyword
            result += keywordsearch(keyword, result)  # executes keyword search function
        search = input("would you like to search again? yes if no enter any key: ")  # repeats loop is user enters yes
    formatResult(result)  # if user enters anything but yes, uses result as an argument for format result function


def formatResult(result):  # format result function to output result into file
    restricted_char = ['/', ':', '?', "<", ">", "|"]  # characters not allowed in a windows file name
    try:  # try and except block to ensure no restricted characters in user file name
        user_file = input('Please enter file with extension: ')
    except ValueError:  # ensures file name is not float type
        print('Please choose a file name')
    else:
        for i in user_file:  # for loop to check each string position to ensure none are invalid characters
            if i in restricted_char:
                print('Please choose an acceptable file name')
            else:
                fout = open(user_file, 'w')  # opens user file name as a writable file
                fout.write(result)  # writes user result to user named file
                fout.close()  # closes user named file


def searchGeneID(geneID, result):  # search gene ID function
    fh = open("soybase_genome_annotation_v2.0_10-17-2019v2.txt")  # opens file
    for line in fh:  # for loop for each line in the file
        if line.startswith("Glyma"):  # lines of interest start with Glyma
            linelst = line.split("\t")  # uses tab delimiter to separate lines into list
            print(linelst)
            if geneID in linelst[0]:  # search for gene ID, in column 1 and proceeds if found
                bpDesc = linelst[12]  # sets biological process string as its index
                mfDesc = linelst[14]  # sets molecular function string as its index
                ccDesc = linelst[16]  # sets cellular component string as its index
                # adds outputs below to result string
                result += "Found gene " + geneID + " in file with:\n"
                result += "\tBiological Process terms:\n\t\t" + bpDesc
                result += "\n\tMolecular Function terms:\n\t\t" + mfDesc
                result += "\n\tCellular Component terms:\n\t\t" + ccDesc
                print(result)
                return result  # returns result
    return "no result found"  # returns if no geneID found


def searchGOID(goID, result):  # function to search for GO ID
    fh = open("soybase_genome_annotation_v2.0_10-17-2019v2.txt")  # opens file
    for line in fh:  # for loop for each line in file
        if line.startswith("Glyma"):  # Lines of interest start w/ Glyma
            linelst = line.split("\t")  # tab delimiter sets line to a list
            # if GO ID in its appropriate column adds its terms to result string and prints
            # returns each result
            if goID in linelst[11]:
                bpDesc = linelst[12]
                result += "Found Gene Ontology Biological Process ID " + goID + " in file with:\n"
                result += "\tBiological Process terms:\n\t\t" + bpDesc
                print(result)
                return result
            elif goID in linelst[13]:
                mfDesc = linelst[14]
                result += "Found Gene Ontology Molecular Function ID " + goID + "in file with:\n"
                result += "\n\tMolecular Function terms:\n\t\t" + mfDesc
                print(result)
                return result
            elif goID in linelst[15]:
                ccDesc = linelst[16]
                result += "Found Gene Ontology Cellular ID " + goID + "in file with:\n"
                result += "\n\tCellular Component terms:\n\t\t" + ccDesc
                print(result)
                return result
    return "no result found"  # returns if no GO ID found


def keywordsearch(keyword, result):  # keyword search function
    fh = open("soybase_genome_annotation_v2.0_10-17-2019v2.txt")  # opens file
    for line in fh:  # for loop for each line in file
        if keyword in line:  # if keyword is in line proceeds
            # adds entire to result string and returns result
            result += "Found keyword " + keyword + " in file with:\n" + line.rstrip()
            print(result)
            return result
    return "no result found"  # returns i fno keyword found


def main():  # main function
    user_search()  # executes user search function 


if __name__ == "__main__":
    main()
