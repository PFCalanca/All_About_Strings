endereco = "Rua dos bobos 0, Bairro unico, Algum lugar, RJ, 28475-669"

import re

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

busca = padrao.search(endereco) #Match

if busca:
    cep = busca.group()
    print(cep)
