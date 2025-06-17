import ollama

# Use the generate function for a one-off prompt
result = ollama.generate(model='deepseek-r1:1.5b', prompt='Por que o ceu é azul?')
print(result['response'])