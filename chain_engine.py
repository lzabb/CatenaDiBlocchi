#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 22:06:43 2018

@author: lzabb autentication withprivate key, transaction logic, rand wallet trans, nodes competiontion con proof of work
"""

import datetime as date
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
        


class Round_(object):
         
    def extract_name(self,list_of_dictionaries, name):
            name_list_loose = [list_of_dictionaries[d][name] for d in range(0,len(list_of_dictionaries))]
            print name_list_loose
            name_list = [name_list_loose[0]]
            for name_ in name_list_loose:
                if name_list.count(name_) >= 1:
                    pass
                else:
                    name_list.append(name_)
            return name_list
        
    def round_(self, transactions, blockchain):
        print ''' 
                Round for new block begins
                '''
        accepted_transactions = [] 
        # need to isolate all the from accounts to see if they have the balance 
        # to do THE POSSIBLY MANY transactions they asked
        from_list = self.extract_name(transactions, 'from')
        print 'Senders list:', from_list,'.'
        for from_i in from_list:
            amount_i = []
            for t in transactions:     #some repeated operations
                if from_i == t['from']:
                    amount_i.append(t['amount'])
                else:
                    pass
            print 'All amounts requested to transfer by', from_i,':', amount_i,'.', 'Total:', sum(amount_i),'.'
            status = Engine().payment(blockchain, from_i, 'N/A', sum(amount_i)) 
            if status == 'insufficient funds':
                print status
            else:
                for t in transactions:
                    if from_i == t['from']:
                        accepted_transactions.append({'from' : t['from'], 'to' : t['to'], 'amount' : t['amount']})
                    else:
                        pass
            
        if accepted_transactions != []:
            previous_block = blockchain[-1]
            block2add = Engine().next_block(previous_block, accepted_transactions)
            blockchain.append(block2add)
            previous_block = block2add
            print 'Block #', block2add.index,' Hash:', block2add.hash,'.'
        else:
            pass
  
