# padrão de nomeação de classe é o PascalCase
# para criá-la devemos usar a palavra reservada class
class ContaBancaria:
    # atributos
    # método construtor
    # self é uma referência ao próprio objeto
    def __init__(self, def_titular, def_saldo):
        self.titular = def_titular
        self.__saldo = def_saldo
    # métodos
    def consultar_saldo(self):
        print(self.__saldo)
    
    def sacar(self, valor):
        self.__saldo = self.__saldo - valor
    
    def depositar(self, valor):
        self.__saldo = self.__saldo + valor

# criei uma classe herdando de outra
class ContaCorrente(ContaBancaria):
    def __init__(self, def_titular, def_saldo, limite):
        super().__init__(def_titular, def_saldo)
        self.limite = limite

    # polimorfismo
    def consultar_saldo(self):
        super().consultar_saldo()
        print(self.limite)