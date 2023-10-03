import random
from config import token_bard
import os
import time
from bardapi import Bard

os.environ['_BARD_API_KEY'] = token_bard

def handle_response(message) -> str:
    answer = Bard().get_answer(message)['content']
    return (answer)
