from datetime import datetime
from typing import Dict, Tuple

class GeradorCobrancaWeb:
    """
    Gera e valida um ID de cobrança para uma Empresa de Tecnologia Web,
    seguindo a estrutura e as regras definidas no documento de especificação.
    
    Estrutura: XXYYZZZZZZDV
    """

    def __init__(self):
        """
        Inicializa o gerador com os dados e regras do documento.
        """
        # Mapeamento de tipos de serviço/produto
        self.servicos = {
            'WS': 'Desenvolvimento de Sites Institucionais',
            'EC': 'Lojas Virtuais / E-commerce',
            'SW': 'Sistemas Web Personalizados',
            'AP': 'Aplicações Mobile',
            'HD': 'Hospedagem e Domínios',
            'MS': 'Manutenção e Suporte',
            'MD': 'SEO e Marketing Digital',
            'DG': 'Design Gráfico e UX/UI',
            'CT': 'Consultoria Tecnológica',
            'TR': 'Treinamentos e Cursos'
        }
        
        # Multiplicadores para o cálculo do DV, conforme especificado
        self.multiplicadores = [3, 7, 1, 9, 3, 7, 1, 9, 3, 7]

    def _to_base36(self, number: int) -> str:
        """
        Converte um número (0-35) para seu caractere Base36 (0-9, A-Z).
        Necessário para o cálculo do Módulo 36.
        """
        if 0 <= number <= 9:
            return str(number)
        elif 10 <= number <= 35:
            return chr(ord('A') + number - 10)
        raise ValueError("Número fora do intervalo da Base36 (0-35).")

    def _calcular_dv(self, base_id: str) -> str:
        """
        Calcula o Dígito Verificador (DV) de 2 caracteres com o algoritmo personalizado.
        """
        # 1. Soma ponderada dos valores ASCII
        soma_ponderada = 0
        for i, char in enumerate(base_id):
            soma_ponderada += ord(char) * self.multiplicadores[i]
            
        # 2. Cálculo do primeiro caractere do DV
        dv1_valor = soma_ponderada % 36
        dv1_char = self._to_base36(dv1_valor)
        
        # 3. Cálculo do segundo caractere do DV
        dv2_valor = (soma_ponderada + dv1_valor) % 36
        dv2_char = self._to_base36(dv2_valor)
        
        return dv1_char + dv2_char

    def gerar_id(self, tipo_servico: str, sequencial: int) -> str:
        """
        Gera um ID de cobrança completo.
        """
        if tipo_servico.upper() not in self.servicos:
            raise ValueError(f"Tipo de serviço '{tipo_servico}' é inválido.")
        
        if not (0 <= sequencial <= 999999):
            raise ValueError("O sequencial deve estar entre 0 e 999999.")
            
        # Formato: XX (Tipo) YY (Ano) ZZZZZZ (Sequencial)
        ano = str(datetime.now().year)[-2:]
        sequencial_str = f"{sequencial:06d}"
        base_id = tipo_servico.upper() + ano + sequencial_str
        
        dv = self._calcular_dv(base_id)
        return base_id + dv

    def validar_id(self, id_completo: str) -> Tuple[bool, Dict]:
        """
        Valida um ID de cobrança completo.
        """
        id_completo = id_completo.upper()
        if len(id_completo) != 12:
            return False, {"erro": "ID inválido. O comprimento deve ser de 12 caracteres."}
            
        try:
            base_id = id_completo[:10]
            dv_informado = id_completo[10:]
            
            tipo_servico = base_id[:2]
            if tipo_servico not in self.servicos:
                return False, {"erro": f"Código de serviço '{tipo_servico}' não reconhecido."}
            
            dv_calculado = self._calcular_dv(base_id)
            
            if dv_calculado != dv_informado:
                return False, {"erro": f"Dígito verificador inválido. Esperado: {dv_calculado}, Recebido: {dv_informado}."}

            info = {
                "valido": True,
                "id_completo": id_completo,
                "servico": self.servicos[tipo_servico],
                "codigo_servico": tipo_servico,
                "ano": f"20{base_id[2:4]}",
                "sequencial": base_id[4:10],
                "dv": dv_informado
            }
            return True, info

        except Exception as e:
            return False, {"erro": f"Erro inesperado na validação: {str(e)}"}

# --- SEÇÃO INTERATIVA EM TEMPO REAL ---
if __name__ == "__main__":
    gerador = GeradorCobrancaWeb()
    print("=== Sistema de Identificação de Cobranças (Empresa de Tecnologia Web) ===")

    # O loop 'while True' mantém o programa rodando para receber dados em tempo real
    while True:
        print("\n--- MENU ---")
        print("1. Gerar novo Código de Cobrança")
        print("2. Validar um Código existente")
        print("3. Listar todos os Tipos de Serviço")
        print("4. Sair")
        
        # A função 'input()' pausa o programa e espera o usuário digitar uma opção
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("\n-- GERAR NOVO CÓDIGO --")
            try:
                # Pede os dados em tempo real
                tipo = input("Digite o código do serviço (ex: WS, EC, SW): ").upper()
                seq = int(input("Digite o número sequencial (de 0 a 999999): "))
                
                # Gera o resultado com base nos dados inseridos
                id_gerado = gerador.gerar_id(tipo, seq)
                print("-" * 40)
                print(f"✅ CÓDIGO GERADO: {id_gerado}")
                print("-" * 40)
            except ValueError as e:
                print(f"\n❌ ERRO: {e}")

        elif escolha == '2':
            print("\n-- VALIDAR CÓDIGO --")
            id_para_validar = input("Digite o código de 12 caracteres para validar: ")
            
            valido, info = gerador.validar_id(id_para_validar)
            
            print("-" * 40)
            if valido:
                print("✅ CÓDIGO VÁLIDO!")
                print("Detalhes:")
                print(f"  - Serviço: {info['servico']} ({info['codigo_servico']})")
                print(f"  - Ano: {info['ano']}")
                print(f"  - Sequencial: {info['sequencial']}")
                print(f"  - Dígito Verificador: {info['dv']}")
            else:
                print(f"❌ CÓDIGO INVÁLIDO!")
                print(f"   Motivo: {info['erro']}")
            print("-" * 40)

        elif escolha == '3':
            print("\n-- TIPOS DE SERVIÇO DISPONÍVEIS --")
            for codigo, descricao in gerador.servicos.items():
                print(f"  - Código: {codigo} -> {descricao}")

        elif escolha == '4':
            print("\nSaindo do sistema.")
            break
        else:
            print("\nOpção inválida. Por favor, tente novamente.")