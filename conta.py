class Conta:
  
  def __init__(self, numero, titulas,saldo, limite):
    print("Construindo objeto...{}".format(self))
    self.numero = numero
    self.titular = titular
    self.saldo = saldo
    self.limite = limite
   
  def extrato(self):
    print("saldo de {} do ttular {}".format(self.saldo, self.titular))
    
  def depositar(self, valor):
    self. saldo += valor
    
  def saca(self, valor):
    self.saldo -= valor
    
Conta
