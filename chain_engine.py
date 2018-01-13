#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 22:06:43 2018

@author: lzabb autentication withprivate key, transaction logic, rand wallet trans, nodes competiontion con proof of work
"""

import time
from Blocks import Block
from portafoglio import Wallet
from CheckBalance import BalanceCheck
from Agents import Agent

class Engine(object):
    
    
    def __init__(self):
  
        self.genesis_block =  Block(0, time.time(), 
                                    [{'from' : 'GOD',
                                     'to' : 'Jesus',
                                     'amount' : 1000000}], '0')
        self.chain = [self.genesis_block]
        self.wallets = self.gen_wallets()
        self.agents = self.wallet_to_agents(self.wallets)
        self.wallets_keys = [wallet.public_key for wallet in self.wallets]

    
    def gen_wallets(self):
         
        return [Wallet() for _ in range(10)]
               
  
    def wallet_to_agents(self, wallets):
        
        return [Agent(wallet) for wallet in wallets]
   
  
    def next_block(self, last_block, list_transaction):
      
        this_index = last_block.index + 1
        this_timestamp = time.time()
        this_data = list_transaction 
        this_hash = last_block.hash
        return Block(this_index, this_timestamp, this_data, this_hash)
    
    
    def payment(self, last_chain, sender, receiver, amount):
    
        transaction = [{'from' : sender, 
                        'to' : receiver, 
                        'amount' : amount, 
                        'stamp' : time.time()}]
        status = BalanceCheck().check(last_chain, sender, amount)
        if status == 'transaction accepted':
            print 'Transaction accepted'
            return transaction
        else:
            return status
        
