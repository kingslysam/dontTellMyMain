import os
import openai

openai.api_key = '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'

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="What are 5 key points I should know when studying Ancient Rome?",
  temperature=0.3,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
printText = response["choices"][0]["text"]
print(printText)