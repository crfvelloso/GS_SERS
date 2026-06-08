import time
import random

def gerar_dados_telemetria():
    return {
        "temperatura": random.uniform(-50.0, 150.0),
        "energia_bateria": random.uniform(0.0, 100.0),
        "geracao_solar": random.uniform(0.0, 50.0),
        "comunicacao": random.choice(["ESTAVEL", "INSTAVEL", "PERDIDA"]),
        "modulos": {
            "suporte_vida": "ATIVO",
            "propulsao": random.choice(["ATIVO", "INATIVO"]),
            "pesquisa": "ATIVO"
        }
    }

def analisar_dados(dados):
    alertas = []
    decisoes = []

    if dados["temperatura"] > 80.0:
        alertas.append("ALERTA CRÍTICO: Temperatura acima do limite (80°C).")
        decisoes.append("AÇÃO: Ativando sistema de resfriamento de emergência.")
    elif dados["temperatura"] < -20.0:
        alertas.append("ALERTA: Temperatura muito baixa.")
        decisoes.append("AÇÃO: Redirecionando energia para aquecedores centrais.")

    consumo_liquido = 10.0
    balanco_energetico = dados["geracao_solar"] - consumo_liquido

    if dados["energia_bateria"] < 20.0 and balanco_energetico < 0:
        alertas.append("ALERTA CRÍTICO: Bateria baixa e déficit energético.")
        decisoes.append("AÇÃO: Desligando módulo de pesquisa para poupar energia.")
        dados["modulos"]["pesquisa"] = "INATIVO"

    if dados["comunicacao"] == "PERDIDA":
        alertas.append("ALERTA CRÍTICO: Comunicação com a base perdida.")
        decisoes.append("AÇÃO: Iniciando protocolo de navegação autônoma.")

    return alertas, decisoes

def exibir_painel(dados, alertas, decisoes):
    print("="*50)
    print(" PAINEL DE MONITORAMENTO ESPACIAL ".center(50, "="))
    print("="*50)
    print(f"Temperatura: {dados['temperatura']:.2f} °C")
    print(f"Bateria: {dados['energia_bateria']:.2f} %")
    print(f"Geração Solar: {dados['geracao_solar']:.2f} kW")
    print(f"Comunicação: {dados['comunicacao']}")
    print("-" * 50)
    print("STATUS DOS MÓDULOS:")
    for modulo, status in dados["modulos"].items():
        print(f" - {modulo.replace('_', ' ').title()}: {status}")
    print("-" * 50)

    if alertas:
        print("ALERTAS:")
        for alerta in alertas:
            print(f" [!] {alerta}")
    else:
        print("ALERTAS: Nenhum. Sistemas operacionais normais.")

    if decisoes:
        print("-" * 50)
        print("AÇÕES AUTOMATIZADAS:")
        for decisao in decisoes:
            print(f" [*] {decisao}")
    print("="*50)
    print("\n")

def iniciar_missao(ciclos=5):
    for i in range(ciclos):
        print(f"--- CICLO DE MONITORAMENTO {i+1} ---")
        dados = gerar_dados_telemetria()
        alertas, decisoes = analisar_dados(dados)
        exibir_painel(dados, alertas, decisoes)
        time.sleep(2)

if __name__ == "__main__":
    iniciar_missao()
