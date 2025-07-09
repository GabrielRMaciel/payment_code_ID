import datetime

# --- Dicionários e Constantes Baseadas no Documento ---

# Dicionário de serviços/produtos com seus códigos 
SERVICOS = {
    "WS": "Desenvolvimento de Sites Institucionais", # [cite: 10, 11]
    "EC": "Lojas Virtuais / E-commerce", # [cite: 14, 15]
    "SW": "Sistemas Web Personalizados", # [cite: 18, 19]
    "AP": "Aplicações Mobile", # [cite: 22, 23]
    "HD": "Hospedagem e Domínios", # [cite: 26, 27]
    "MS": "Manutenção e Suporte", # [cite: 30, 31]
    "MD": "SEO e Marketing Digital", # [cite: 33, 34]
    "DG": "Design Gráfico e UX/UI", # [cite: 36, 37]
    "CT": "Consultoria Tecnológica", # [cite: 40, 41]
    "TR": "Treinamentos e Cursos" # [cite: 44, 45]
}

# Fases do projeto com sufixos 
FASES_PROJETO = {
    "E": "Entrada/Sinal (30%)", # [cite: 118, 119]
    "D": "Desenvolvimento/Parcelas (50%)", # [cite: 121, 122]
    "F": "Entrega/Final (20%)", # [cite: 124, 125]
    "M": "Mensalidade/Recorrente" # [cite: 127, 128]
}

# Multiplicadores para o cálculo do Dígito Verificador (DV) [cite: 107]
MULTIPLICADORES = [3, 7, 1, 9, 3, 7, 1, 9, 3, 7]

# Caracteres para o Módulo 36
ALFANUMERICO = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# --- Funções de Geração da Sigla ---

def gerar_sigla_empresa(nome_empresa: str) -> str:
    """
    Gera uma sigla de 6 caracteres para o nome da empresa com base nas regras.
    [cite: 48]
    """
    # Ignorar conectivos e títulos comuns [cite: 67, 70]
    conectivos = ['&', 'E', 'DE', 'DA', 'DO']
    palavras = nome_empresa.upper().split()
    
    # Tratamento para títulos como Dr., Dra.
    if palavras[0].startswith(("DR", "DRA")):
        nome_principal = "".join(palavras[1:])
        sigla = palavras[0][:3] + nome_principal[:3]
        return sigla.ljust(6, 'X')[:6] # [cite: 66, 68]

    palavras_filtradas = [p for p in palavras if p not in conectivos]

    if not palavras_filtradas:
        return "XXXXXX"

    # Regra para nome com uma palavra [cite: 58, 59]
    if len(palavras_filtradas) == 1:
        sigla = palavras_filtradas[0][:6]
    # Regra principal para duas ou mais palavras [cite: 51, 52, 63, 64]
    else:
        primeira_palavra = palavras_filtradas[0]
        segunda_palavra = palavras_filtradas[1]
        sigla = primeira_palavra[:3] + segunda_palavra[:3]

    # Completa com 'X' se a sigla for curta [cite: 74]
    return sigla.ljust(6, 'X')


# --- Funções de Cálculo do Dígito Verificador ---

def calcular_dv(base_code: str) -> str:
    """
    Calcula o Dígito Verificador (DV) de 2 caracteres.
    
    """
    soma_ponderada = 0
    # Soma ponderada dos valores ASCII dos 10 primeiros caracteres [cite: 106]
    for i, char in enumerate(base_code):
        soma_ponderada += ord(char) * MULTIPLICADORES[i]

    # Primeiro DV: Módulo 36 do resultado [cite: 108, 114]
    primeiro_dv_index = soma_ponderada % 36
    dv1 = ALFANUMERICO[primeiro_dv_index]

    # Segundo DV: Soma do resultado com o primeiro valor, depois módulo 36 [cite: 109, 115]
    segundo_dv_index = (soma_ponderada + primeiro_dv_index) % 36
    dv2 = ALFANUMERICO[segundo_dv_index]

    return dv1 + dv2


