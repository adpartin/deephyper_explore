""" Romain Egele
mpirun -np 8 python parallel_example.py
"""

import time

from deephyper.evaluator import Evaluator


def run(job):
    print(f"Running job: {job.id} with x = {job.parameters['x']}", flush=True)
    time.sleep(1)
    return job.parameters["x"]


if __name__ == "__main__":
    with Evaluator.create(run, method="mpicomm") as evaluator:

        if evaluator is not None:
            tasks = [{"x": i} for i in range(20)]
            evaluator.submit(tasks)
            outputs = evaluator.gather(type="ALL")

            for out in outputs:
                print(out)

            evaluator.dump_evals() # creates a `results.csv` file with outputs
