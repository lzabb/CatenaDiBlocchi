# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 19:26:58 2018

@author: Mas
"""

from chain_engine import Engine
from CheckBalance import BalanceCheck


class Round_(object):
         
                  
    def round_(self, transactions, blockchain):       
        print ''' 
              Round for new block begins
              '''
        accepted_transactions = [] 
        # need to isolate all the from accounts to see if they have the balance to do THE POSSIBLY MANY transactions they asked
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
            status = BalanceCheck().check(blockchain, from_i, sum(amount_i)) 
            if status == 'insufficient funds':
                print status
            else:
                for t in transactions:
                    if from_i == t['from']:
                        accepted_transactions.append(t)
                    else:
                        pass
            
        if accepted_transactions != []:
            previous_block = blockchain[-1]
            block2add = Engine().next_block(previous_block, accepted_transactions)
            blockchain.append(block2add)
            previous_block = block2add
            print 'Block #', block2add.index,'. Hash:', block2add.hash,'.'
        else:
            pass
  

    def extract_name(self, list_of_dictionaries, name):        
            name_list = []
            for dictionary in list_of_dictionaries:
                if name_list.count(dictionary[name]) == 0:
                    name_list.append(dictionary[name])
            return name_list
      
