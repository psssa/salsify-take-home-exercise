#import necessary modules and classes
from flask import Flask
from api.utils.dataProcessing import DataProcessing   
from api.utils.responseConfiguration import LineServerException 
from http import HTTPStatus
import re
from multiprocessing.pool import ThreadPool


# creating a Flask app
app = Flask(__name__)
data_processing = DataProcessing()

@app.route('/lines/<line_index>', methods = ['GET'])
def client_request(line_index):
    '''[Summary]
        Return the text of the requested line 
        
        args:
            line_index (int): index requested by client

        returns:
            text (str) : Corresponding text to the requested line

        raise:
            LineServerException : If requested line is beyond the end of the file throw a HTTP 413 Status
    '''
    try:
        if isinstance(line_index, str) and re.match('[-+]?\d+$', line_index):
            line_index = int(line_index) 
            if line_index == 0:
                 raise LineServerException(HTTPStatus.BAD_REQUEST, 'This request doesn\'t accept line index as 0')
        else :
            raise LineServerException(HTTPStatus.BAD_REQUEST, 'This request only accept integer values')
       
        pool = ThreadPool(processes=1)
        async_result = pool.apply_async(data_processing.getTextFromFile, (line_index,))
        return async_result.get()
    
    except LineServerException as e:
        return e.message, e.code