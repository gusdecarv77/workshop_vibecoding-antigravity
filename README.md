# workshop_vibecoding-antigravity
Workshop de Vibe Coding no Antigravity IDE
============================================

# 💼 CRM Inteligente - Pipeline de Vendas

Este é um MVP (Produto Mínimo Viável) de um **CRM Inteligente** focado no controle e análise de pipelines de vendas. Desenvolvido em Python utilizando o framework **Streamlit**, o app oferece uma interface moderna, reativa e interativa para acompanhamento de leads, análise de métricas financeiras e exportação de dados para tomada de decisões estratégicas.

---

## 🚀 Funcionalidades Principais

*   **📊 Indicadores Financeiros (Métricas)**:
    *   **Total de Leads Ativos**: Contagem em tempo real da base de contatos.
    *   **Valor em Negociação**: Soma financeira dos leads que estão no estágio de Negociação.
    *   **Faturamento Realizado**: Soma financeira dos negócios já Fechados.
    *   *Todos os valores monetários são exibidos no padrão brasileiro (`R$ X.XXX,XX`).*

*   **⚡ Cadastro Ágil de Leads**: 
    *   Formulário intuitivo na barra lateral para registrar novos contatos informando: nome do contato, empresa, valor estimado do contrato e status atual.
    *   A tela e os relatórios são atualizados de forma instantânea ao salvar o registro (`st.rerun`).

*   **🧠 Score de Prioridade Automático**:
    *   Uma regra de negócio inteligente avalia cada lead em tempo real e define o nível de prioridade na tabela:
        *   **ALTO**: Valor do contrato $\ge$ `R$ 10.000,00` e status de `Negociação`.
        *   **MÉDIO**: Valor entre `R$ 5.000,00` e `R$ 10.000,00` ou status de `Prospecção`.
        *   **BAIXO**: Demais casos (ex: contratos fechados ou de menor valor).

*   **📈 Dashboard de Analytics Interativo**:
    *   Gráfico de barras verticais desenvolvido com **Plotly Express** exibindo a distribuição do volume financeiro acumulado por status do pipeline.
    *   Cores corporativas harmonizadas e elegantes para facilitar a leitura visual rápida.

*   **📥 Exportação Inteligente**:
    *   Botão para download dos dados em formato **CSV** compatível com o Microsoft Excel em português (usando separador de ponto e vírgula `;` e codificação `utf-8-sig` para evitar problemas com acentuação).

*   **🧹 Limpeza de Sessão**:
    *   Botão discreto na barra lateral para apagar todos os registros da memória e reiniciar o estado limpo do app.

---

## 🛠️ Tecnologias Utilizadas

*   **[Python](https://www.python.org/)** (v3.8+)
*   **[Streamlit](https://streamlit.io/)** (Framework para interface web)
*   **[Pandas](https://pandas.pydata.org/)** (Manipulação e estruturação de dados)
*   **[Plotly](https://plotly.com/)** (Gráficos interativos prêmios)

---

## 📦 Como Instalar e Executar Localmente

### Pré-requisitos
Certifique-se de ter o **Python** instalado na sua máquina.

### Passo 1: Instalar as Dependências
Abra seu terminal (PowerShell, Command Prompt ou Terminal do VS Code) e instale as bibliotecas necessárias executando o comando abaixo:

```bash
pip install streamlit pandas plotly
```

### Passo 2: Executar o Aplicativo
Navegue até a pasta onde está o arquivo `crm_app.py` e execute o comando:

```bash
streamlit run crm_app.py
```

O aplicativo iniciará um servidor web local e abrirá automaticamente no seu navegador de internet padrão através do endereço `http://localhost:8501`.

---

## 📂 Estrutura do Projeto

```text
CRM_app/
│
├── crm_app.py       # Código-fonte principal da aplicação
└── README.md        # Documentação e guia do projeto
```

---

## 📝 Licença

Este projeto é de código aberto e está disponível sob a licença MIT. Sinta-se livre para clonar, modificar e expandir de acordo com suas necessidades de negócio!
