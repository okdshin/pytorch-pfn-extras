#!/bin/bash -uex

pip3 install torchvision pytorch-ignite pytest flake8 matplotlib tensorboard onnx
# TODO(kmaehashi): fix to use stable version after v8 release
pip3 install 'cupy-cuda100>=8.0.0rc1'
pip3 install -e .

# Run unit tests
python3 -m pytest tests/

# Run examples
python3 example/mnist.py --batch-size 2048 --test-batch-size 2048 --epochs 1 --save-model
python3 example/ignite-mnist.py --batch_size 2048 --val_batch_size 2048 --epochs 1

# Run flake8
flake8 .
