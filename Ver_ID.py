import datetime

SERVICOS = {
    "WS": "Desenvolvimento de Sites Institucionais",
    "EC": "Lojas Virtuais / E-commerce",
    "SW": "Sistemas Web Personalizados",
    "AP": "Aplicações Mobile",
    "HD": "Hospedagem e Domínios",
    "MS": "Manutenção e Suporte",
    "MD": "SEO e Marketing Digital",
    "DG": "Design Gráfico e UX/UI",
    "CT": "Consultoria Tecnológica",
    "TR": "Treinamentos e Cursos"
}

FASES_PROJETO = {
    "E": "Entrada/Sinal (30%)",
    "D": "Desenvolvimento/Parcelas (50%)",
    "F": "Entrega/Final (20%)",
    "M": "Mensalidade/Recorrente"
}

MULTIPLICADORES = [3, 7, 1, 9, 3, 7, 1, 9, 3, 7]

ALFANUMERICO = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def gerar_sigla_empresa(nome_empresa: str) -> str:
    conectivos = ['&', 'E', 'DE', 'DA', 'DO']
    palavras = nome_empresa.upper().split()
    
    if palavras[0].startswith(("DR", "DRA")):
        nome_principal = "".join(palavras[1:])
        sigla = palavras[0][:3] + nome_principal[:3]
        return sigla.ljust(6, 'X')[:6]

    palavras_filtradas = [p for p in palavras if p not in conectivos]

    if not palavras_filtradas:
        return "XXXXXX"

    if len(palavras_filtradas) == 1:
        sigla = palavras_filtradas[0][:6]
    else:
        primeira_palavra = palavras_filtradas[0]
        segunda_palavra = palavras_filtradas[1]
        sigla = primeira_palavra[:3] + segunda_palavra[:3]

    return sigla.ljust(6, 'X')

def calcular_dv(base_code: str) -> str:
    soma_ponderada = 0
    for i, char in enumerate(base_code):
        soma_ponderada += ord(char) * MULTIPLICADORES[i]

    primeiro_dv_index = soma_ponderada % 36
    dv1 = ALFANUMERICO[primeiro_dv_index]

    segundo_dv_index = (soma_ponderada + primeiro_dv_index) % 36
    dv2 = ALFANUMERICO[segundo_dv_index]

    return dv1 + dv2

def gerar_codigo_cobranca_interativo():
    print("\n--- Gerador de Código de Cobrança ---")
    
    nome_cliente = input("Digite o nome da empresa cliente: ")
    sigla_cliente = gerar_sigla_empresa(nome_cliente)
    print(f"-> Sigla gerada para '{nome_cliente}': {sigla_cliente}\n")

    print("Selecione o tipo de serviço/produto:")
    for codigo, descricao in SERVICOS.items():
        print(f"  {codigo} - {descricao}")
    
    codigo_servico = ""
    while codigo_servico not in SERVICOS:
        codigo_servico = input("Digite o código do serviço (ex: WS, EC): ").upper()
        if codigo_servico not in SERVICOS:
            print("Código inválido. Por favor, escolha um da lista.")
    
    ano_atual = str(datetime.datetime.now().year)[2:]
    base_codigo = f"{codigo_servico}{ano_atual}{sigla_cliente}"
    print(f"\n-> Base do código (sem DV): {base_codigo}")

    dv = calcular_dv(base_codigo)
    print(f"-> Dígito Verificador (DV) calculado: {dv}\n")
    
    print("Selecione a fase do projeto para adicionar o sufixo:")
    for sufixo, descricao in FASES_PROJETO.items():
        print(f"  {sufixo} - {descricao}")

    sufixo_fase = ""
    while sufixo_fase not in FASES_PROJETO:
        sufixo_fase = input("Digite o sufixo da fase (E, D, F, M): ").upper()
        if sufixo_fase not in FASES_PROJETO:
            print("Sufixo inválido. Por favor, escolha um da lista.")

    codigo_final = f"{base_codigo}{sufixo_fase}{dv[0]}"
    
    print("\n-------------------------------------------------")
    print("           CÓDIGO DE COBRANÇA GERADO           ")
    print("-------------------------------------------------")
    print(f"Cliente: {nome_cliente}")
    print(f"Serviço: {SERVICOS[codigo_servico]}")
    print(f"Fase: {FASES_PROJETO[sufixo_fase]}")
    print(f"\nCódigo Final: {codigo_final}")
    print("-------------------------------------------------\n")

def validar_codigo_interativo():
    print("\n--- Validador de Código de Cobrança ---")
    codigo = input("Digite o código de cobrança para validar: ").upper()

    if len(codigo) != 12:
        print(f"\n[FALHA] O código '{codigo}' é INVÁLIDO. Motivo: O comprimento deve ser de 12 caracteres.")
        return

    base_codigo = codigo[:10]
    servico_code = base_codigo[:2]
    ano = base_codigo[2:4]
    sigla = base_codigo[4:10]

    if servico_code not in SERVICOS:
        print(f"\n[FALHA] O código '{codigo}' é INVÁLIDO. Motivo: Código de serviço '{servico_code}' não reconhecido.")
        return
    if not ano.isdigit():
        print(f"\n[FALHA] O código '{codigo}' é INVÁLIDO. Motivo: A parte do ano '{ano}' deve ser numérica.")
        return

    dv_calculado = calcular_dv(base_codigo)
    is_valid = False
    
    possivel_sufixo = codigo[10]
    dv_informado_str = ""
    fase_info = "Não aplicável (código padrão)"

    if possivel_sufixo in FASES_PROJETO:
        dv_informado = codigo[11]
        dv_informado_str = f"{dv_informado} (1º Dígito)"
        fase_info = f"{possivel_sufixo} ({FASES_PROJETO[possivel_sufixo]})"
        if dv_informado == dv_calculado[0]:
            is_valid = True
    else:
        dv_informado = codigo[10:]
        dv_informado_str = dv_informado
        if dv_informado == dv_calculado:
            is_valid = True

    status = "[SUCESSO] O código é VÁLIDO." if is_valid else "[FALHA] O código é INVÁLIDO."
    print(f"\n{status}")
    print("---------------------------------------------")
    print("        DETALHES DO CÓDIGO ANALISADO         ")
    print("---------------------------------------------")
    print(f"* Código de Serviço (XX): {servico_code} ({SERVICOS[servico_code]})")
    print(f"* Ano do Projeto (YY):    {ano} (Refere-se ao ano de 20{ano})")
    print(f"* Sigla do Cliente (SSSSSS): {sigla}")
    print(f"* Fase do Projeto:        {fase_info}")
    print(f"* Dígito Verificador (DV):  {dv_informado_str}")
    print("---------------------------------------------")
    if not is_valid:
        print(f"Motivo da Falha: O Dígito Verificador informado não corresponde ao DV calculado para a base '{base_codigo}'.")
        print(f"DV Informado: {dv_informado_str} | DV Calculado Esperado: {dv_calculado}")
    print("")

def main():
    print("=================================================================")
    print("   Sistema de Identificação de Cobranças - Empresa Web Tech")
    print("=================================================================")

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Gerar Código de Cobrança")
        print("2. Validar Código de Cobrança")
        print("3. Sair")
        
        escolha = input("Escolha uma opção (1, 2 ou 3): ")

        if escolha == '1':
            gerar_codigo_cobranca_interativo()
        elif escolha == '2':
            validar_codigo_interativo()
        elif escolha == '3':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")


if __name__ == "__main__":
    main()
