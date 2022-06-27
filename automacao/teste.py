import json

with open("./automacao/links.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    
oi = dados["sensorWeb"]["xpath_como_funciona"]["xpath_midia"]

casa = oi
print(casa)