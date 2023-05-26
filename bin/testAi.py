import openai
import os
import requests

url = "https://api.openai.com/v1/chat/completions"
api_key = "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"

import os
import openai
api_key = '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'

openai.api_key = api_key

completion = openai.ChatCompletion.create(
  model="ada",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)



    
