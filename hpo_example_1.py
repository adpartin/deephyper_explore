""" Romain Egele
mpirun -np 8 python hpo_example_1.py
"""

import time

from deephyper.evaluator import Evaluator
from deephyper.search.hps import CBO
from deephyper.problem import HpProblem

problem = HpProblem()
problem.add_hyperparameter((0.0, 10.0), "x_float")  # continuous hyperparameter
problem.add_hyperparameter((0, 10), "x_int")  # discrete hyperparameter
problem.add_hyperparameter([0, 2, 4, 6, 8, 10], "x_cat")  # categorical hyperparameter


def run(job):
    print(f"Running job: {job.id} with params = {job.parameters}", flush=True)
    time.sleep(1)
    return job.parameters["x_float"] + job.parameters["x_int"] + job.parameters["x_cat"]


if __name__ == "__main__":
    with Evaluator.create(run, method="mpicomm") as evaluator:

        if evaluator is not None:  # When evaluator is None??
            print(problem)

            search = CBO(problem, evaluator)

            results = search.search(max_evals=100)
