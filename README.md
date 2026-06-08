# Sistema de Monitoramento de Missão Espacial Sustentável

## Integrantes
Guilherme Figueira Velloso - RM: 568827

José Augusto Ribeiro Freire Manfrinato - RM: 571151

## Resumo do Projeto
Sistema inteligente desenvolvido em Python para monitoramento de sistemas energéticos em uma missão espacial experimental. A aplicação simula o recebimento de telemetria (temperatura, comunicação, energia) e utiliza estruturas lógicas para a tomada de decisão automatizada, visando a eficiência energética e a segurança dos módulos operacionais.

## Funcionalidades
* **Monitoramento em Tempo Real:** Interpretação de dados simulados de geração solar e status da bateria.
* **Geração de Alertas:** Identificação de temperaturas críticas e falhas de comunicação.
* **Tomada de Decisão Autônoma:** Desligamento de módulos não essenciais (ex: módulo de pesquisa) para preservação de energia em momentos de déficit.
* **Dashboard em Terminal:** Visualização limpa e estruturada dos indicadores vitais da missão.

## Como Executar
1. Clone o repositório:
   `git clone [https://github.com/crfvelloso/GS_SERS/tree/main]`
2. Acesse a pasta do projeto e execute o script:
   `python main.py`

## Tecnologias Utilizadas
* Python 3.14
* Módulos nativos (`random`, `time`)