# --- Função Principal Interativa ---

def gerar_codigo_cobranca_interativo():
    """
    Função principal que interage com o usuário para gerar o código de cobrança.
    """
    print("--- Gerador de Código de Cobrança Interativo ---")
    print("Bem-vindo ao sistema de identificação de cobranças da Empresa de Tecnologia Web.\n") # [cite: 1, 2]

    # 1. Obter nome do cliente e gerar sigla
    nome_cliente = input("Digite o nome da empresa cliente: ")
    sigla_cliente = gerar_sigla_empresa(nome_cliente)
    print(f"-> Sigla gerada para '{nome_cliente}': {sigla_cliente}\n") # [cite: 7]

    # 2. Selecionar o tipo de serviço
    print("Selecione o tipo de serviço/produto:")
    for codigo, descricao in SERVICOS.items():
        print(f"  {codigo} - {descricao}")
    
    codigo_servico = ""
    while codigo_servico not in SERVICOS:
        codigo_servico = input("Digite o código do serviço (ex: WS, EC): ").upper()
        if codigo_servico not in SERVICOS:
            print("Código inválido. Por favor, escolha um da lista.")
    
    # 3. Montar a base do código
    ano_atual = str(datetime.datetime.now().year)[2:] # [cite: 6]
    base_codigo = f"{codigo_servico}{ano_atual}{sigla_cliente}" # [cite: 4]
    print(f"\n-> Base do código (sem DV): {base_codigo}")

    # 4. Calcular o Dígito Verificador (DV)
    dv = calcular_dv(base_codigo)
    print(f"-> Dígito Verificador (DV) calculado: {dv}\n") # [cite: 8]
    
    codigo_com_dv = base_codigo + dv

    # 5. Selecionar a fase do projeto
    print("Selecione a fase do projeto para adicionar o sufixo:")
    for sufixo, descricao in FASES_PROJETO.items():
        print(f"  {sufixo} - {descricao}")

    sufixo_fase = ""
    while sufixo_fase not in FASES_PROJETO:
        sufixo_fase = input("Digite o sufixo da fase (E, D, F, M): ").upper()
        if sufixo_fase not in FASES_PROJETO:
            print("Sufixo inválido. Por favor, escolha um da lista.")

    # Inserir o sufixo antes do DV. O documento tem exemplos ambíguos.
    # Ex: WS25TECHNOE6 [cite: 120] vs WS25TECHNO6C[cite: 116].
    # Optei por inserir o sufixo ANTES do primeiro dígito do DV, pois é o padrão 
    # mais comum nos exemplos de faturamento por fase.
    # Exemplo: WS25TECHNOE6, onde o 'E' é o sufixo e '6' é o primeiro dígito verificador.
    # Esta implementação assume que o DV é calculado sobre a base e depois o sufixo é inserido.
    # Se a regra for diferente, o posicionamento do sufixo pode ser ajustado.
    
    # Vamos seguir o padrão dos exemplos práticos [cite: 132, 134, 137]
    # Formato: XXYYSSSSSS(Sufixo)(DV1)
    # Por simplicidade e consistência com os exemplos, vamos adotar essa estrutura:
    codigo_final = f"{base_codigo}{sufixo_fase}{dv[0]}"
    
    print("\n-------------------------------------------------")
    print("           CÓDIGO DE COBRANÇA GERADO           ")
    print("-------------------------------------------------")
    print(f"Cliente: {nome_cliente}")
    print(f"Serviço: {SERVICOS[codigo_servico]}")
    print(f"Fase: {FASES_PROJETO[sufixo_fase]}")
    print(f"\nCódigo Final: {codigo_final}")
    print("-------------------------------------------------\n")


if __name__ == "__main__":
    gerar_codigo_cobranca_interativo()
