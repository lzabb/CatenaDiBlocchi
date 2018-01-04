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
    
transactions_list =[
              [{'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))},
              {'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))}, {'from' : 'zabba', 'to': 'toni', 'amount' : int(np.random.randint(0,10, 1))}],
              [{'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))},
              {'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))}, {'from' : 'zabba', 'to': 'toni', 'amount' : int(np.random.randint(0,10, 1))}], 
               [{'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))},
              {'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))}, {'from' : 'zabba', 'to': 'toni', 'amount' : int(np.random.randint(0,10, 1))}],
              [{'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))},
              {'from' : 'toni', 'to': 'zabba', 'amount' : int(np.random.randint(0,10, 1))}, {'from' : 'zabba', 'to': 'toni', 'amount' : int(np.random.randint(0,10, 1))}]
              ] #FOUR rounds of transactions. toni starts with 10 (from Jesus), zappa with 0  
 

# The following, for each round checks first if the transactions for each 'from' have the required balance to choose which transactions to accept, then the accepted transaction go in the next block.          
for transactions in transactions_list:
    print ''' 
            Round for new block begins
            '''
    accepted_transactions = [] 
    # need to isolate all the from accounts to see if they have the balance to do THE POSSIBLY MANY transactions they asked
    from_list_loose = []
    for t in transactions:
        from_list_loose.append(t['from'])
    from_list = [from_list_loose[0]]
    for f in from_list_loose:
        if from_list.count(f) >= 1:
            pass
        else:
            from_list.append(f)
    print from_list
    for from_i in from_list:
        amount_i = []
        for t in transactions:     #some repeated operations
            if from_i == t['from']:
                amount_i.append(t['amount'])
            else:
                pass
        print 'All amounts requested to transfer by', from_i,':', amount_i,'.'
        print sum(amount_i)
        status = e.payment(blockchain, from_i, 'N/A', sum(amount_i)) 
        if status == 'insufficient funds':
            print status
        else:
            for t in transactions:
                if from_i == t['from']:
                    accepted_transactions.append({'from' : t['from'], 'to' : t['to'], 'amount' : t['amount']})
                else:
                    pass
        
    if accepted_transactions != []:
        block2add = e.next_block(previous_block, accepted_transactions)
        blockchain.append(block2add)
        previous_block = block2add
        print block2add.index, block2add.hash
    else:
        pass
        
      
