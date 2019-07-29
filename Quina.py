
jogo = open('jogos.txt', 'r')
resultado = open('resultado.txt', 'r')
retorno = open('retorno.txt', 'w')

dados_jogo = []
dados_resultado = []
numeros_acertados = []


for linha_resultado in resultado:
    linha_resultado = linha_resultado.replace('\n','')
    dados_resultado = linha_resultado.split(';')

    print(dados_resultado)

    for linha_jogo in jogo:
        linha_jogo = linha_jogo.replace('\n','')
        dados_jogo = linha_jogo.split(';')

        print(dados_jogo)

        for i in range(len(dados_jogo)):

            for j in range(len(dados_resultado)):

                if dados_jogo[i] == dados_resultado[j]:
                    numeros_acertados.append(dados_jogo[i])
            
        if numeros_acertados != '':
            print('Acertou o total de : ' + str(len(numeros_acertados)) + ' numeros, para o jogo: ' + str(linha_jogo))
            nova_linha = 'Jogo: ' + str(linha_jogo) + ' Resultado: ' + str(linha_resultado) + ' - Quantidade de numeros acertados: ' + str(len(numeros_acertados)) + ' - Numeros Acertados: '
            for numero in numeros_acertados:
                nova_linha = nova_linha + str(numero) + ';'

            numeros_acertados = []
        else:
            print('Acertou o total de : 0  numeros, para o jogo: ' + str(linha_jogo))
            nova_linha = str(linha_jogo) + ' - Quantidade de numeros acertados: 0 - Numeros Acertados: '

        print(nova_linha)
        retorno.write(nova_linha + '\n')

jogo.close()
resultado.close()
retorno.close()