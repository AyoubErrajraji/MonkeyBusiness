'''
Created on Nov 25, 2017
@author: lexdewilligen
'''
class Item:
    def __init__(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind