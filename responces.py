import random
from config import token_bard
import os
import time
from bardapi import Bard

os.environ['_BARD_API_KEY'] = token_bard

def handle_response(message) -> str:
    answer = Bard().get_answer(message)['content']
    return (answer)

# input_text = thing_to_say
# try:
# # answer = Bard().get_answer(input_text)['content']
# answer = "error 1`"
# except Exception as e:
# print(e)
# print (answer)
# await interaction.response.send_message(answer)
# await interaction.response.send_message("test")
#
# p_message = message.lower()
#
# if p_message == 'hello':
#     return 'Hey there!'  # Changed response for "hello" input
#
# if p_message == 'roll':
#     return str(random.randint(1, 6))
#
# if p_message == '!help':
#     return "`This is a help message that you can modify.`"
#
# if p_message == 'badge':
#     return "/activedevbadge"
#
# return ''  # Return an empty string for unrecognized input
