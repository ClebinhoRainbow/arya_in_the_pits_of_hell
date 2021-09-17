class MenuRanking():
    def __init__(self):
        self.arquivo = open('arquivo_ranking.txt', 'a')
        self.lista_do_ranking = []
        self.separador = ';'
        self.quantidade_de_linhas = 0
        self.dicionario = {}
    def escreve_dado_no_arquivo(self,nome,pontuacao):
        self.arquivo = open('arquivo_ranking.txt', 'a')
        pontuacao_atual = str(pontuacao.get_pontuacao())
        self.arquivo.write(f"{pontuacao_atual};{nome};\n")
        self.quantidade_de_linhas += 1
        self.arquivo.close()
    def le_dados_do_arquivo(self):
        self.arquivo = open('arquivo_ranking.txt', 'r')
        self.lista_do_ranking.extend(self.tail(self.arquivo,5))
        self.arquivo.close()
        self.separa_lista_em_dicionario()
        #tem que transformar or arquivos de string para int
    def separa_lista_em_dicionario(self):
        lista_nomes = []
        lista_ranking = []
        print(self.lista_do_ranking)
        l_aux = []
        for linha in self.lista_do_ranking:

            l_aux = linha.split(';')

            lista_nomes.append(l_aux[0])
            lista_ranking.append(l_aux[1])
        self.dicionario= dict(zip(lista_nomes, lista_ranking))

    def tail(self,f, n):
        assert n >= 0
        pos, lines = n + 1, []
        while len(lines) <= n:
            try:
                f.seek(-pos, 2)
            except IOError:
                f.seek(0)
                break
            finally:
                lines = list(f)
            pos *= 2
        return lines[-n:]

    def display_ranking(self,janela):
        self.le_dados_do_arquivo()
        janela.draw_text("RANKING", 400, 100, size=32, color=(255, 255, 255),
                         font_name="Arial",
                         bold=False, italic=False)
        delta_y = 200
        aux_count = 0
        for key in self.dicionario:
            if(aux_count>5):
                break
            janela.draw_text(str(key)+" "+str(self.dicionario[key]), 300, delta_y, size=28, color=(255, 255, 255),
                              font_name="Arial",
                              bold=False, italic=False)
            delta_y += 40

