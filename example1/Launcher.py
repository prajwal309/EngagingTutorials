#import numpy as np
import glob
import os

BaseText="#!/bin/bash\n#SBATCH --time=20:00:00 \n#SBATCH --ntasks=1\n#SBATCH -p pi_seager\n#SBATCH --cpus-per-task=4\n#SBATCH --mem=16G\n#SBATCH -o Run_%j.log\nsource /etc/profile\nmodule load anaconda3/2023.07\nexport MKL_NUM_THREADS=4\npython myCode.py MATRIXSIZE"

#Specifying the number of jobs to be submitted
TotalNumJobs = 10
JobNum = 0

assert TotalNumJobs<11, "TotalNumJobs should be less than 11"


matrixSize = 128 #Starting size of the matrix for matrix inversion

os.system("rm *.log") # remove the log files
os.system("rm *.sh") # remove the scripts 

while True:
    
    ReplacedText = BaseText.replace("MATRIXSIZE", str(matrixSize))

    #Create a launch script
    LauncherName = "SubmitJob_"+str(JobNum).zfill(5)+".sh"
    with open(LauncherName, 'w') as f:
        f.write(ReplacedText)
    os.system("chmod u+x %s" %LauncherName)

    JobNum+=1
    matrixSize*=2
    
    os.system("sbatch %s" %LauncherName) # Submit the job script 
   
    if JobNum>TotalNumJobs:
        break        

