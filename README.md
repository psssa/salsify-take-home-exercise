# Salsify Take Home Exercise

## Intro

&nbsp;&nbsp;&nbsp; The purpose of this exercise was to upload a txt file, then run a server that was going to receive requests from several clients with the line they wanted to get from the file.


## Assumptions 
- Have [Git Bash](https://git-scm.com/download/win) installed 
- Have [Python 3.9](https://www.python.org/downloads/) installed

## Before running the scripts

- The .txt has to be inside the folder named 'file' in the project
- Since I couldn't incorporate the requirement to get the filename when executing the run.sh, the work around done was, to define the filename in the .env file, in the environment variable FILE_NAME, without the extension .txt


## Overview

**How will your system perform with a 1 GB file? a 10 GB file? a 100 GB file?**

&nbsp;&nbsp;&nbsp; Since I used dataframe to store the txt file information, up to 1GB the performance is good since these types of structures are suitable for larger datasets. However, for files with a larger size, only chunks implementation would improve the performance.

</br>

**How will your system perform with 100 users? 10000 users? 1000000 users?**

&nbsp;&nbsp;&nbsp; In this topic it was only made tests with 100 users and files with KB size. From those tests it was possible to analyze that the processing time for the 100 clients was 10 seconds

</br>

**What documentation, websites, papers, etc did you consult in doing this assignment?**

- [HTTP Status Library](https://docs.python.org/3/library/http.html)
- [Ignore header from files](https://stackoverflow.com/questions/28382735/python-pandas-does-not-read-the-first-row-of-csv-file)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)
- [Multiprocessing VS Threading](https://realpython.com/python-concurrency/#how-to-speed-up-an-io-bound-program)
- [Multiprocessing VS Threading](https://www.kaggle.com/code/residentmario/multithreading-and-multiprocessing-apis-in-python/notebook)

</br>

**What third-party libraries or other tools does the system use? How did you choose each library or framework you used?**

&nbsp;&nbsp;&nbsp;This exercise was done in Python so, I used Flask to build the REST Api and, with that I used:
- pip : to install all the modules needed, such as, pandas
- virtualenv : to make sure that only the needed libraries and respective versions were installed 
- requests : simulate the HTTP Requests in the clientSimulator

</br>

**How long did you spend on this exercise?**

&nbsp;&nbsp;&nbsp;Since my time was spent between work and courses twice a week until 10pm, I dedicated about 2 to 3 hours in a period of 7 days to solve this exercise 

</br>

**If you were to critique your code, what would you have to say about it?**

&nbsp;&nbsp;&nbsp;Although it's a small project there are some improvements that I would make in the future, such as:
  - Implement the single command-line parameter in the run.sh 
  - Chunks implementation to improve performance
  - Unit tests
  - Better named files, to be more clear what is being implemented in that file
  
&nbsp;&nbsp;&nbsp;Outside the context of the project, I should have investigated a little bit more before starting the exercise, to understand in which language it would be easier to implement what was requested as well as, the integration with shell script. 
