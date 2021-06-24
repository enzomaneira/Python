"""
Escrevendo um iterador costumizado

 - Funções dentro de uma classe são chamada de Métodos
"""

class Contador:
    def __int__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

