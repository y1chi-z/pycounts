# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts")

from .pycounts import count_words

__all__ = ["count_words"]
