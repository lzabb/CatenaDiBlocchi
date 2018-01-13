#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 17:14:10 2018

@author: lzabb
"""

class BalanceCheck(object):
    

    def get_(self, updated_blockchain, sender, dictionary_item):    
     
        get_ = []
        for block in updated_blockchain: 
            for dictionary in block.data:
                if dictionary[dictionary_item] == sender:
                    get_.append(dictionary)
                else:
                    pass
        return get_
  

    def get_2(self, dictionaries, amount):        
        
        return [dictionary[amount] for dictionary in dictionaries]
        
 
    def check(self, last_blockchain, sender, payment):
   
        amount_sent = self.get_2(self.get_(last_blockchain, sender, 'from'), 'amount')
        amount_received = self.get_2(self.get_(last_blockchain, sender, 'to'), 'amount')
        
        balance = sum(amount_received) - sum(amount_sent)
        print 'Balance of', sender,':', balance,'.' # questo non ha senso avvenga qua
        if balance >= payment:
            return 'transaction accepted'
        else:
            return 'insufficient funds'
        
    
