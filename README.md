# Installation

## Lambda (Argonne GPU cluter)
```bash
conda create --name dh python=3.9 pip --yes
conda activate dh
conda install mpi4py --yes
git clone -b develop git@github.com:deephyper/deephyper.git
pip install -e "deephyper/[hps]"
```

## Polaris (ACLF machine)
TODO

# Examples

## Hello world
### Example 1
```bash
mpirun -np 8 python hello_mpi4py_1.py
```

### Example 2
```bash
mpirun -np 8 python hello_mpi4py_2.py
```

## Deephyper
### Example 1 (HPO)
```bash
mpirun -np 8 python hpo_example_1.py
```

### Example 2 (HPO)
```bash
mpirun -np 8 python hpo_example_2.py
```

### Example 3 (Parallel)
```bash
mpirun -np 8 python parallel_example.py
```
