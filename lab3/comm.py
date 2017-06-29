#!/usr/bin/python


import random, sys
import string
import locale 
from optparse import OptionParser

#File class, which stores the lines from each input file
class file:
    def __init__(self,filename):
        f = open(filename, 'r')
        self.lines = f.readlines()
        f.close()

    def printlines(self):
        print(self.lines)
        return

    def __getitem__(self,i):
        return self.lines[i]
    def __len__(self):
        j=0
        for i in self:
            j=j+1
        return j

    
class line:

    def __init__(self,line):
        self.string=line
        self.column=0





def main():
    locale.setlocale(locale.LC_COLLATE, 'C')

    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE1 FILE2

Compare sorted files FILE1 and FILE2 line by line."""
    
#Parse the options and files, and store them in an array 
#Options go into options, files go into args

    parser = OptionParser(version=version_msg, usage=usage_msg)
    parser.add_option("-1", action='store_true', dest="arg1", default=False,
                      help="suppress column 1 (lines unique to FILE1)")    
    parser.add_option("-2", action='store_true', dest = "arg2", default=False,
                      help="suppress column 2 (lines unique to FILE2)")
    parser.add_option("-3", action='store_true', dest = "arg3", default=False,
                      help="suppress column 3 (lines that appear in both files)")
    parser.add_option("-u", action='store_true', dest = "arg4", default=False,
                      help="Output on unsorted files")
    options, args = parser.parse_args(sys.argv[1:])
#Check for parser errors


    if len(args) != 2:
        parser.error("Wrong number of operands")

    

    file_1 = args[0]
    file_2 = args[1]
    
#Read input from file_1 and put the lines into file_1_lines
    file_1_lines = file(file_1)
    file_2_lines = file(file_2)



    strings1 = []
    strings2 = []
#Remove the newlines from file_1_lines and put the entries into strings1
    for i in range(len(file_1_lines)):
        strings1.append(file_1_lines[i].rstrip('\n'))
        
    for i in range(len(file_2_lines)):
        strings2.append(file_2_lines[i].rstrip('\n'))

        #strings1 now contains all the lines from the first file
        #strings2 contains all lines from second file



        #If the -u option isn't used, check if the files are sorted. If they aren't, then parser error
    if options.arg4 == False:
            

        if strings1 != sorted(strings1):
            parser.error("First file is not sorted.")

        if strings2 != sorted(strings2):
            parser.error("Second file is not sorted.")



#Create new objects, lines1 and lines2, which contain the column informatoin for lines in each corresponding file
    lines1 = []
    lines2 = []

    for i in strings1:
        newline = line(i)
        lines1.append(newline)
    
    for i in strings2:
        newline = line(i)
        lines2.append(newline)
        
    #Check if lines are in both files
    for i in lines1:
        for j in lines2:
            if i.string == j.string:
                i.column = 3
                j.column = 3

    #Check if the line is in the first file only
    for i in lines1:
        in_both = False
        for j in lines2:
            if i.string == j.string:
                in_both = True
        if in_both == False:
            i.column = 1

    #Check if the line is in the second file only
    for i in lines2:
        in_both = False
        for j in lines1:
            if i.string == j.string:
                in_both = True
        if in_both == False:
            i.column = 2



    output = []

#If the unsorted option isn't used, the file is sorted, so put them into an output list
    if options.arg4 == False:

        for i in lines1:
            output.append(i)

        for i in lines2:
            if i.column != 3:
                output.append(i)


                #If the unsorted option is used, create a list outputting first file's order, 
                #then second file lines in the end

    if options.arg4 == True:
        for i in lines1:
            output.append(i)
            
        for i in lines2:
            if i.column != 3:
                output.append(i)




    newlist = sorted(output, key=lambda line: line.string)

    # for i in newlist:
    #     print i.string
    #     print i.column
    
    for i in newlist:
        if options.arg1 == False and i.column == 1:
            sys.stdout.write(i.string + '\n')

        if options.arg2 == False and i.column == 2:
            if options.arg1 == False:
                sys.stdout.write('\t')

            sys.stdout.write(i.string + '\n')

        if options.arg3 == False and i.column == 3:
            if options.arg1 == False:
                sys.stdout.write('\t')
            if options.arg2 == False:
                sys.stdout.write('\t')
            sys.stdout.write(i.string + '\n')





if __name__ == "__main__":
    main()






