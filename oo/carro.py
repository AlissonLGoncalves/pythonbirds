"""
Você deve criar uma classe carro que irá possuir dois atributos compostos por outras duas classes:?

1) motor
O motor terá a resposabilidade de controlar a velocidade.
ele oferecerá os seguintes atributos:
a) Atributo de dado velocidade
b) Método acelerar, que deverá incrementar a velocidade de uma unidade
c) Método frear que deverá decrementar a velocidade em duas unidades.

2)Direção
A direção terá a resposabilidade de controlar a direção. Ela oferecerá os seguintes atributos:
a) Valor de direção com valores possíveis: norte, sul, leste oeste.
b) método girar_a_direita
c) método girar_a_esquerda

    N
O       L
    S


    Exemplo>
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> #teste direção
    >>> direcao = Direcao()
    >>> diretacao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> diretacao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> diretacao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> diretacao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> diretacao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> diretacao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> diretacao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> diretacao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> diretacao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    >>>'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    >>>'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>>'Norte'
    >>>carro.girar_a_esquerda()
    >>>carro.calcular_direcao()
    >>>'Oeste'
"""

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao:
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
