
class Verificador():
    """Classe responsável por verificar se a entrada é a mesma da saída"""

    def __init__(self, entrada):
        """Método construtor"""
        self.entrada = entrada

    def exibe_entrada(self):
        """Exibe a mensagem que o usuário digitou sem nenhuma verificação"""
        print("Mensagem de entrada: " + self.entrada)

    def criptografa_entrada(self):
        """Varre a entrada e a guarda uma lista com o valor unicode (ASCI) da entrada"""
        lista = []
        for i in str(self.entrada):
            lista.append(ord(i))

        return lista

    def soma_entrada(self):
        """Faz um somatório total com os inteiros da lista no valor de entrada"""
        lista = self.criptografa_entrada()
        soma = 0
        for i in lista:
            soma += i

        return soma
    
    def soma_saida(self):
        """Faz a soma da lista que foi preenchida para a saída"""
        lista = self.descriptografa_entrada()
        soma = 0
        for i in lista:
            soma += i

        return soma
    
    def descriptografa_entrada(self):
        """Peda os valores UNICODE e reverte para string"""
        lista = self.criptografa_entrada()
        lista_saida = []
        print("Mensagem de saida: ", end="")
        for i in lista:
            print(chr(i), end="")
            lista_saida.append(i)

        return lista_saida

    def check_sum(self):
        """Faz a verificação se a entrada e a saída possuem a mesma soma de valores UNICODE"""
        if self.soma_entrada() == self.soma_saida():
            return "\nTudo ok"
        
        return "\nERRO!"
    
    def analisa(self):
        """Chama os métodos"""
        self.exibe_entrada()
        print(self.check_sum())


entrada = input("Digite uma entrada: ")

verificador = Verificador(entrada)

verificador.analisa()