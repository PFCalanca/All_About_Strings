

url = "http://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
#url = url.replace(" ","")
#poderia usar o .strp() também
url = url.strip()

#Validação da URL
if  url == "":
    raise ValueError("URL invalida")

indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)

#busca o valor de um parametro
parametro_busca = 'moedaDestino'
indice_paramentro = url_parametros.find(parametro_busca)
print(indice_paramentro)

indice_valor = indice_paramentro + len(parametro_busca) + 1
print(indice_valor)
indice_comercial = url_parametros.find('&', indice_valor)

if indice_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_comercial]

print(valor)
