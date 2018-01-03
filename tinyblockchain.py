#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:22:05 2017

@author: lorenzozabban
"""

import datetime as date
import numpy as np
from CheckBalance import BalanceCheck
from Blocks import Block
 


def create_genesis_block():
    return Block(0, date.datetime.now(), 'Genesis Block', '0')


def next_block(last_block, list_transaction):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = list_transaction[this_index - 1] 
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)



blockchain = [create_genesis_block()]
previous_block = blockchain[0]

transaction =[{'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(1,10, 1))},
              {'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(1,10, 1))},
              {'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(1,10, 1))},
              {'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(1,10, 1))}]


num_of_block_to_add = len(transaction)

for i in range(0, num_of_block_to_add):
    block2add = next_block(previous_block, transaction)
    blockchain.append(block2add)
    previous_block = block2add
    print block2add.index, block2add.hash

cb = BalanceCheck()    
print cb.check(blockchain, 'zabba', 5)