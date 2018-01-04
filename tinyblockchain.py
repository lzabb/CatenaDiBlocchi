#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:22:05 2017

@author: lzabb
"""
import numpy as np
from chain_engine import Engine 


e = Engine()
blockchain = e.chain


# initial allocation from Jesus to generated wallets

previous_block = blockchain[0]

for i in range (0, len(e.wallets)):
    trans = e.payment(blockchain, 'Jesus', e.wallets[i], 10)
    block_to_add = e.next_block(previous_block, trans)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print block_to_add.index, block_to_add.hash


#further transactions added to the blockchain
    
transaction =[{'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(1,10, 1))},
              {'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(1,10, 1))},
              {'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(1,10, 1))},
              {'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(1,10, 1))}]   
    
for i in range(0, len(transaction)):
    block2add = e.next_block(previous_block, transaction[i])
    blockchain.append(block2add)
    previous_block = block2add
    print block2add.index, block2add.hash