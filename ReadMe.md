## Created by
Prajwal Niraula
Email: pniraula@mit.edu

## Details
Recently there were 16 nodes added to the Engaging clusters named pi_seager. Getting an account requires MIT kerberos, hence no requirements like MIT Lincoln lab. To get started look at their page:


## Login
Multiple login nodes are available. The login node often determines what modules are available. 
 - eofe7.mit.edu (CentOS 7)
 - eofe8.mit.edu (CentOS 7)
 - eofe9.mit.edu (CentOS 7)
 - eofe10.mit.edu (Rocky 8)

Some such as eofe7.mit.edu does not require authentication, hence are easier to copy the files locally to HPC. Your home directory is although available in all of them

>>> ssh yourKerberos@eofe7.mit.edu



## Submitting a job
Following is an example of script for submitting a job to 

```
#!/bin/bash
#SBATCH --time=20:00:00 
#SBATCH --ntasks=1
#SBATCH -p mit_normal
#SBATCH --cpus-per-task=4
#SBATCH --mem=4G
#SBATCH -o Run_%j.log
source /etc/profile
module load anaconda3/2023.07
export MKL_NUM_THREADS=4
python your_program.py
```

To use our dedicated nodes use: #SBATCH -p pi_seager

example1 contains a simple case of matrix inversion, which submits multiple nodes. 

## Specs

The storage available is 1 TB, which is larger than MIT supercloud (500 GB), hence is suitable for more storage required calculations.
The p 

## Differences between MIT Supercloud and Engaging

- Only SLURM commands are available.
- Modes such as TripleMode are not available. TripleMode is great way for submitting 1000s of jobs, which handles queuing well. Similarly, command such as LLstat are not available.
- If you don't specify the node, your job is submitted to mit_quicktest node, which has limitation of 15 minutes. On Pi_seager it is currently set at 5 days. 


## Best Practice:
- Find the optimum number of cores to run your job. This allows the most efficient use of the nodes.
