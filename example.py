#Rode somente o container da ollama
#Use esse comando para rodar o seu modelo de preferencia 'docker exec -it ollama ollama run model_namev1'
#Faça o comando pip install ollama e rode o codigo abaixo


import ollama

result = ollama.generate(model='model_namev1', prompt='Por que o ceu é azul?')
print(result['response'])