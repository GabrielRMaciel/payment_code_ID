# Sistema de Identificação de Cobranças - Empresa de Tecnologia Web

Um sistema robusto de identificação e categorização de cobranças para empresas de tecnologia web, permitindo controle detalhado de projetos, fases e modalidades de pagamento.

## 📋 Índice

- [Estrutura do Código](#estrutura-do-código)
- [Tipos de Serviços](#tipos-de-serviços)
- [Modalidades de Cobrança](#modalidades-de-cobrança)
- [Algoritmo de Verificação](#algoritmo-de-verificação)
- [Categorização por Fases](#categorização-por-fases)
- [Exemplos Práticos](#exemplos-práticos)
- [Relatórios e Análises](#relatórios-e-análises)
- [Vantagens](#vantagens)

## 🏗️ Estrutura do Código

O sistema utiliza um código de identificação com 12 caracteres no formato:

```
XXYYZZZZZZDV
```

### Componentes:
- **XX**: Tipo de serviço/produto (2 caracteres)
- **YY**: Ano atual (2 últimos dígitos)
- **ZZZZZZ**: Sequencial único (6 dígitos)
- **DV**: Dígito verificador (2 caracteres)

**Exemplo**: `WS25000001AB`

## 🛠️ Tipos de Serviços

| Código | Serviço | Descrição | Exemplo |
|--------|---------|-----------|---------|
| `WS` | Sites Institucionais | Sites corporativos, portfólios, landing pages | `WS25000001AB` |
| `EC` | E-commerce | Plataformas de venda online, marketplaces | `EC25000002CD` |
| `SW` | Sistemas Web | ERPs, CRMs, dashboards, sistemas internos | `SW25000003EF` |
| `AP` | Aplicações Mobile | Apps iOS, Android, PWAs | `AP25000004GH` |
| `HD` | Hospedagem e Domínios | Serviços de hosting, registro de domínios | `HD25000005IJ` |
| `MS` | Manutenção e Suporte | Atualizações, correções, suporte técnico | `MS25000006KL` |
| `MD` | Marketing Digital | SEO, Google Ads, redes sociais | `MD25000007MN` |
| `DG` | Design Gráfico | Identidade visual, layouts, prototipagem | `DG25000008OP` |
| `CT` | Consultoria Tecnológica | Análise de sistemas, arquitetura, estratégia | `CT25000009QR` |
| `TR` | Treinamentos | Capacitação em tecnologia, workshops | `TR25000010ST` |

## 📊 Modalidades de Cobrança

### Sites Institucionais (WS)
- **Básico**: Até 5 páginas
- **Avançado**: Até 15 páginas  
- **Premium**: Ilimitado + funcionalidades extras

### E-commerce (EC)
- **Básico**: Até 50 produtos
- **Profissional**: Até 500 produtos
- **Enterprise**: Produtos ilimitados

### Sistemas Web (SW)
- **Simples**: Até 3 módulos
- **Intermediário**: Até 8 módulos
- **Complexo**: Módulos ilimitados

### Hospedagem (HD)
- **Básico**: 1GB, 1 domínio
- **Profissional**: 5GB, 3 domínios
- **Enterprise**: Recursos ilimitados

## 🔐 Algoritmo de Verificação

O sistema utiliza um algoritmo personalizado para gerar o dígito verificador:

### Processo:
1. **Soma ponderada** dos valores ASCII dos primeiros 10 caracteres
2. **Multiplicadores**: `3, 7, 1, 9, 3, 7, 1, 9, 3, 7` (sequencialmente)
3. **Módulo 36** para gerar caracteres alfanuméricos
4. **Segundo dígito** baseado na soma do primeiro com valor original

### Exemplo de Cálculo para `WS25000001`:
```
W(87)×3 + S(83)×7 + 2(50)×1 + 5(53)×9 + 0(48)×3 + 0(48)×7 + 0(48)×1 + 0(48)×9 + 0(48)×3 + 1(49)×7
= 261 + 581 + 50 + 477 + 144 + 336 + 48 + 432 + 144 + 343 = 2816

Primeiro DV = 2816 % 36 = 8 → 8
Segundo DV = (2816 + 8) % 36 = 20 → K

Resultado: WS25000001K8
```

## 🎯 Categorização por Fases

### Sufixos de Fase:
- **E (Entrada)**: 30% do valor - Sinal do projeto
- **D (Desenvolvimento)**: 50% do valor - Parcelas intermediárias
- **F (Final)**: 20% do valor - Entrega final
- **M (Mensal)**: Cobrança recorrente

### Exemplos:
- `WS25000001E8` - Sinal de site institucional
- `WS25000001D9` - Desenvolvimento de site institucional
- `WS25000001F0` - Entrega final de site institucional
- `HD25000001M5` - Hospedagem mensal

## 💼 Exemplos Práticos

### Projeto Site Institucional Completo:
```
WS25000001E8 - Sinal (30%)
WS25000001D9 - Desenvolvimento (50%)
WS25000001F0 - Entrega (20%)
HD25000001M5 - Hospedagem mensal
```

### Projeto E-commerce Completo:
```
EC25000002E1 - Sinal (30%)
EC25000002D2 - Desenvolvimento (50%)
EC25000002F3 - Entrega (20%)
MS25000001M4 - Manutenção mensal
```

### Projeto Sistema Personalizado:
```
SW25000003E5 - Sinal (30%)
SW25000003D6 - Desenvolvimento (50%)
SW25000003F7 - Entrega (20%)
TR25000001U8 - Treinamento de usuários
```

## 📈 Relatórios e Análises

### Por Tipo de Serviço:
- **WS**: Quantidade de sites desenvolvidos
- **EC**: Quantidade de lojas virtuais criadas
- **SW**: Quantidade de sistemas personalizados
- **HD**: Receita recorrente de hospedagem

### Por Modalidade:
- **Entrada (E)**: Sinais recebidos
- **Desenvolvimento (D)**: Parcelas intermediárias
- **Final (F)**: Entregas finalizadas
- **Mensal (M)**: Receita recorrente

### Por Período:
- **Ano atual (25)**: Todos os projetos de 2025
- **Comparativo mensal**: Crescimento/redução por tipo

## ✨ Vantagens

### Controle de Projetos:
- ✅ Identificação rápida do tipo de serviço
- ✅ Acompanhamento de fases do projeto
- ✅ Controle de receita recorrente vs. pontual

### Gestão Financeira:
- ✅ Separação clara entre entrada, desenvolvimento e entrega
- ✅ Controle de mensalidades (hospedagem, manutenção)
- ✅ Análise de rentabilidade por tipo de serviço

### Relatórios Comerciais:
- ✅ Quantificação de sites vs. sistemas vs. apps vendidos
- ✅ Análise de sazonalidade dos serviços
- ✅ Identificação de clientes com maior volume de projetos

## 📚 Referência por Tipo de Cliente

### Pequenas Empresas:
| Serviço | Código | Descrição | Exemplo |
|---------|--------|-----------|---------|
| Site Básico | WS | Até 5 páginas | `WS25000001K8` |
| Loja Simples | EC | Até 50 produtos | `EC25000001L9` |
| Hospedagem Básica | HD | 1GB, 1 domínio | `HD25000001M0` |

### Médias Empresas:
| Serviço | Código | Descrição | Exemplo |
|---------|--------|-----------|---------|
| Site Avançado | WS | Até 15 páginas | `WS25000002N1` |
| Sistema Web | SW | Até 8 módulos | `SW25000001O2` |
| Marketing Digital | MD | SEO + Ads | `MD25000001P3` |

### Grandes Empresas:
| Serviço | Código | Descrição | Exemplo |
|---------|--------|-----------|---------|
| Site Premium | WS | Ilimitado | `WS25000003Q4` |
| Sistema Complexo | SW | Módulos ilimitados | `SW25000002R5` |
| Consultoria | CT | Estratégia digital | `CT25000001S6` |

---

## 🤝 Contribuição

Este sistema foi desenvolvido para otimizar o controle financeiro e operacional de empresas de tecnologia web. Para sugestões ou melhorias, por favor abra uma issue ou pull request.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
