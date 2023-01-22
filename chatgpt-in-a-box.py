import openai
import getpass
import os
prompt_file = open('prompt.txt', 'r').read()
openai.api_key = getpass.getpass("Enter your OpenAI API key: ")
def respond_to(myprompt):
  output=[]
  result=openai.Completion.create(model="text-davinci-003",prompt=myprompt,max_tokens=1024,temperature=0.3)
  for i in result.choices[0].text:
    output.append(i)
  for i in range(1,len(output)):
    if i!=len(output):
      print(output[i],end="")
    else:
      print(output[i])
username = input("What is your username? ")
os.system("clear")
while True:
  prompt = input(username+": ")
  print("\nChatGPT: ",end="")
  respond_to(prompt_file+prompt+"\n")
  print("\n")