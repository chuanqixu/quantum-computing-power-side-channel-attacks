# Import necessary libraries and modules
from qcutils.credential import load_provider
from qcutils.benchmarks import QASMBenchmark
from qcutils.benchmarks.utils import expand_by_layout
from qcutils.pulse import BasisPulse, CircAmpTimeSeries
import pickle, multiprocessing, itertools, functools, os

# Main entry point for the script
if __name__ == "__main__":
    # List of number of circuits to be generated (powers of 2)
    num_layout_list = [2**i for i in range(8)]
    # Seed for random layout generation
    seed_layout = 0

    # Initialize a QASMBenchmark object with specific configuration options
    bm = QASMBenchmark(r"../../QASMBench", "small", num_qubits_list=list(range(7)), remove_final_measurements=True)

    # Load the quantum provider and obtain the backend named "ibm_lagos"
    provider = load_provider()
    backend = provider.get_backend("ibm_lagos")
    # Create a BasisPulse object based on the backend
    bp = BasisPulse(backend)
    # Save basis pulse amplitude time series data for the specified backend
    bp.save_basis_amp_time_series_list(os.path.join(os.path.dirname(__file__), "data", f"basis_pulse_{backend.configuration().backend_name}.pickle"))

    # Number of parallel processes to be used for computation
    num_process = 12

    # Calculate the total number of circuits to be processed and distribute them among processes
    total_len = len(bm)
    if total_len % num_process:
        process_len = int(total_len / num_process) + 1
    else:
        process_len = int(total_len / num_process)

    p_input_idx = []
    for p_idx in range(num_process):
        if p_idx * process_len >= total_len:
            p_idx -= 1
            break
        else:
            # Distribute indices of circuits to be processed among processes
            p_input_idx.append(list(range(p_idx * process_len, (p_idx+1) * process_len)))

    # Iterate through different layouts for benchmarking
    for num_layout in num_layout_list:
        # Initialize a multiprocessing pool with the specified number of processes
        pool = multiprocessing.Pool(p_idx)
        # Perform benchmarking and layout expansion in parallel processes
        results = pool.starmap(expand_by_layout, zip(itertools.repeat(bm), itertools.repeat(backend), p_input_idx, itertools.repeat(num_layout), itertools.repeat(seed_layout)))
        pool.close()
        pool.join()

        # Concatenate results from parallel processes into a single list of schedules
        schedule_list = functools.reduce(lambda a, b: a + b, results)

        # Print the total number of circuits generated for the current layout
        print(f"Total number of circuits: {len(schedule_list)}")

        # Convert schedules to CircAmpTimeSeries objects and compute total power for each circuit
        power_list = [CircAmpTimeSeries.from_sched(sched, backend).total() for sched in schedule_list]
        
        # Save the computed power values as a pickle file for further analysis
        with open(os.path.join(os.path.dirname(__file__), "data", f"layout_{str(num_layout)}.pickle"), "wb") as f:
            pickle.dump(power_list, f)
