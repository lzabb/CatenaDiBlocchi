#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 12:11:00 2018

@author: lzabb
"""

import numpy as np


class Agent(object):
    
    def __init__(self, portafoglio):
        self.portafoglio = portafoglio
        self.time_of_transaction = [0]
        self.rate_of_exchange = np.random.randint(1,100,1) # Can be made dependent on parameters of the model


    def stamp(self):
        new_time_of_transaction = self.time_of_transaction[-1] + np.random.exponential(self.rate_of_exchange)
        self.time_of_transaction.append(new_time_of_transaction)      
        return new_time_of_transaction