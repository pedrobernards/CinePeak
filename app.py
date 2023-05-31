app.py
from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

lista_de_filmes = []
generos = ["Romance", "Suspense", "Ficção Científica", "Ação", "Drama", "Terror", "Comédia"]

class Filme:
    def __init__(self, nome, data, nota, genero1, genero2, pontuacao_algoritmo, recomendado):
        self.nome = nome
        self.data = data
        self.nota = nota
        self.genero1 = genero1
        self.genero2 = genero2
        self.pontuacao_algoritmo = pontuacao_algoritmo
        self.recomendado = recomendado


# função para adicionar filmes
def adicionar_filme(nome, data, nota, genero1, genero2, pontuacao_algoritmo, recomendado):
    filme = Filme(nome, data, nota, genero1, genero2, pontuacao_algoritmo, recomendado)
    lista_de_filmes.append(filme)

adicionar_filme("Tropa de Elite 3", date(2002,4,20), 9.0, "Ação", "Suspense", 0, False),
adicionar_filme("Blade Runner", date(1982,6,25), 8.1, "Ficção Científica", "Suspense", 0, False),
adicionar_filme("Jurassic Park", date(1993,6,9), 8.1, "Ficção Científica", "Ação", 0, False),
adicionar_filme("A Origem", date(2010,7,16), 8.8, "Ficção Científica", "Suspense", 0, False),
adicionar_filme("De Volta Para o Futuro", date(1985,7,3), 8.5, "Ficção Científica", "Comédia", 0, False),
adicionar_filme("Interestelar", date(2014,11,6), 8.6, "Ficção Científica", "Drama", 0, False),
adicionar_filme("O Show de Truman", date(1998,6,5), 8.1, "Drama", "Ficção Científica", 0, False),
adicionar_filme("O Sexto Sentido", date(1999,8,6), 8.1, "Suspense", "Drama", 0, False),
adicionar_filme("Os Outros", date(2001,8,10), 7.6, "Suspense", "Drama", 0, False),
adicionar_filme("Psicose", date(1960,9,8), 8.5, "Suspense", "Terror", 0, False),
adicionar_filme("O Iluminado", date(1980,5,23), 8.4, "Terror", "Suspense", 0, False),
adicionar_filme("A Hora do Pesadelo", date(1984,11,16), 7.5, "Terror", "Suspense", 0, False),
adicionar_filme("It: A Coisa", date(2017,9,7), 7.3, "Terror", "Drama", 0, False),
adicionar_filme("Corra!", date(2017,3,17), 7.7, "Suspense", "Terror", 0, False),
adicionar_filme("Jogos Mortais", date(2004,10,29), 7.6, "Terror", "Suspense", 0, False),
adicionar_filme("O Exorcista", date(1973,12,26), 8.0, "Terror", "Drama", 0, False),
adicionar_filme("A Lista de Schindler", date(1993,12,3), 8.9, "Drama", "Histórico", 0, False),
adicionar_filme("Forrest Gump", date(1994,7,6), 8.8, "Drama", "Comédia", 0, False),
adicionar_filme("O Chamado", date(2002,10,18), 7.1, "Terror", "Suspense", 0, False),
adicionar_filme("O Exorcista", date(1973,12,26), 8.0, "Terror", "Drama", 0, False)
adicionar_filme("A Noite do Pesadelo", date(1984,10,1), 8.5, "Terror", "Suspense", 0, False),
adicionar_filme("A Bruxa", date(2015,2,19), 7.2, "Terror", "Suspense", 0, False),
adicionar_filme("Halloween", date(1978,10,25), 7.8, "Terror", "Suspense", 0, False),
adicionar_filme("Pânico", date(1996, 12, 20), 7.2, "Terror", "Suspense", 0, False),
adicionar_filme("Atividade Paranormal", date(2007, 9, 14), 6.3, "Terror", "Suspense", 0, False),
adicionar_filme("A Órfã", date(2009,7,24), 7.0, "Terror", "Suspense", 0, False),
adicionar_filme("Missão Impossível: Protocolo Fantasma", date(2011,12,7), 7.4, "Ação", "Suspense", 0, False),
adicionar_filme("Duro de Matar", date(1988,7,15), 8.2, "Ação", "Suspense", 0, False),
adicionar_filme("Velozes e Furiosos", date(2001,6,22), 6.8, "Ação", "Crime", 0, False),
adicionar_filme("John Wick", date(2014,10,24), 7.4, "Ação", "Suspense", 0, False),
adicionar_filme("O Exterminador do Futuro 2: O Julgamento Final", date(1991,7,3), 8.5, "Ação", "Ficção Científica", 0, False),
adicionar_filme("O Resgate do Soldado Ryan", date(1998,7,24), 8.6, "Ação", "Drama", 0, False),
adicionar_filme("007: Operação Skyfall", date(2012,10,26), 7.7, "Ação", "Espionagem", 0, False),
adicionar_filme("O Profissional", date(1994,11,18), 8.5, "Ação", "Drama", 0, False),
adicionar_filme("Os Mercenários", date(2010,8,13), 6.5, "Ação", "Aventura", 0, False),
adicionar_filme("A Supremacia Bourne", date(2004,7,23), 7.7, "Ação", "Suspense", 0, False),
adicionar_filme("Busca Implacável", date(2008,2,29), 7.8, "Ação", "Suspense", 0, False),
adicionar_filme("O Grande Herói", date(2013,12,25), 7.5, "Ação", "Drama", 0, False),
adicionar_filme("Velocidade Máxima", date(1994,6,10), 7.2, "Ação", "Suspense", 0, False),
adicionar_filme("Kill Bill: Volume 1", date(2003,10,10), 8.1, "Ação", "Crime", 0, False),
adicionar_filme("Madrugada dos Mortos", date(2004,3,19), 7.3, "Ação", "Terror", 0, False),
adicionar_filme("Blade Runner 2049", date(2017,10,6), 8.0, "Ação", "Ficção Científica", 0, False),
adicionar_filme("Orgulho e Preconceito", date(2005,11,11), 7.8, "Romance", "Drama", 0, False),
adicionar_filme("Diário de uma Paixão", date(2004,6,25), 7.8, "Romance", "Drama", 0, False),
adicionar_filme("Titanic", date(1997,12,19), 7.8, "Romance", "Drama", 0, False),
adicionar_filme("La La Land: Cantando Estações", date(2016,12,25), 8.0, "Romance", "Musical", 0, False),
adicionar_filme("Antes do Amanhecer", date(1995,1,27), 8.1, "Romance", "Drama", 0, False),
adicionar_filme("Amor à Flor da Pele", date(2000,12,29), 8.1, "Romance", "Drama", 0, False),
adicionar_filme("Simplesmente Acontece", date(2014,10,22), 7.2, "Romance", "Drama", 0, False),
adicionar_filme("Casablanca", date(1942,11,26), 8.5, "Romance", "Drama", 0, False),
adicionar_filme("500 Dias com Ela", date(2009,7,17), 7.7, "Romance", "Comédia", 0, False),
adicionar_filme("E o Vento Levou", date(1939,12,15), 8.1, "Romance", "Drama", 0, False),
adicionar_filme("Amor", date(2012,5,20), 7.9, "Romance", "Drama", 0, False),
adicionar_filme("Um Lugar Chamado Notting Hill", date(1999,5,28), 7.1, "Romance", "Comédia", 0, False),
adicionar_filme("A Bela e a Fera", date(1991,11,22), 8.0, "Romance", "Animação", 0, False),
adicionar_filme("Me Chame pelo seu Nome", date(2017,11,24), 7.9, "Romance", "Drama", 0, False),
adicionar_filme("Doce Novembro", date(2001,2,16), 6.7, "Romance", "Drama", 0, False),
adicionar_filme("Romeu + Julieta", date(1996,11,1), 6.7, "Romance", "Drama", 0, False),
adicionar_filme("Um Amor para Recordar", date(2002,1,25), 7.3, "Romance", "Drama", 0, False)
adicionar_filme("Blade Runner", date(1982,6,25), 8.1, "Ficção Científica", "Suspense", 0, False),
adicionar_filme("2001: Uma Odisseia no Espaço", date(1968,4,6), 8.3, "Ficção Científica", "Drama", 0, False),
adicionar_filme("Matrix", date(1999,3,31), 8.7, "Ficção Científica", "Ação", 0, False),
adicionar_filme("De Volta para o Futuro", date(1985,7,3), 8.5, "Ficção Científica", "Aventura", 0, False),
adicionar_filme("Exterminador do Futuro 2: O Julgamento Final", date(1991,7,3), 8.5, "Ficção Científica", "Ação", 0, False),
adicionar_filme("E.T. - O Extraterrestre", date(1982,6,11), 7.8, "Ficção Científica", "Aventura", 0, False),
adicionar_filme("A Chegada", date(2016,11,10), 7.9, "Ficção Científica", "Drama", 0, False),
adicionar_filme("Star Wars: Uma Nova Esperança", date(1977,5,25), 8.6, "Ficção Científica", "Aventura", 0, False),
adicionar_filme("Minority Report: A Nova Lei", date(2002,6,21), 7.6, "Ficção Científica", "Ação", 0, False),
adicionar_filme("O Quinto Elemento", date(1997,5,7), 7.7, "Ficção Científica", "Ação", 0, False),
adicionar_filme("O Exterminador do Futuro", date(1984,10,26), 8.0, "Ficção Científica", "Ação", 0, False),
adicionar_filme("A.I. - Inteligência Artificial", date(2001,6,29), 7.2, "Ficção Científica", "Drama", 0, False),
adicionar_filme("Se Beber, Não Case!", date(2009,6,5), 7.7, "Comédia", "Aventura", 0, False),
adicionar_filme("Superbad: É Hoje", date(2007,8,17), 7.6, "Comédia", "Drama", 0, False),
adicionar_filme("As Branquelas", date(2004,6,23), 5.6, "Comédia", "Ação", 0, False),
adicionar_filme("Todo Mundo em Pânico", date(2000,7,7), 6.2, "Comédia", "Terror", 0, False),
adicionar_filme("Debi & Lóide: Dois Idiotas em Apuros", date(1994,12,16), 7.3, "Comédia", "Aventura", 0, False),
adicionar_filme("Missão Madrinha de Casamento", date(2011,5,13), 6.8, "Comédia", "Romance", 0, False),
adicionar_filme("Ace Ventura: Um Detetive Diferente", date(1994,2,4), 6.9, "Comédia", "Aventura", 0, False),
adicionar_filme("Se Eu Fosse Você", date(2006,1,6), 6.7, "Comédia", "Romance", 0, False),
adicionar_filme("Curtindo a Vida Adoidado", date(1986,6,11), 7.8, "Comédia", "Drama", 0, False),
adicionar_filme("American Pie: A Primeira Vez é Inesquecível", date(1999,7,9), 7.0, "Comédia", "Romance", 0, False),
adicionar_filme("Zumbilândia", date(2009,10,2), 7.6, "Comédia", "Terror", 0, False),
adicionar_filme("As Patricinhas de Beverly Hills", date(1995,7,19), 6.8, "Comédia", "Romance", 0, False),
adicionar_filme("Escola de Rock", date(2003,10,3), 7.1, "Comédia", "Música", 0, False),
adicionar_filme("Uma Noite no Museu", date(2006,12,22), 6.4, "Comédia", "Aventura", 0, False),
adicionar_filme("A Escolha Perfeita", date(2012,9,28), 7.1, "Comédia", "Música", 0, False),
adicionar_filme("Meu Malvado Favorito", date(2010,7,9), 7.6, "Comédia", "Animação", 0, False),
adicionar_filme("Seven: Os Sete Crimes Capitais", date(1995,9,22), 8.6, "Suspense", "Drama", 0, False),
adicionar_filme("O Silêncio dos Inocentes", date(1991,2,14), 8.6, "Suspense", "Drama", 0, False),
adicionar_filme("Ilha do Medo", date(2010,2,19), 8.2, "Suspense", "Drama", 0, False),
adicionar_filme("Clube da Luta", date(1999,10,15), 8.8, "Suspense", "Drama", 0, False),
adicionar_filme("Cisne Negro", date(2010,12,17), 8.0, "Suspense", "Drama", 0, False),
adicionar_filme("Sexto Sentido", date(1999,8,6), 8.1, "Suspense", "Drama", 0, False),
adicionar_filme("A Garota com a Tatuagem de Dragão", date(2011,1,21), 7.8, "Suspense", "Drama", 0, False),
adicionar_filme("O Segredo dos Seus Olhos", date(2009,8,13), 8.2, "Suspense", "Drama", 0, False),
adicionar_filme("O Sexto Sentido", date(1999,8,6), 8.1, "Suspense", "Drama", 0, False),
adicionar_filme("Prisioneiros", date(2013,9,20), 8.1, "Suspense", "Drama", 0, False),
adicionar_filme("A Vila", date(2004,7,30), 6.5, "Suspense", "Drama", 0, False),
adicionar_filme("A Janela Secreta", date(2004,3,12), 6.6, "Suspense", "Drama", 0, False),
adicionar_filme("Chamada de Emergência", date(2013,3,15), 6.7, "Suspense", "Drama", 0, False),
adicionar_filme("O Homem Duplicado", date(2013,10,4), 6.9, "Suspense", "Drama", 0, False),
adicionar_filme("Oldboy", date(2003,11,21), 8.4, "Suspense", "Drama", 0, False)

