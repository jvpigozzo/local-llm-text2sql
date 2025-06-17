#Rode somente o container da ollama
#Use esse comando para rodar o seu modelo de preferencia 'docker exec -it ollama ollama run model_namev1'
#Faça o comando pip install ollama e rode o codigo abaixo


import ollama
from langchain_community.chat_models import ChatOllama

#result = ollama.generate(model='model_namev1', prompt='Por que o ceu é azul?')
#print(result['response'])

chat = ChatOllama(model="deepseek-r1:1.5b")
response = chat.invoke("Conte uma piada")
print(response)
                  