class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        print(f'Nome: {self.nome}  Likes: {self.likes}')


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def lista(self):
        return self._programas

    @property
    def tamnaho(self):
        return len(self._programas)


filme1 = Filme("avengers: infinity war", 2018, 149)
filme2 = Filme("lord of the rings: The Fellowship of the Ring", 2001, 178)
serie1 = Serie("mr. robot", 2017, 4)
serie2 = Serie("Daredevil ", 2015, 3)

# testando dar likes
filme1.dar_likes()
filme1.dar_likes()
filme2.dar_likes()
filme2.dar_likes()
filme2.dar_likes()
filme2.dar_likes()
filme2.dar_likes()
serie1.dar_likes()
serie1.dar_likes()
serie1.dar_likes()
serie2.dar_likes()

# testando o setter para o nome
# filme1.nome = "novo nome"
# print(filme1.nome)

# inicio do codigo da playlist
lista_de_programas = [filme1, filme2, serie1, serie2]
minha_playlist = Playlist("minha lista de programas", lista_de_programas)

for programa in minha_playlist.lista:
    print(programa)

print(f'Tamanho: {len(minha_playlist.lista)} itens')
