""" From Romain Egele
mpirun -np 8 python hello_mpi4py_1.py
or
mpiexec -np 8 python hello_mpi4py_1.py
""" 
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
name = MPI.Get_processor_name()

print(f"Hello from process {rank} of {size} on {name}!", flush=True)
