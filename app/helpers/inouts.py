import time
from termcolor import cprint
import pprint
import datetime




class Inout():

    def __init__(self) -> None:
        pass
    
    
    
    #Wrappers

    def test_wrap(self, func):
        """Prints the name of the tested function, 
            Prints the exec time of the test"""
        def wrap(*args, **kwargs):
            st = time.time()
            print("\n")
            cprint(f"Testing {' '.join(func.__name__.split('_')[1:])}", "green", attrs=['underline'])
            func(*args, **kwargs)
            nd = round(time.time()-st,4)
            cprint(f"\nTest executed in {nd} seconds","green",  attrs=['underline'])
        return wrap

    #pretty printers
    def print_statement(self, message):
        cprint(message, "yellow")