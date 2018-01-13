#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:22:05 2017

@author: lzabb
"""

import numpy as np
import random
from chain_engine import Engine
from node_engine import Round_ 


e = Engine()
blockchain = e.chain


# initial allocation from Jesus to generated wallets

previous_block = blockchain[0]

for wallet in e.wallets_keys:
    trans = e.payment(blockchain, 'Jesus', wallet, 15)
    block_to_add = e.next_block(previous_block, trans)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print block_to_add.index, block_to_add.hash


#further transactions added to the blockchain
# Mechanism s.t. once 10 more transactions are requested they form  an element of transactions_list, and they are broadcasted
    

transactions_list = [e.payment(blockchain, random.choice(e.wallets_keys),
                               random.choice(e.wallets_keys),
                               int(np.random.randint(1,10, 1)))
                     for i in range(4)
                     ]
    
# The following, for each round checks first if the transactions for each 'from' have the required balance to choose which transactions to accept, then the accepted transactions go in the next block.          
[Round_().round_(transactions, blockchain) for transactions in transactions_list]