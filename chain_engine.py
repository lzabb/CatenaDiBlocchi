#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 22:06:43 2018

@author: lzabb autentication withprivate key, transaction logic, rand wallet trans, nodes competiontion con proof of work
"""

import datetime as date
import numpy as np
from Blocks import Block
from portafoglio import Wallet
from CheckBalance import BalanceCheck

class Engine(object):
    
    
    def __init__(self):
  
        self.genesis_block =  Block(0, date.datetime.now(), 
                                    [{'from' : 'GOD',
                                     'to' : 'Jesus',
                                     'amount' : 1000000}], '0')
        self.chain = [self.genesis_block]
        self.wallets = self.gen_wallet() #forse questo non serve neanche

      
    def gen_wallet(self):
        
        wallets_keys = [Wallet().public_key for _ in range(10)]
        wallets_keys.append('toni')
        return wallets_keys

   
    def next_block(self, last_block, list_transaction):
      
        this_index = last_block.index + 1
        this_timestamp = date.datetime.now()
        this_data = list_transaction 
        this_hash = last_block.hash
        return Block(this_index, this_timestamp, this_data, this_hash)
    
    
    def payment(self, last_chain, sender, receiver, amount):
    
        transaction = [{'from' : sender, 'to' : receiver, 'amount' : amount}]
        status = BalanceCheck().check(last_chain, sender, amount)
        if status == 'transaction accepted':
            print 'Transaction accepted'
            return transaction
        else:
            return status
        
