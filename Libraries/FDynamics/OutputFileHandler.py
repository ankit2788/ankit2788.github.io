#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 7 09:00:42 2018

@author: anks
"""

from FDynamics.Exceptions import FileMissingException
from FDynamics.Utils import CheckFileExists
import pandas as pd

class DumpOutput:
    """
    Base Class to Write different outputs to file
    """

    def __init__(self, OutputFile):
        
        if CheckFileExists(OutputFile):
            #Open file to write
            self.File = open(OutputFile, "w")
        else:

            #Creating file and raising exception for not available file
            self.File = open(OutputFile, "w")
            #raise FileMissingException(OutputFile)


        
    def WriteToFile(self, Information):
        self.File.write(','.join(str(info) for info in Information))
        self.File.write("\n")
        self.File.flush()


    def CloseFile(self):
        self.File.close()


class ReadOutput:

    def __init__(self, File):
        
        data_file_delimiter = ','
        largest_column_count = 0

        if CheckFileExists(File) is False:
            raise FileMissingException(File)
        else:
            with open(File, "r") as f:
                lines = f.readlines()

                for l in lines:
                    # Count the column count for the current line
                    column_count = len(l.split(data_file_delimiter)) + 1
                    # Set the new most column count
                    largest_column_count = column_count if largest_column_count < column_count else largest_column_count
                    
            f.close()
            
            # Generate column names (will be 0, 1, 2, ..., largest_column_count - 1)
            column_names = [i for i in range(0, largest_column_count-1)]
            
            # Read csv
            self.File = pd.read_csv(File, header=None, delimiter=data_file_delimiter, names=column_names, index_col = 0)
            


  
  


    

    


    