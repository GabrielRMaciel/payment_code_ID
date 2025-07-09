# Sistema de Identificação de Cobranças - Empresa de Tecnologia Web

Sistema padronizado para identificação e controle de cobranças de serviços web, com códigos únicos para cada tipo de serviço, cliente e fase do projeto.

## 📋 Estrutura do Código de Identificação

### Formato Geral
```
XXYYSSSSSSDV
```

**Componentes:**
- **XX**: Tipo de serviço/produto (2 caracteres)
- **YY**: Ano atual (2 últimos dígitos)
- **SSSSSS**: Sigla da empresa cliente (6 caracteres)
- **DV**: Dígito verificador (2 caracteres)

**Exemplo:** `WS25TECHNO6C`

## 🔧 Tipos de Serviços/Produtos

| Código | Serviço | Descrição | Exemplo |
|--------|---------|-----------|---------|
| **WS** | Desenvolvimento de Sites Institucionais | Sites corporativos, portfólios, landing pages | `WS25000001AB` |
| **EC** | Lojas Virtuais / E-commerce | Plataformas de venda online, marketplaces | `EC25000002CD` |
| **SW** | Sistemas Web Personalizados | ERPs, CRMs, dashboards, sistemas internos | `SW25000003EF` |
| **AP** | Aplicações Mobile | Apps iOS, Android, PWAs | `AP25000004GH` |
| **HD** | Hospedagem e Domínios | Serviços de hosting, registro de domínios | `HD25000005IJ` |
| **MS** | Manutenção e Suporte | Atualizações, correções, suporte técnico | `MS25000006KL` |
| **MD** | SEO e Marketing Digital | Otimização, Google Ads, redes sociais | `MD25000007MN` |
| **DG** | Design Gráfico e UX/UI | Identidade visual, layouts, prototipagem | `DG25000008OP` |
| **CT** | Consultoria Tecnológica | Análise de sistemas, arquitetura, estratégia digital | `CT25000009QR` |
| **TR** | Treinamentos e Cursos | Capacitação em tecnologia, workshops | `TR25000010ST` |

## 🏢 Sistema de Siglas de Empresas (6 caracteres)

### Regra Principal
- **Primeira palavra:** Primeiras 3 letras
- **Segunda palavra:** Primeiras 3 letras
- **Resultado:** 6 caracteres sempre em maiúsculo

### Exemplos de Formação
```
TechnoSoft Sistemas → TECHNO
Moda Fashion Store → MODAFA
Construtora Reforma → CONSTR
Dr. João Silva → DRJOAO
Restaurante Gourmet → RESTAU
Farmácia Popular → FARMAC
```

### Regras Especiais

#### Para nomes com uma palavra:
- Usar as primeiras 6 letras
- Exemplo: `Microsoft → MICROS`

#### Para nomes com mais de duas palavras:
- Primeira palavra: 3 letras + Segunda palavra: 3 letras
- Exemplo: `Construtora Silva & Associados → CONSIL`

#### Para nomes com títulos (Dr., Dra., etc.):
- Incluir título + nome
- Exemplo: `Dr. Carlos Pereira → DRCARL`

#### Para nomes com conectivos (&, E, DE, DA, DO):
- Ignorar conectivos
- Exemplo: `Silva & Santos → SILSAN`

#### Para nomes curtos:
- Completar com X
- Exemplo: `Tech → TECHXX`

## 📊 Exemplos de Siglas por Segmento

### Clínicas e Consultórios
- `CLINME` - Clínica Médica
- `DRPEDR` - Dr. Pedro Silva
- `ODONTO` - Odontologia Moderna
- `FISIOT` - Fisioterapia Total

### Lojas e Comércio
- `MODAFA` - Moda Fashion
- `SUPERM` - Supermercado
- `FARMAC` - Farmácia Popular
- `PETSHP` - Pet Shop

### Indústrias
- `INDMET` - Indústria Metalúrgica
- `FABRIC` - Fábrica Têxtil
- `CONSTR` - Construtora
- `ELETR1` - Eletrônica Ltda

### Serviços
- `ESCRITT` - Escritório Advocacia
- `CONTAB` - Contabilidade
- `CONSUL` - Consultoria
- `DESPAC` - Despachante

### Restaurantes
- `RESTAU` - Restaurante Gourmet
- `PIZZAR` - Pizzaria Italiana
- `HAMBUR` - Hamburguer House
- `LANCHE` - Lanchonete

## 🔐 Lógica de Geração do Dígito Verificador

### Algoritmo Personalizado
1. Soma ponderada dos valores ASCII dos primeiros 10 caracteres
2. Multiplicadores: `3, 7, 1, 9, 3, 7, 1, 9, 3, 7` (sequencialmente)
3. Módulo 36 para gerar caracteres alfanuméricos
4. Segundo dígito baseado na soma do primeiro com valor original

