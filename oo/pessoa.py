class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    alisson = Pessoa(nome='Alisson')
    edivaldo = Pessoa(alisson, nome='Edivaldo')
    print(Pessoa.cumprimentar(edivaldo))
    print(id(edivaldo))
    print(edivaldo.cumprimentar())
    print(edivaldo.nome)
    print(edivaldo.idade)
    for filho in edivaldo.filhos:
        print(filho.nome)
    edivaldo.sobrenome = 'Gonçalves'
    del edivaldo.filhos
    print(edivaldo.__dict__)
    print(alisson.__dict__)