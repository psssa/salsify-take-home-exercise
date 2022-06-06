import pandas as pd
import os
from http import HTTPStatus
from api.utils.responseConfiguration import LineServerException
import time

class DataProcessing(object):
    
    def __init__(self):
        self.fileDf = self.__fileToDataframe(os.environ.get('FILE_PATH') + os.environ.get('FILE_NAME') + '.txt')

    def __fileToDataframe(self, filepath):
        '''[Summary]
            Convert the text file to a dataframe. 
            The nomenclature of this method shows that it is a private method.
            
            args:
                filepath (str): path to the file that is going to be converted

            returns:
                dataframe : contains all the texts from file
        '''
        return pd.read_csv(filepath, header=None)

    
    def getTextFromFile(self, requested_line):
        '''[Summary]
            Get text from the requested line by the client 
            
            args:
                requested_line (int): requested line by the client

            returns:
                text : Corresponding text to the requested line

            raise:
                LineServerException : If requested line is beyond the end of the file throw a HTTP 413 Status
        '''
        if requested_line >= 1:
            requested_line = int(requested_line) - 1

        if abs(requested_line) > self.fileDf.size -1 :
            raise LineServerException(HTTPStatus.REQUEST_ENTITY_TOO_LARGE.value, 'Requested line is beyond the end of the file')
       
        return self.fileDf.iloc[requested_line, 0]


