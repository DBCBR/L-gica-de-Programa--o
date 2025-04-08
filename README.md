# Lógica de Programação

Este projeto contém uma calculadora simples desenvolvida em Python. A calculadora permite realizar as operações básicas de adição, subtração, multiplicação e divisão.

## Funcionalidades

- Exibe uma mensagem de boas-vindas ao iniciar.
- Permite realizar as operações matemáticas: `+`, `-`, `*`, `/`.
- Trata entradas inválidas, como números não numéricos e divisão por zero.
- Permite encerrar o programa digitando `sair`.

## Estrutura do Código

### Funções

1. **`exibir_mensagem_boas_vindas`**  
   Exibe a mensagem inicial do programa.

2. **`solicitar_operacao`**  
   Solicita ao usuário a operação desejada.

3. **`solicitar_numero`**  
   Solicita um número ao usuário e trata entradas inválidas.

4. **`calcular`**  
   Realiza a operação matemática com base nos parâmetros fornecidos:
   - `+`: Soma
   - `-`: Subtração
   - `*`: Multiplicação
   - `/`: Divisão (com tratamento para divisão por zero)

5. **`main`**  
   Função principal que executa o programa.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Execute o arquivo `calculadora.py` no terminal:

   ```bash
   python calculadora.py
3. Siga as instruções exibidas no terminal.

Licença
Este projeto está licenciado sob a MIT License.
