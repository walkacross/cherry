#!/usr/bin/env python3

import sys
import numpy as np
import torch as th

# TODO: Change to 1e-8, but make sure that it doesn't break the Cartpole stats
EPS = sys.float_info.epsilon


def totensor(array):
    if isinstance(array, (int, float)):
        array = [array, ]
    if isinstance(array, list):
        array = np.array(array, dtype=np.float32)
    if isinstance(array, (np.ndarray, np.bool_)):
        if array.dtype == np.bool_:
            array = array.astype(np.uint8)
        array = th.tensor(array)
        array = array.view(1, *array.size())
    return array


def min_size(tensor):
    """
    Returns the minimium viewable size of a tensor.
    e.g. (1, 1, 3, 4) -> (3, 4)
    """
    true_size = tensor.size()
    if len(true_size) < 1:
        return (1, )
    while true_size[0] == 1 and len(true_size) > 1:
        true_size = true_size[1:]
    return true_size


def normalize(tensor, epsilon=EPS):
    """
    Normalizes a tensor to zero mean and unit std.
    """
    if tensor.numel() <= 1:
        return tensor
    return (tensor - tensor.mean()) / (tensor.std() + epsilon)


def onehot(x, dim):
    onehot = np.zeros(1, dim)
    onehot[x] = 1.0
    return onehot
