""" Romain Egele
mpirun -np 5 python hpo_example_2.py
"""
import time

import numpy as np
from deephyper.evaluator import Evaluator, profile
from deephyper.evaluator.callback import TqdmCallback
from deephyper.problem import HpProblem
from deephyper.search.hps import CBO

# Definition of the parameter space to optimize
problem = HpProblem()
problem.add_hyperparameter((0.0, 10.0), "x_float")  # continuous hyperparameter
problem.add_hyperparameter((0, 10), "x_int")  # discrete hyperparameter
problem.add_hyperparameter([0, 2, 4, 6, 8, 10], "x_cat")  # categorical hyperparameter

# Path of the directory where "results" of HPO will be stored
log_dir = "logs/"


# "Back-box" function optimized (usually your machine learning workflow/code)
# The problem we want to solve is:
#   arg max f(x) where x \in X
# f(x=(0, 1, 2))
@profile
def run(job):

    # print(f"Running job: {job.id } with params = {job.parameters}", flush=True)
    training_duration = np.random.uniform(low=0, high=1)
    time.sleep(training_duration)

    # Train model and retrieve the objective
    objective = (
        job.parameters["x_float"] + job.parameters["x_int"] + job.parameters["x_cat"]
    )

    # Collect metadata
    metadata = dict(
        training_duration=training_duration,
    )

    # Checkpoint the model weights
    with open(f"{log_dir}/model_{job.id}.pkl", "w") as f:
        f.write("model weights")

    return {"objective": objective, "metadata": metadata}


if __name__ == "__main__":
    with Evaluator.create(
        run, method="mpicomm", method_kwargs={"callbacks": [TqdmCallback()]}
    ) as evaluator:

        if evaluator is not None:
            print(problem)

            search = CBO(
                problem,
                evaluator,
                log_dir=log_dir,
                verbose=1,
            )

            results = search.search(max_evals=100)
