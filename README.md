# quantum-computing-power-side-channel-attacks

This is the repository for ACM CCS 23 Artifact Appendix: Exploration of Power Side-Channel
Vulnerabilities in Quantum Computer Controllers.

Please find full-length paper paper: [Exploration of Power Side-Channel
Vulnerabilities in Quantum Computer Controllers](https://dl.acm.org/doi/10.1145/3576915.3623118), or arXiv version [Exploration of Quantum Computer Power Side-Channels](https://arxiv.org/abs/2304.03315).

Bibtex:
```bibtex
@inproceedings{10.1145/3576915.3623118,
author = {Xu, Chuanqi and Erata, Ferhat and Szefer, Jakub},
title = {Exploration of Power Side-Channel Vulnerabilities in Quantum Computer Controllers},
year = {2023},
isbn = {9798400700507},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3576915.3623118},
doi = {10.1145/3576915.3623118},
abstract = {The rapidly growing interest in quantum computing also increases the importance of securing these computers from various physical attacks. Constantly increasing qubit counts and improvements to the fidelity of the quantum computers hold great promise for the ability of these computers to run novel algorithms with highly sensitive intellectual property. However, in today's cloud-based quantum computer setting, users lack physical control over the computers. Physical attacks, such as those perpetrated by malicious insiders in data centers, could be used to extract sensitive information about the circuits being executed on these computers. This work shows the first exploration and study of power-based side-channel attacks in quantum computers. The explored attacks could be used to recover information about the control pulses sent to these computers. By analyzing these control pulses, attackers can reverse-engineer the equivalent gate-level description of the circuits, and the algorithms being run, or data hard-coded into the circuits. This work introduces five new types of attacks, and evaluates them using control pulse information available from cloud-based quantum computers. This work demonstrates how and what circuits could be recovered, and then in turn how to defend from the newly demonstrated side-channel attacks on quantum computing systems.},
booktitle = {Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security},
pages = {579–593},
numpages = {15},
keywords = {quantum computer controllers, power side-channel vulnerabilities, quantum computers},
location = {<conf-loc>, <city>Copenhagen</city>, <country>Denmark</country>, </conf-loc>},
series = {CCS '23}
}
```

## Abstract

This paper delves into the analysis of power side-channel attacks on quantum computers, specifically focusing on the controllers of superconducting quantum computers. The study explores various attacks capable of retrieving secret information from quantum circuits, including User Circuit Identification (UC), Circuit Oracle Identification (CO), Circuit Ansatz Identification (CA), Qubit Mapping Identification (QM), Quantum Processor Identification (QP), and Circuit Reconstruction (CR). 

In the artifact evaluation, we provide source code and experiments corroborating the claims made in this paper.


## Description & Requirements

### Security, Privacy, and Ethical Concerns

This study involves non-destructive procedures, posing no security, privacy, or ethical risks for evaluators.

### How to Access

Check the GitHub repository from https://github.com/chuanqixu/quantum-computing-power-side-channel-attacks.

### Hardware Dependencies

The code is primarily Python-based and should be compatible with most CPUs. In addition, access to quantum computers is required. The experiments in this study were conducted on IBM Quantum's platforms. One can register it at https://www.ibm.com/quantum.

### Software Dependencies

Similarly, the code requires users to execute Python and Jupyter Notebook, and how to install the dependencies will be introduced in the following. Besides, there is no specific requirement for the software or operating systems. However, due to the path resolution issue with different operating systems, we may require users to manually change some path specifications in the code.

### Benchmarks

This study utilizes [QASMBench](https://github.com/pnnl/QASMBench) as its benchmarking tool. Users can download it from the repository, and the required files are included in the `QASMBench`` directory within the repository.


## Set-up

### Installation

#### Software Dependencies

Python is the main programming language for this paper. We recommend creating a new Python environment for evaluations.

First, install the dependencies with the command:

```bash
pip install qiskit qiskit[visualization] qiskit-ibmq-provider qiskit-aer matplotlib ipykernel
```
These modules are `qiskit`, `qiskit[visualization]`, `qiskit-ibmq-provider`, `qiskit-aer`, which are the quantum computing software development kit we used in this paper. For more information, please see [Qiskit Official Website](https://qiskit.org/). Other modules are `matplotlib` for figure plotting, and `ipykernel` for the Jupyter Notebook running.

Besides, the source Python code for this project is in the directory `src`. The module can be downloaded with the command (starting from the root):

```bash
cd src && pip install .
```

This study utilizes [QASMBench](https://github.com/pnnl/QASMBench) as its benchmarking tool. Users can download it from the repository, and the required files are included in the `QASMBench`` directory within the repository.


#### Access to IBM Quantum

The access to IBM Quantum is required. One can register at [IBM Quantum Platform](https://quantum-computing.ibm.com/).

To set up the Qiskit account, visit the IBM Quantum Account web page and copy the account API token at: [IBM Quantum Account](https://quantum-computing.ibm.com/account). Replace `MY_API_TOKEN` below with it and execute the following code snippet:
```python
   from qiskit import IBMQ
   IBMQ.save_account('MY_API_TOKEN')
```


We provide a quick load function to access the provider. To set up, create a JSON file `provider_credential.json` containing the credential information under the path `src/qcutils/credential`. For example, in the Linux system, this can be done with the command (starting from the root):
```bash
touch src/qcutils/credential/provider_credential.json
```

Inside the file, include the access information. One example:
```json
{
    "ibm_quantum": {
        "hub": "ibm-q", 
        "group": "open", 
        "project": "main"
    }
}
```

#### Notes on Reproducibility

Due to the fast updates of the needed Python modules, the code may not be successfully executed if different versions of dependencies are used. We provide here the version used in this paper:


| Name      | Version |
| ----------- | ----------- |
matplotlib   |             3.8.0
numpy        |             1.23.5
python        |            3.9.18
qiskit         |           0.44.2
qiskit-aer      |          0.12.2
qiskit-ibmq-provider  |    0.20.2
qiskit-terra          |    0.25.2.1

Additionally, quantum computers on IBM Quantum may retire in the future. At the time of this artifact evaluation, `ibmq_lima`, `ibmq_belem`, `ibmq_quito`, `ibmq_manila`, `ibmq_jakarta`, `ibm_oslo` are all retired. With different quantum computer architectures, users may need to manually change the code to satisfy the hardware requirements, such as changing the native gates. Also, because the calibration and pulse data are continuously changing, users will get a different result from what is presented in the paper. We provide the data that may be used in the time that we executed the experiments under each experiment directory.

### Basic Test

Once installation is successful, the code should be executable. Follow the provided evaluation workflow to validate experiment reproducibility.


## Evaluation Workflow

### Major Claims

We provide all necessary code and experiments to generate the data and figures presented in the paper. Users can reproduce the results by following the outlined steps.

### Experiments

The experiments done in this paper are presented under the directory `experiments`. The authors did the experiments with a personal computer, which is equipped with 12th Gen Intel(R) Core(TM) i7-12700H 2.69 GHz and 32 GB RAM. 

The experiments used classes and functions in the directory `src/qcutils`, which consists of 4 parts:

1. `credential`: Provides a quick load of the provider.
2. `benchmarks`: Provides the interface to get the circuit from QASMBench, as well as the class to process the pulse information from the backend.
3. `pulse`: Provides the code for processing pulse information and simulating the power traces, as well as the function to reconstruct the circuit.
4. `circuit`: Provides the code to generate the quantum circuits for Bernstein-Vazirani, Deutsch-Jozsa, and Grover's search for the evaluation in Section 5.2 Circuit Oracle Identification (CO).

Other codes needed to reproduce the experiments are in each Jupyter Notebook to perform the experiments. The estimated human-time is the time of running the Jupyter notebooks and thus is negligible. The estimated compute-time is provided in the following for each experiment:

1. `0-benchmark` [4 compute-minutes]: This directory contains the schematics to show the general features of the benchmark.
   1. `benchmark_info.ipynb`: Figure 9 of the undefended version, and Fig. 9 in the long version of the paper.
   2. `benchmark_reconstruct_info.ipynb`: Table 3, Parameters data of the benchmark quantum circuits.
   3. `mean_power.ipynb`: Additional figures to show the mean power plot of different quantum circuit, and different layouts of `toffoli_n3`. These figures are not shown in the paper due to the page limit.
   4. `plot_backend_info.ipynb`: Figure 6 (d-f), which shows the amplitude of the native gates, X, SX, and CNOT on different quantum machines. Note that by the time of the submission of this artifact, only `ibm_nairobi`, `ibm_lagos`, and `ibm_perth` are working, while other backends have retired. Correspondingly, the list of backends needs to be changed. This can be done by changing the first parameters in the 4th block. For example, change it to `backend_name_list = ["ibm_nairobi", "ibm_lagos", "ibm_perth"]` so that only these three backends will be considered.

2. `1-user_circuit_identification` [20 compute-hours]: This directory contains the code for Section 5.1 User Circuit Identification (UC).
   1. `benchmark_gen.py`: Generate the amplitude time series for quantum circuits in the benchmark, with data boosting by transpiling circuits into different layouts.
   2. `compute_accuracy.ipynb`: Generate the data for Figure 7, which shows the results of user circuit identification (UC).
   3. `plot_accuracy.ipynb`: Plot Figure 7.

3. `2-circuit_oracle_identification` [3 compute-hours]: This directory contains the code for Section 5.2 Circuit Oracle Identification (CO).
   1. `circuit_oracle_identification.ipynb`: Table 2, which shows the minimum circuit distance with the different number of qubits of the oracles.
   2. `circuit_oracle_plot.ipynb`: Fig. 8 (a) and (b) in the long version, which shows the idea that angles in RZ will be changed for Deutsch-Jozsa and Grover's search.

4. `3-circuit_ansatz_identification` [1 compute-minute]: This directory contains the code for Section 5.3 Circuit Ansatz Identification (CA).
   1. `circuit_ansatz_identification.ipynb`: The minimum circuit distance mentioned in Section 5.3.
   2. `circuit_ansatz_plot.ipynb`: Fig. 8 (c) in the long version, which shows the idea that angles in RZ will be changed for QAOA.

4. `4-qubit_mapping_identification` [1 compute-hour]: This directory contains the code for Section 5.4 Qubit Mapping Identification (QM).
   1. `qubit_mapping_identification.ipynb`: Table 3, Column Attacks - QM, which shows the minimum circuit distance of different layouts.

5. `5-quantum_processor_identification` [1 compute-minute]: This directory contains the code for Section 5.5 Quantum Processor Identification (QP).
   1. `quantum_processor_identification.ipynb`: Table 3, Column Attacks - QP, which shows the minimum circuit distance of different quantum processors.

6. `6-circuit_reconstruction`: [2 compute-hours] This directory contains the code for Section 5.6 Quantum Circuit Reconstruction (CR).
   1. `circuit_reconstruction.ipynb`: Table 3, Column Attacks - CR, which shows whether the circuit can be reconstructed with the method mentioned in the paper. If the circuit distance is close to 0, it means that the circuit can be reconstructed.

7. `7-defense` [1 compute-hour]: This directory contains the code for Section 6.1 Preventing Timing, Total Energy, and Mean Power Attacks.
   1. `ui_defense.ipynb`: Figure 9 in Section 6.1 Preventing Timing, Total Energy, and Mean
Power Attacks, which shows the results with defense for energy, mean power, and duration.
   1. `rz_defense.ipynb`: Discussion in Section 6.3 Preventing Per-Channel Trace Attacks, which defense by transforming the gates.


## Version

Based on the LaTeX template for Artifact Evaluation V20231005. Submission,
reviewing and badging methodology followed for the evaluation of this artifact
can be found at https://secartifacts.github.io/acmccs2023/.