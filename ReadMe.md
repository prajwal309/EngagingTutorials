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
cd EngagingTutorials
cd example1
python Launcher.py
```

Now to see your jobs



## Specs

The storage available is 1 TB, which is larger than MIT supercloud (500 GB), hence for impression wise, Engaging seems to be more suitable for jobs requiring storage required calculations.

As for the nodes itself, here are the specs (use lscpu to find after sshing into the node where you have the job):

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
NUMA node0 CPU(s):   0-47,96-143
NUMA node1 CPU(s):   48-95,144-191
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 invpcid_single hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 clzero irperf xsaveerptr wbnoinvd amd_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq la57 rdpid overflow_recov succor smca fsrm flush_l1d
```


Compare this to 8260 node in MIT Supercloud. Others have worse spec.

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
    Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bt
                         s rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_de
                         adline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cdp_l3 invpcid_single intel_ppin ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriori
                         ty ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid cqm mpx rdt_a avx512f avx512dq rdseed adx smap clflushopt clwb intel_pt avx512cd avx512bw avx512vl xsaveopt xsavec
                          xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local dtherm ida arat pln pts pku ospke avx512_vnni md_clear flush_l1d arch_capabilities
Virtualization features: 
  Virtualization:        VT-x
Caches (sum of all):     
  L1d:                   1.5 MiB (48 instances)
  L1i:                   1.5 MiB (48 instances)
  L2:                    48 MiB (48 instances)
  L3:                    71.5 MiB (2 instances)
NUMA:                    
  NUMA node(s):          2
  NUMA node0 CPU(s):     0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94
  NUMA node1 CPU(s):     1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95
```




## Differences between MIT Supercloud and Engaging

- Only SLURM commands are available.
- Modes such as TripleMode are not available. TripleMode is great way for submitting 1000s of jobs, which handles queuing well. Similarly, command such as LLstat are not available.
- To see 
- If you don't specify the node, your job is submitted to mit_quicktest node, which has limitation of 15 minutes. On Pi_seager it is currently set at 5 days. 


## Best Practice:
- Find the optimum number of cores to run your job. This allows the most efficient use of the nodes.
