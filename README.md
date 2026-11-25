# SOC Log Analyzer

Script em Python que analisa logs de autenticação SSH do Linux e detecta
possíveis ataques de força bruta.

## O que ele faz

1. Lê o arquivo `sample_auth.log` linha por linha
2. Filtra as linhas de falha de senha (`Failed password`)
3. Extrai o IP de origem de cada falha
4. Conta as falhas por IP usando um dicionário
5. Gera um alerta quando um IP chega a 5 falhas ou mais

## Como rodar

    py log_analyzer.py