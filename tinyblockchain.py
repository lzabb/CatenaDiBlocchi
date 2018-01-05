#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:22:05 2017

@author: lzabb
"""

import numpy as np
from chain_engine import Engine, Round_ 


e = Engine()
blockchain = e.chain


# initial allocation from Jesus to generated wallets

previous_block = blockchain[0]

for i in range (0, len(e.wallets)):
    trans = e.payment(blockchain, 'Jesus', e.wallets[i], 20)
    block_to_add = e.next_block(previous_block, trans)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print block_to_add.index, block_to_add.hash


#further transactions added to the blockchain
    
transactions_list =[
              [{'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(9,10, 1))},
              {'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))}, {'from' : 'zabba', 'to': 'toni', 'amount' : int(np.random.randint(0,10, 1))}],
              [{'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))},
              {'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))}, {'from' : 'zabba', 'to': 'toni', 'amount' : int(np.random.randint(0,10, 1))}], 
               [{'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))},
              {'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))}, {'from' : 'zabba', 'to': 'toni', 'amount' : int(np.random.randint(0,10, 1))}],
              [{'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))},
              {'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))}, {'from' : 'zabba', 'to': 'toni', 'amount' : int(np.random.randint(0,10, 1))}]
              ] #FOUR rounds of transactions. toni starts with 10 (from Jesus), zabba with 0  
    
# The following, for each round checks first if the transactions for each 'from' have the required balance to choose which transactions to accept, then the accepted transactions go in the next block.          
[Round_().round_(transactions, blockchain) for transactions in transactions_list]


