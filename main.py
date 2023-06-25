#! /usr/bin/env python3

import sys
sys.path.append("../..")

from myParser import *
from myLexer import *


# Leitura do arquivo de dados
def read_data():
    nome_arquivo = input(str('Digite o nome do arquivo de entrada junto com a extensão: '))
    with open(nome_arquivo, mode="r", encoding="utf-8") as file:
        dados = file.read()
        return dados


data = read_data()

analyse_lex(data)

parse(data)
