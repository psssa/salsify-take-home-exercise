import requests
import multiprocessing 
import time
import random
from http import HTTPStatus

class ClientSimulator():

    def simulate_multiple_client_requests():
        '''[Summary]
            Simulate two requests per client, where the requested line is randomly generated. 
            It will write on the console the response obtained whether it is a success or an error, with the associated message for each situation.
            
            args:
                None

            returns:
                None
        '''
        for i in range(1,3):
            random_line = random.randint(-10, 170)
            response = requests.get('http://127.0.0.1:5000/lines/' + str(random_line))

            if response.status_code: 
              if response.status_code == HTTPStatus.OK.value:
                print(f'[SUCCESS] Requested Line {random_line} from file : {response.text}')
            
              elif (response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE.value) or (response.status_code == HTTPStatus.BAD_REQUEST.value):
                print(f'[ERROR] Requested Line {random_line} from file  : {response.text}')
            

if __name__ == "__main__":
    '''[Summary]
        Simulate number of clients (processes) and call for each process the method simulate_multiple_client_requests that will simulate the request to get the text associated to the requested line
        
        variables:
            NUM_PROC : Number of clients that will do the request 

        returns:
            None
    '''
    NUM_PROC = 100
    processes = []
    start_time = time.time()
    for i in range(NUM_PROC):
        process = multiprocessing.Process(target=ClientSimulator.simulate_multiple_client_requests)
        processes.append(process)

    for process in processes:
      process.start()    

    for process in processes:
      process.join()
    
    end_time = time.time()
    print(f'Duration with {NUM_PROC} processes: {(end_time-start_time)} seconds')