__author__ = 'Julian Hernandez'
__version__ = '0.0.1'

from .reader import *
from .writer import Writer

# passthrough to make column_text_format.reader() return a Reader object
def reader(*args, **kwargs):
    return Reader(*args, **kwargs)

def writer(*args, **kwargs):
    return Writer(*args, **kwargs)

print("running package init")
__all__ = ["Reader"]
