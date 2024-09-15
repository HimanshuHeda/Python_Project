#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    def __init__(self):
        self.items = {
            'A1': {'name': 'Soda','price': 1.50,'stock': 10},
            'B1': {'name': 'Chips','price': 1.00,'stock': 5},
            'C1': {'name': 'Candy','price': 0.75,'stock': 20}
        }
        self.balance = 0
        
    def insert_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Balance updated: ${self.balance:.2f}")
        else:
            print("Invalid amount.")
    
    def select_item(self, code):
        if code in self.items:
            item = self.items[code]
            if item['stock'] > 0:
                if self.balance >= item['price']:
                    self.balance -= item['price']
                    item['stock'] -= 1
                    print(f"Dispensing {item['name']}.")
                    self.return_change()
                else:
                    print(f"Insufficient balance for {item['name']}.")
            else:
                print(f"{item['name']} is out of stock.")
        else:
            print("Invalid selection.")
                
    def return_change(self):
        if self.balance > 0:
            print(f"Returning ${self.balance:.2f} in change.")
            self.balance = 0
        else:
            print("No change to return.")


# Instantiate and use the VendingMachine
vm = VendingMachine()
vm.insert_money(2.00)
vm.select_item('A1')
vm.select_item('B1')
