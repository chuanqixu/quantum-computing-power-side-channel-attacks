from qcutils.benchmarks import QASMBenchmark
from qcutils.benchmarks import PulseMetircs

from qiskit import IBMQ
import matplotlib.pyplot as plt

IBMQ.load_account()
provider = IBMQ.get_provider(hub="ibm-q", group="open", project="main")
backend = provider.get_backend("ibm_lagos")

from qcutils.benchmarks import QASMBenchmark
bm = QASMBenchmark(r"E:\Research\QASMBench", "small", num_qubit=list(range(7)))
pm = PulseMetircs(bm, backend=backend, remove_final_measurements=True)



# amp_timeseries_dict = pm.to_mean_amp_timeseries_dict(scale = 1, do_transpile=True)

# circ_name_list = []
# mean_amp_list = []
# for circ_name, mean_amp in amp_timeseries_dict.items():
#     circ_name_list.append(circ_name)
#     mean_amp_list.append(mean_amp)

# plt.bar(circ_name_list, mean_amp_list)
# plt.xticks(rotation=90)

# plt.xlabel("Circuit")
# plt.ylabel("Mean Power")

# plt.savefig("./mean_power.pdf", bbox_inches = "tight")
# plt.show()


from qiskit import QuantumCircuit
import itertools
from qcutils.pulse.basispulse import circ_to_amp_timeseries
import numpy as np

circ = QuantumCircuit.from_qasm_file(r"E:\Research\QASMBench\small\toffoli_n3\toffoli_n3.qasm")
mean_amp_list = [np.mean(circ_to_amp_timeseries(circ, backend, total=True, do_transpile=True, initial_layout=layout)) for layout in list(itertools.permutations(range(7), 3))]

plt.bar(range(len(mean_amp_list)), mean_amp_list)
plt.savefig("./mean_power_layout.pdf", bbox_inches = "tight")

plt.xlabel("Layout")
plt.ylabel("Mean Power")

plt.show()
