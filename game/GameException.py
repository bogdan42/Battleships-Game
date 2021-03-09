'''
Created on Dec 21, 2018

@author: Bogdan
'''
class GameException(Exception):
    def __init__(self,msg):
        self._msg = msg
        
    @property
    def message(self):
        return self._msg