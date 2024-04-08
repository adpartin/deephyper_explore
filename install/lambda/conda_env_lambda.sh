#!/bin/bash --login

set -e

# https://deephyper.readthedocs.io/en/latest/install/conda.html

# From Romain Egele
conda create -n dh python=3.9 pip --yes
conda activate dh
conda install mpi4py -y
git clone -b develop git@github.com:deephyper/deephyper.git  # This may require to type github password
pip install -e "deephyper/[hps]"

# This helped remove warning (but maybe not required)
# export OMPI_MCA_btl=^openib
