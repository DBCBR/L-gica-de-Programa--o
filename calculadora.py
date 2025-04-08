# Calculadora #

# Autor: David Barcellos Cardoso #
# Data de Criação: 08/04/2025 #

def exibir_mensagem_boas_vindas():
    """Exibe a mensagem inicial do programa."""
    print("Bem-vindo à Calculadora!")
    print("Você pode realizar as seguintes operações: +, -, *, /")
    print("Digite 'sair' para encerrar o programa.")

def solicitar_operacao():
    """Solicita ao usuário a operação desejada."""
    return input("Digite a operação desejada (+, -, *, /, 'sair'): ").strip()

def solicitar_numero(mensagem):
    """Solicita um número ao usuário e trata entradas inválidas."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

def calcular(operacao, num1, num2):
    """
    Realiza a operação matemática com base nos parâmetros fornecidos.

    Parâmetros:
    - operacao (str): Operação desejada (+, -, *, /).
    - num1 (float): Primeiro número.
    - num2 (float): Segundo número.

    Retorna:
    - Resultado da operação ou mensagem de erro.
    """
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2 if num2 != 0 else "Erro: Divisão por zero não é permitida."

def main():
    """Função principal que executa o programa."""
    exibir_mensagem_boas_vindas()

    while True:
        operacao = solicitar_operacao()

        if operacao.lower() == "sair":
            print("Encerrando o programa.")
            break

        if operacao not in ["+", "-", "*", "/"]:
            print("Operação inválida. Tente novamente.")
            continue

        num1 = solicitar_numero("Digite o primeiro número: ")
        num2 = solicitar_numero("Digite o segundo número: ")

        resultado = calcular(operacao, num1, num2)
        print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")

# Executa o programa
if __name__ == "__main__":
    main()
