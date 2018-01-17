#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 22:24:29 2018

@author: lzabb
"""
import hashlib as hasher
import random


class Wallet(object):
 
    
    def __init__(self):
    
        self.private_key = ''.join(random.choice('0123456789ABCDEFghij') for i in range(8))
        self.public_key = hasher.sha256(self.private_key).hexdigest()
        self.keys = {'public' : self.public_key, 'private' : self.private_key}