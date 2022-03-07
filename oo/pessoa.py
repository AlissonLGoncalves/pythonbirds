class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35, ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_eatributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass


if __name__ == '__main__':
    alisson = Homem(nome='Alisson')
    edivaldo = Homem(alisson, nome='Edivaldo')
    print(Pessoa.cumprimentar(edivaldo))
    print(id(edivaldo))
    print(edivaldo.cumprimentar())
    print(edivaldo.nome)
    print(edivaldo.idade)
    for filho in edivaldo.filhos:
        print(filho.nome)
    edivaldo.sobrenome = 'Gonçalves'
    del edivaldo.filhos
    edivaldo.olhos = 1
    del edivaldo.olhos
    print(edivaldo.__dict__)
    print(alisson.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(edivaldo.olhos)
    print(alisson.olhos)
    print(id(Pessoa.olhos), id(edivaldo.olhos), id(alisson.olhos))
    print(Pessoa.metodo_estatico(), edivaldo.metodo_estatico())
    print(Pessoa.nome_eatributos_de_classe(), edivaldo.nome_eatributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(alisson, Pessoa))
    print(isinstance(alisson, Homem))
