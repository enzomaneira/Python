"""
Herança

A ideia de herança é reutilizar código e extender nossas classes.

Sobrescrita de método ocorre quando reescrevemos um método presente na super classe
em classes filhas

Herança Múltipla -> possibilidade de uma classe herdar de múltiplas classes fazendo
com que a classe filha herde todos os atributos e métodos de todas classes herdadas.
  - Multiderivação Direta
  - Multiderivação Indireta

Polimorfismo

Poli -> muitos
Morfis -> formas

Quando a gente reinplementa um método presente na classe pai em classes filhas
estamos realizando uma sobrescrita de método(Overriting)

Overrting é a melhor representação do Polimorfismo

Métodos Mágicos
 - Métodos que utilizam dunder

   - Dunder Init

"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    "Cliente herda de pessoa"

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    "Funcionário herda de Pessoa"

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Enzo', 'Maneira', '48717402859', 2400)
funcionario1 = Funcionario('Jão', 'Da Silva', '49318238910', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)

# Propriedades

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor





conta1 = Conta('Enzo', 3000, 5000)
conta2 = Conta('Miguel', 200, 600)

print(conta1.extrato())
print(conta2.extrato())

print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)
print(conta1.limite)

# Herança Múltipla

# Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class Multiderivada(Base1, Base2, Base3):
    pass

# Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3):
    pass


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou o {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
         return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou o {self._Animal__nome} do mar'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou o {self._Animal__nome} da terra'

class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)

# Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Cadu')
print(tatu.andar())
print(tatu.cumprimentar())

deslizo = Pinguim('Deslizo')
print(deslizo.andar())
print(deslizo.nadar())
print(deslizo.cumprimentar())

# Objeto é instância de...

print(f'Deslizo é instância de Pinguim? {isinstance(deslizo, Pinguim)}')
print(f'Deslizo é instância de Aquatico? {isinstance(deslizo, Aquatico)}')
print(f'Deslizo é instância de Terrestre? {isinstance(deslizo, Terrestre)}')
print(f'Deslizo é uma instância de objeto? {isinstance(deslizo, object)}')

# Polimorfismo

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa ser implementada')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala auau')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala squick')

filipe = Gato('Filipe')
filipe.comer()
filipe.falar()

fiel = Cachorro('Fiel')
fiel.comer()
fiel.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()

# Métodos Mágicos

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __len__(self):
        return self.paginas

    def __del__(self):
         print('Um objeto do tipo livro foi deletado da memória')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Não é possível multiplicar'

livro1 = Livro('1984', 'George Orwell', 405)
livro2 = Livro('Age of The Spiritual Machines', 'Ray Kurzwell', 283 )

print(livro1)
print(livro2)
print(len(livro1))