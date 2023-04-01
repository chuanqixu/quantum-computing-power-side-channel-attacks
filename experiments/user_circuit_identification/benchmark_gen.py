from qcutils.credential import load_provider
from qcutils.benchmarks import QASMBenchmark
from qcutils.benchmarks.utils import expand_by_layout
from qcutils.pulse import BasisPulse, CircAmpTimeSeries

import pickle, multiprocessing, itertools, functools, os



if __name__ == "__main__":
    num_layout_list = [2**i for i in range(10)]
    seed_layout = 0

    bm = QASMBenchmark(r"E:\Research\QASMBench", "small", num_qubits_list=list(range(7)), remove_final_measurements=True)

    provider = load_provider()
    backend = provider.get_backend("ibm_lagos")
    bp = BasisPulse(backend)
    bp.save_basis_amp_time_series_list(os.path.join(os.path.dirname(__file__), "benchmark_amp_timeseries", "basis_pulse_data.pickle"))

    num_process = 12

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
            p_input_idx.append(list(range(p_idx * process_len, (p_idx+1) * process_len)))


    for num_layout in num_layout_list:
        pool = multiprocessing.Pool(p_idx)
        results = pool.starmap(expand_by_layout, zip(itertools.repeat(bm), itertools.repeat(backend), p_input_idx, itertools.repeat(num_layout), itertools.repeat(seed_layout)))
        pool.close()
        pool.join()
        
        schedule_list = functools.reduce(lambda a, b: a + b, results)

        print(f"Total number of circuits: {len(schedule_list)}")

        scale = 10
        power_list = []
        for sched in schedule_list:
            power_list = CircAmpTimeSeries.from_sched(sched, backend).total()
        
        with open(os.path.join(os.path.dirname(__file__), "benchmark_amp_timeseries", f"benchmark_amp_timeseries_layout_{str(num_layout)}.pickle"), "wb") as f:
            pickle.dump(power_list, f)
