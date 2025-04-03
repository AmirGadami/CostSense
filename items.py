from typing import Optional 
from transformers import AutoTokenizer
import re



BASE_MODEL = "meta-llama/Meta-Llama-3.1-8B"

MIN_TOKENS = 150
MAX_TOKENS = 160

MIN_CHARS = 300
CEI