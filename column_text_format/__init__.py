__author__ = 'Julian Hernandez'
__version__ = '0.0.1'

from .reader import Reader, stream_convert_csv_to_ctf
from .writer import Writer

# passthrough to make column_text_format.reader() return a Reader object
def reader(*args, **kwargs):
    return Reader(*args, **kwargs)

def writer(*args, **kwargs):
    return Writer(*args, **kwargs)

print("running package init")
__all__ = ["Reader", "stream_convert_csv_to_ctf"]
