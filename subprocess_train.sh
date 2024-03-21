#!/bin/bash


train_ml_data_dir=$1
val_ml_data_dir=$2
model_outdir=$3

# activate conda env for model
source activate /path/to/model/conda/env/

python model_train.py --train_ml_data_dir=$train_ml_data_dir --val_ml_data_dir=$val_ml_data_dir --model_outdir=$model_outdir
