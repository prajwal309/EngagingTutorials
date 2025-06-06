## Created by
**Prajwal Niraula**

Email: pniraula@mit.edu

---

## Overfiew
The Engaging cluster now includes 16 nodes under the pi_seager partition. Access requires an MIT Kerberos account, making it more accessible than systems requiring MIT Lincoln Lab credentials.

To get started, refer to the official documentation on the Engaging cluster [here](https://engaging-web.mit.edu/eofe-wiki/).

---

## Login Instructions
Multiple login nodes are available. The login node often determines what modules are available. 

- **CentOS 7 Nodes**
    - eofe7.mit.edu 
    - eofe8.mit.edu 
    - eofe9.mit.edu 

- **Rocky 8 Node**
    - eofe10.mit.edu 

Some such as eofe7.mit.edu does not require authentication, hence are easier to copy the files locally to HPC. Your home directory is although available in all of them


**To Login**

>>> ssh yourKerberos@eofe7.mit.edu



## Submitting a job
Following is an example of script for submitting a job to 

```
#!/bin/bash
#SBATCH --time=20:00:00 
#SBATCH --ntasks=1
#SBATCH -p mit_normal
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH -o Run_%j.log
source /etc/profile
module load anaconda3/2023.07
export MKL_NUM_THREADS=4
python your_program.py
```

To use our dedicated nodes use: #SBATCH -p pi_seager

example1 contains a simple case of matrix inversion, which submits multiple nodes. This code is not optimized for using multiple cores. TO run the code go to clone this repository, go to the folder example1, and launch the Launcher.py which should submit 10 jobs:

```
git clone https://github.com/prajwal309/EngagingTutorials
cd EngagingTutorials/example1
python Launcher.py
```

Now to see if your jobs have been properly submitted:

>>> squeue -u username

To kill the jobs:

>>> scancel -u username

To find the time limit and the nodes available: 

>>> sinfo


## System Specs

The storage available is 1 TB, which is larger than MIT supercloud (500 GB), hence for impression wise, Engaging seems to be more suitable for jobs requiring storage required calculations.

As for the nodes itself, here are the specs (use lscpu to find after sshing into the node where you have the job):

**Engaging (pi_seager Nodes)**
```
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              192
On-line CPU(s) list: 0-191
Thread(s) per core:  2
Core(s) per socket:  48
Socket(s):           2
NUMA node(s):        2
Vendor ID:           AuthenticAMD
CPU family:          25
Model:               17
Model name:          AMD EPYC 9474F 48-Core Processor
Stepping:            1
CPU MHz:             3600.000
CPU max MHz:         4113.2808
CPU min MHz:         1500.0000
BogoMIPS:            7200.25
Virtualization:      AMD-V
L1d cache:           32K
L1i cache:           32K
L2 cache:            1024K
L3 cache:            32768K
```

**MIT Supercloud Nodes (8260 nodes)**
```
Architecture:            x86_64
  CPU op-mode(s):        32-bit, 64-bit
  Address sizes:         46 bits physical, 48 bits virtual
  Byte Order:            Little Endian
CPU(s):                  96
  On-line CPU(s) list:   0-95
Vendor ID:               GenuineIntel
  Model name:            Intel(R) Xeon(R) Platinum 8260 CPU @ 2.40GHz
    CPU family:          6
    Model:               85
    Thread(s) per core:  2
    Core(s) per socket:  24
    Socket(s):           2
    Stepping:            7
    CPU max MHz:         3900.0000
    CPU min MHz:         1000.0000
    BogoMIPS:            4800.00
Virtualization features: 
  Virtualization:        VT-x
Caches (sum of all):     
  L1d:                   1.5 MiB (48 instances)
  L1i:                   1.5 MiB (48 instances)
  L2:                    48 MiB (48 instances)
  L3:                    71.5 MiB (2 instances)
```

---


## Storage
The home directory typically allows for storage of 100 GB (old accounts) or 200 GB (new accounts). You should have access to either for 1 TB 
- /home/<username>/orcd/pool
 or 
- /pool001/<username>

## Differences between MIT Supercloud and Engaging

### 1. Scheduling System:
- Only SLURM commands are available.
- Modes such as TripleMode are not available. TripleMode is great way for submitting 1000s of jobs, which handles queuing well. Similarly, command such as LLstat are not available.

### 2. Queue Behavior
- If you don't specify the node, your job is submitted to mit_quicktest node, which has limitation of 15 minutes. On Pi_seager it is currently set at 5 days. 

---
## Best Practice:
- Find the optimum number of cores to run your job. This allows the most efficient use of the nodes. We have 16 total nodes. 
---
Happy computing.
