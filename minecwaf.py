#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 11:52:02 2022

@author: sarah
"""
import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
    mc.setBlock(-181, 85, 277, 46)
    time.sleep(0.1) 