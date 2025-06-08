# Criando-um-sistema-banc-rio-com-Python
Sistema bancário do desafio do Bootcamp da DIO
Neste desafio, a proposta era criar um sistema bancário com as seguintes funções:
- Depósito
- Saque
- Visualizar Extrato
Conforme especificado no desafio, o projeto deveria seguir as seguintes regras:
### Depósito:
- Não é permitido o depósito de valores negativos ( valor_deposito > 0 ).
### Saque:
- Cada saque não pode ultrapassar o valor de R$ 500,00.
- O usuário tem um limite diário de 3 saques.
### Visualizar extrato:
- Esta função deve listar os depósitos e saques registrados anteriormente, e ao final apresentar o saldo da conta.
### Incrementos adicionados ao desafio:
**Com o intuito de incrementar o que foi proposto pelo desafio, adicionei as seguintes funções:**
- Este Sistema Bancário não aceitaria o depósito de moedas. Para verificar esta condição, utilizei a fórmula: (valor_deposito % 1 > 0).
- Através da biblioteca "datetime", importei a função "sleep" para o programa aguardar alguns segundos para processar as escolhas do usuário.
