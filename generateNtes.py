import os
import openai

openai.api_key = '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'

question = input("What notes do want to be generated: ")

boolCheck = False

while boolCheck is False:
    maxWords = int(input("Enter the number of words you want to be generated: "))
    if maxWords <= 4000:
        boolCheck = True
    else:
        print("The maximum number of words is 4000")

response = openai.Completion.create(
    model="text-davinci-002",
    prompt=question,
    temperature=0.3,
    max_tokens=maxWords,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
printText = response["choices"][0]["text"]
print(printText)
