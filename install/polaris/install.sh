#!/bin/bash

# From Romain Egele (this script is called install.sh)

# Generic installation script for DeepHyper on ALCF's Polaris.
# This script is meant to be run on the login node of the machine.
# It will install DeepHyper and its dependencies in the current directory.
# A good practice is to create a `build` folder and launch the script from there,
# e.g. from the root of the DeepHyper repository:
# $ mkdir build && cd build && ../install/alcf/polaris.sh
# The script will also create a file named `activate-dhenv.sh` that will
# setup the environment each time it is sourced `source activate-dhenv.sh`.

set -xe

module load llvm
module load conda/2023-10-04

conda create -p dh --clone base -y
conda activate dh/
pip install --upgrade pip

# Install Spack
git clone -c feature.manyFiles=true https://github.com/spack/spack.git
. ./spack/share/spack/setup-env.sh

git clone git@github.com:deephyper/deephyper-spack-packages.git

# Install RedisJson With Spack
spack env create redisjson
spack env activate redisjson
spack repo add deephyper-spack-packages
spack add redisjson
spack install

# Clone DeepHyper (master)
git clone -b master git@github.com:deephyper/deephyper.git

# Install DeepHyper with MPI and Redis backends
pip install -e "deephyper/[default,mpi,redis]"

# Copy activation of environment file
cp ../install/env/polaris.sh activate-dhenv.sh
echo "" >> activate-dhenv.sh
echo "conda activate $PWD/dhenv/" >> activate-dhenv.sh

# Activate Spack env
echo "" >> activate-dhenv.sh
echo ". $PWD/spack/share/spack/setup-env.sh" >> activate-dhenv.sh
echo "spack env activate redisjson" >> activate-dhenv.sh

# Redis Configuration
cp ../install/env/redis.conf redis.confg
cat $(spack find --path redisjson | grep -o "/.*/redisjson.*")/redis.conf >> redis.conf