### Exemplo de Cálculo para `WS25TECHNO`
```
W(87)×3 + S(83)×7 + 2(50)×1 + 5(53)×9 + T(84)×3 + E(69)×7 + C(67)×1 + H(72)×9 + N(78)×3 + O(79)×7
= 261 + 581 + 50 + 477 + 252 + 483 + 67 + 648 + 234 + 553 = 3606

Primeiro DV = 3606 % 36 = 6 → 6
Segundo DV = (3606 + 6) % 36 = 12 → C

Resultado: WS25TECHNO6C
```

## 📅 Categorização por Fases do Projeto

### Tipos de Cobrança
- **Entrada/Sinal (30% do valor)** - Sufixo: `E`
- **Desenvolvimento/Parcelas (50% do valor)** - Sufixo: `D`
- **Entrega/Final (20% do valor)** - Sufixo: `F`
- **Mensalidade/Recorrente** - Sufixo: `M`

### Exemplos
```
WS25TECHNOE6 - Sinal (30%) - Site institucional
WS25TECHNOD7 - Desenvolvimento (50%) - Site institucional
WS25TECHNOF8 - Entrega (20%) - Site institucional
HD25TECHNOM9 - Hospedagem mensal do site
```

## 💼 Exemplos Práticos por Projeto

### Projeto Site Institucional Completo (TechnoSoft)
```
WS25TECHNOE6 - Sinal (30%) - Site institucional
WS25TECHNOD7 - Desenvolvimento (50%) - Site institucional
WS25TECHNOF8 - Entrega (20%) - Site institucional
HD25TECHNOM9 - Hospedagem mensal do site
```

### Projeto E-commerce Completo (Moda Fashion)
```
EC25MODAFAE1 - Sinal (30%) - Loja virtual
EC25MODAFAD2 - Desenvolvimento (50%) - Loja virtual
EC25MODAFAF3 - Entrega (20%) - Loja virtual
MS25MODAFAM4 - Manutenção mensal da loja
```

### Projeto Sistema Personalizado (Construtora)
```
SW25CONSTRE5 - Sinal (30%) - Sistema ERP
SW25CONSTRD6 - Desenvolvimento (50%) - Sistema ERP
SW25CONSTRF7 - Entrega (20%) - Sistema ERP
TR25CONSTRU8 - Treinamento de usuários
```

## 📈 Tabela de Referência por Porte de Cliente

### Pequenas Empresas
| Serviço | Código | Cliente | Exemplo |
|---------|--------|---------|---------|
| Site Básico | WS | Pet Shop | `WS25PETSHPK8` |
| Loja Simples | EC | Farmácia | `EC25FARMACL9` |
| Hospedagem Básica | HD | Clínica | `HD25CLINMEM0` |

### Médias Empresas
| Serviço | Código | Cliente | Exemplo |
|---------|--------|---------|---------|
| Site Avançado | WS | Restaurante | `WS25RESTAUN1` |
| Sistema Web | SW | Escritório | `SW25ESCRITO2` |
| Marketing Digital | MD | Indústria | `MD25INDMETP3` |

### Grandes Empresas
| Serviço | Código | Cliente | Exemplo |
|---------|--------|---------|---------|
| Site Premium | WS | Construtora | `WS25CONSTRQ4` |
| Sistema Complexo | SW | Hospital | `SW25HOSPISR5` |
| Consultoria | CT | Metalúrgica | `CT25METALS6` |

## 📊 Relatórios Gerenciais

### Por Tipo de Serviço
- **WS**: Quantos sites foram desenvolvidos
- **EC**: Quantas lojas virtuais foram criadas
- **SW**: Quantos sistemas personalizados
- **HD**: Receita recorrente de hospedagem

### Por Modalidade
- **Entrada (E)**: Sinais recebidos
- **Desenvolvimento (D)**: Parcelas intermediárias
- **Final (F)**: Entregas finalizadas
- **Mensal (M)**: Receita recorrente

### Por Período
- **Ano atual (25)**: Todos os projetos de 2025
- **Comparativo mensal**: Crescimento/redução por tipo

## ✅ Vantagens para Empresa de Tecnologia

### Controle de Projetos
- Identificação rápida do tipo de serviço
- Acompanhamento de fases do projeto
- Controle de receita recorrente vs. pontual

### Gestão Financeira
- Separação clara entre entrada, desenvolvimento e entrega
- Controle de mensalidades (hospedagem, manutenção)
- Análise de rentabilidade por tipo de serviço

### Relatórios Comerciais
- Quantos sites vs. sistemas vs. apps foram vendidos
- Sazonalidade dos serviços
- Clientes com maior volume de projetos

## 🚀 Como Usar

1. **Identifique o tipo de serviço** usando a tabela de códigos
2. **Gere a sigla do cliente** seguindo as regras estabelecidas
3. **Aplique o ano atual** (2 últimos dígitos)
4. **Calcule o dígito verificador** usando o algoritmo
5. **Adicione o sufixo** conforme a fase do projeto

## 📝 Licença

Este sistema foi desenvolvido para uso interno de empresas de tecnologia web e pode ser adaptado conforme necessário.

---

*Documentação atualizada em 2025 - Sistema de Identificação de Cobranças v1.0*
