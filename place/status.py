from enum import IntEnum

class Status(IntEnum):
    PEINGIN = 1
    ACTIVTE = 2 
    DEACTIVTE = 3 
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class StatusITem(IntEnum):
    NEW = 1
    USED = 2
    OLD = 3
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

'''
class Status_Requsts(IntEnum):
    PEINGIN = 1  #Failure
    DEPOSIT = 2
    RECEIPT = 3
    DONE = 5
    FAILURE = 6

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
'''