"""
Orientação a Objetos

 - Paradigma de programação que utiliza um mapeamento
 de objetos do mundo real para modelos computacionais

- Paradigma de programação é a forma/metodologia utilizada
 para pensar/desenvolver sistemas

 Principais elementos da Orientação a Objetos:
  - Classe -> MOdelo do objeto do mundo real sendo representado computacionamelte;
  - Atributo -> Característica do Objeto;
  - Método -> Comportamento do objeto(função);
  - Construtor -> Método especial utilizado para criar os objetos;
  - Objeto -> Instância da classe.

Classes podem contar:
   - Atributos -> Representam características do objeto. Ou seja, pelos atributos conseguimos
   representar computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente
   iriamos querer saber voltagem, cor, e luminosidade.

   - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este
   objeto pode realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum
    que muito provavelmente iríamos querer representar no nosso sistema é o de ligar e desligar.

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema,
chamamos estes objetos que serão mapeados por classes de entidades.

Atributos:
        - de instância
        - de classe
        - dinâmicos
# Atributos de instância: são atributos declarados dentro do método construtor.

Em Python por convenção ficou estabelecido que, todo atribudo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizando somente dentro de uma própria classe onde está declarado,
utiliza-se __ duplo underline no início do nome
Isso é conhecido como Name Mangling

 - Métodos -> representam os comportamentos do objeto. Ou seja, as ações
 que este objeto pode realizar no seu sistema.
      - Métodos de classe
      - Métodos de instância

# Método dunder init é um método especial chamado construtor e
sua função é construir o objeto a partir da classe.

 - Objetos -> São instâncias de classe. Ou seja, após o mapeamento do objeto do mundo real para sua
 representação computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar
 nos objetos/instâncias de uma classe com variáveis do tipo definido na classe.

Abstração e Encapsulamento

O grande objeto da POaO é encapsular nosso código dentro de um grupo lógico e hierárquico
utilizando classes.

Encapsular -> cápsula

Abstração -> ato de expor apenas dados relevantes de uma classe, escondendo atributos
e métodos privados do usuário.
"""

numero = 10

print(numero)
print(type(numero))

class Produto:
    pass

ps4 = Produto()
print(ps4)
print(type(ps4))

# Classes

class Lampada:
    pass

lamp = Lampada()
print(type(lamp))

# Atributos

# Classes com istância publica
class Lampada:

    def __init__(self, voltagem, cor, luminosidade):
        self.voltagem = voltagem
        self.cor = cor
        self.luminosidade = luminosidade
        self.ligada = False

class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributos públicos e privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def mostra_senha(self):
        print(self.senha)

    def mostra_email(self):
        print(self.email)


# Obs: lembre-se que isso é apenas uma convenção

# Exemplo

user = Acesso('enzo@maneira.com', 'Miguel2007')

print(user.email)
# print(user.senha)  #Attribute error

# print(user.Acesso__senha)  # Temos acesso, mas não deveríamos

user.mostra_email()
user.mostra_senha()

# O que são atributos de instância?

# Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias,
# terão estes atributos

user1 = Acesso('enzomaneira@outlook.com', 'Suasescolhas16')

user1.mostra_email()
user1.mostra_senha()

# Atributos de classe

p1 = Produto('Playstation 5', 'Video Game', '5000')
p2 = Produto('Xbox S', 'Video Game', '3200')

# Atributos de classe são atributos que são declarados diretamente na classe, ou seja
# fora do construtor. Geralmente ja inicializamos um valor, e este valor é compartilhado entre
# todas as instâncias da classe. Ou seja, ao invés de cada instância de classe ter seus próprios
# valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias
# terão o mesmo valor para este atributo.

# Refatorar a classe Produto

class Produto:

    # Atributo de classe
    imposto = 1.05  #0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

    def desconto(self, porcentagem):
        """"Retorna o valor do produto com desconto"""
        return(self.valor * (100 - porcentagem))/100

p1 = Produto('Playstation 5', 'Video Game', 5000)
p2 = Produto('Xbox S', 'Video Game', 3200)

print(p2.valor)

print(p1.id)
print(p2.id)

# Atributo dinâmico -> Um atributo de instância que pode ser criado em tempo de execução

# O atributo pode ser exclusivo da instância que o criou

p2.peso = '5kg'

print(f' Produto: {p2.nome}\n Descrição: {p2.descricao}\n Valor: {p2.valor}\n Peso: {p2.peso}')

# Deletando

del p2.peso

print(p2.__dict__)

# Métodos

def __init__(self, nome, descricao, valor):
    self.__id = Produto.contador + 1
    self.__nome = nome
    self.__descricao = descricao
    self.__valor = (valor * Produto.imposto)
    Produto.contador = self.id


def desconto(self, porcentagem):
    """"Retorna o valor do produto com desconto"""
    return (self.valor * (100 - porcentagem)) / 100

print(p1.desconto(50))
print(Produto.desconto(p1, 40))


from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

# user1 = Usuario('Enzo', 'Maneira', 'enzo@maneira.com', 'Miguel2007')

# print(user1.nome_completo())
# print(Usuario.nome_completo(user1))

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere')
    exit(42)

print('Usuário criado com sucesso')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

# print(f'Senha user Criptografado: {user.Usuario__senha}')  # Acesso errado

# Métodos de classe

class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuários no sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod
    def definicao():
        return 'UXR433'

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def gera_usuario(self):
        return self.__email.split('0')[0]

user = Usuario('Miguel', 'Maneira', 'mimaneira@hotmail.com', '140402001')

Usuario.conta_usuarios()  # Forma correta
user.conta_usuarios()  # Forma possível, mas incorreta

# Instância/Objetos

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.limite = limite
        self.saldo = saldo
        self.cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')

class Lampada:

    def __init__(self, voltagem, cor, luminosidade):
        self.cor = cor
        self.voltagem = voltagem
        self.luminosidade = luminosidade
        self.ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

lamp1 = Lampada('branca', 110, 60)

lamp1.ligar_desligar()

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')


cc = ContaCorrente(5000, 20000, 'Enzo Maneira')

cc.mostra_cliente()

# Abstração e Encapsulamento

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
            print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valor precisa ser positivo')

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        self.__valor -= valor
        conta_destino.__saldo += valor

conta1 = Conta('Enzo Maneira', 200, 1500)

# print(conta1.numero)  # Só funciona com públicos
# print(conta1.titular)
# print(conta1.saldo)
# print(conta1.limite)

conta1.depositar(100)

print(Conta.__dict__)