#!/usr/bin/env python

from __future__ import print_function, division

import sys
from optparse import OptionParser
from time import sleep
import datetime
import json
import numpy as np

import pymoduleconnector
from pymoduleconnector import DataType

__version__ = 1


def reset(device_name):
    mc = pymoduleconnector.ModuleConnector(device_name)
    xep = mc.get_xep()
    xep.module_reset()
    mc.close()
    sleep(3)


def clear_buffer(mc):
    """Clears the frame buffer"""
    xep = mc.get_xep()
    while xep.peek_message_data_float():
        xep.read_message_data_float()


def simple_xep_plot(device_name, baseband=False, N=0, T=100):
    FPS = 17
    reset(device_name)
    mc = pymoduleconnector.ModuleConnector(device_name)

    xep = mc.get_xep()
    xep.x4driver_set_dac_min(900)
    xep.x4driver_set_dac_max(1150)
    xep.x4driver_set_iterations(16)
    xep.x4driver_set_pulses_per_step(26)

    xep.x4driver_set_downconversion(int(baseband))
    xep.x4driver_set_fps(FPS)

    def read_frame():
        d = xep.read_message_data_float()
        frame = np.array(d.data)
        if baseband:
            n = len(frame)
            frame = frame[:n // 2] + 1j * frame[n // 2:]
        return frame

    n = 0
    interval = T / 1000
    filename = "x1_" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + \
        "_" + str(N) + "_" + str(T) + ".txt"
    with open(filename, 'w') as f:
        while n < N:
            frame = read_frame()
            f.write(str(n) + " : [")
            frame.tofile(f, ",")
            f.write("]\n")
            print(frame.tolist() + "\n")
            sleep(interval)
            n += 1

    clear_buffer(mc)
