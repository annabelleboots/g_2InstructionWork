import os

if "g_2" in os.environ:
    g_2 = os.environ["g_2"]+"/"
else:
    g_2 = "./"

from .core import *
from .retrieval import *
print("loading the g-2 shifter assistant")
