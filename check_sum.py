
class Verificador():
    def __init__(self, entrada):
        self.entrada = entrada

    def exibe_entrada(self):
        print("Mensagem de entrada: " + self.entrada)

    def criptografa_entrada(self):
        """Varre a lista e a guarda com o valor unicode (ASCI) da entrada"""
        lista = []
        for i in str(self.entrada):
            lista.append(ord(i))

        return lista

    def soma_entrada(self):
        lista = self.criptografa_entrada()
        soma = 0
        for i in lista:
            soma += i

        return soma
    
    def soma_saida(self):
        lista = self.descriptografa_entrada()
        soma = 0
        for i in lista:
            soma += i

        return soma
    
    def descriptografa_entrada(self):
        lista = self.criptografa_entrada()
        lista_saida = []
        print("Mensagem de saida: ", end="")
        for i in lista:
            print(chr(i), end="")
            lista_saida.append(i)

        return lista_saida

    def check_sum(self):
        if self.soma_entrada() == self.soma_saida():
            return "\nTudo ok"
        
        return "\nERRO!"
    
    def analisa(self):
        self.exibe_entrada()
        print(self.check_sum())


entrada = input("Digite uma entrada: ")

verificador = Verificador(entrada)

verificador.analisa()