# função para recomendar filme
def recomendar_filme(genero1, genero2):

    lista_de_filmes_filtrada = [filme for filme in lista_de_filmes if not filme.recomendado]

    # Calcular a pontuação para cada filme filtrado
    pontuacao_lista = []
    for filme in lista_de_filmes_filtrada:
        x = 1 if genero1 == filme.genero1 else 0
        y = 1 if genero2 == filme.genero2 else 0

        if filme.data >= date(2022, 1, 1):
            z = 1
        elif filme.data <= date(2018, 12, 31):
            z = 0.9
        else:
            z = 0.8

        p = (filme.nota / 6) + x + y + z
        p = p * 2.17
        p = round(p,2)
        filme.pontuacao_algoritmo = p
        pontuacao_lista.append(p)

    if pontuacao_lista:
        indice_maior_pontuacao = pontuacao_lista.index(max(pontuacao_lista))
        filme_recomendado = lista_de_filmes_filtrada[indice_maior_pontuacao]

        filme_recomendado.recomendado = True

        return filme_recomendado
    else:
        return None


# rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        genero1_index = int(request.form['genero1'])
        genero2_index = int(request.form['genero2'])
        genero1 = generos[genero1_index]
        genero2 = generos[genero2_index]

        if genero1 == genero2:
            erro = "Os gêneros selecionados devem ser diferentes."
            return render_template("index.html", filme_recomendado=None, erro=erro)

        filme_recomendado = recomendar_filme(genero1, genero2)
        return render_template("index.html", filme_recomendado=filme_recomendado, erro=None)

    return render_template("index.html", filme_recomendado=None, erro=None)


# execução da aplicação
if __name__ == '__main__':
    app.run(debug=True)