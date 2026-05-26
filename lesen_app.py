import pandas as pd
import streamlit as st
import plotly.express as px

# 1. Configuração da página em modo "wide" com título profissional
st.set_page_config(
    page_title="Lesen - Aprendizado de Alemão por Leitura",
    layout="wide"
)

# Inicialização do st.session_state com dados fictícios para os textos de alemão
if "textos" not in st.session_state:
    st.session_state["textos"] = [
        {
            "Título": "Das Oktoberfest in München",
            "Nível": "B1",
            "Texto Completo": "Das Oktoberfest in München ist das größte Volksfest der Welt. Es beginnt Ende September und dauert zwei Wochen. Millionen von Besuchern aus der ganzen Welt kommen, um bayerisches Bier zu trinken, traditionelle Musik zu hören und Brezeln zu essen. Die Menschen tragen oft traditionelle Kleidung: Lederhosen für Männer und Dirndl für Frauen. Die Atmosphäre ist immer sehr fröhlich und laut.",
            "Vocabulário": {
                "Volksfest": "Festa popular",
                "dauert": "dura",
                "Besuchern": "visitantes",
                "tragen": "vestem / usam",
                "Lederhosen": "calças de couro tradicionais",
                "Dirndl": "vestido tradicional feminino",
                "fröhlich": "alegre"
            }
        },
        {
            "Título": "Die Energiewende in Deutschland",
            "Nível": "B2",
            "Texto Completo": "Die Energiewende ist eines der wichtigsten Projekte Deutschlands im 21. Jahrhundert. Das Ziel ist es, die Energieversorgung von fossilen Brennstoffen auf erneuerbare Energien wie Wind- und Solarenergie umzustellen. Dies soll den Ausstoß von Treibhausgasen reduzieren und das Klima schützen. Obwohl es viele Herausforderungen gibt, wie zum Beispiel die Speicherung von Strom, ist der Übergang zu einer nachhaltigen Wirtschaft unumgänglich.",
            "Vocabulário": {
                "Energiewende": "transição energética",
                "Energieversorgung": "abastecimento de energia",
                "erneuerbare Energien": "energias renováveis",
                "umzustellen": "mudar / transicionar",
                "Ausstoß": "emissão",
                "Treibhausgasen": "gases de efeito estufa",
                "Herausforderungen": "desafios",
                "Speicherung": "armazenamento",
                "unumgänglich": "inevitável"
            }
        },
        {
            "Título": "Goethes Einfluss auf die Weltliteratur",
            "Nível": "C1/C2",
            "Texto Completo": "Johann Wolfgang von Goethe gilt als der bedeutendste deutsche Dichter und einer der einflussreichsten Intellektuellen der europäischen Geschichte. Sein Werk umfasst Gedichte, Dramen, Romane sowie naturwissenschaftliche Abhandlungen. Sein Meisterwerk 'Faust' reflektiert die existentielle Zerrissenheit des modernen Menschen und dessen unstillbares Streben nach Erkenntnis. Bis heute prägt Goethes literarisches Erbe das deutsche Selbstverständnis und fasziniert Leser weltweit durch seine stilistische Brillanz und philosophische Tiefe.",
            "Vocabulário": {
                "gilt als": "é considerado como",
                "bedeutendste": "mais importante / ilustre",
                "Werk": "obra",
                "umfasst": "abrange / compreende",
                "Zerrissenheit": "dilaceramento / conflito interno",
                "unstillbares": "insaciável",
                "Streben": "busca / aspiração",
                "Erkenntnis": "conhecimento",
                "prägt": "molda / marca",
                "Selbstverständnis": "autoimagem / identidade"
            }
        }
    ]

# Inicialização da lista de textos lidos
if "lidos" not in st.session_state:
    st.session_state["lidos"] = []

# Exibe notificação flutuante de sucesso do cadastro de novos textos
if st.session_state.get("cadastro_texto_sucesso"):
    st.toast("Novo texto cadastrado com sucesso pelo Professor! 🎓", icon="📝")
    st.session_state["cadastro_texto_sucesso"] = False

# Função para converter a string livre de vocabulário em dicionário
def processar_vocabulario(texto_livre):
    vocab = {}
    for linha in texto_livre.split("\n"):
        if "-" in linha:
            partes = linha.split("-", 1)
            de = partes[0].strip()
            pt = partes[1].strip()
            if de and pt:
                vocab[de] = pt
    return vocab


# --- BARRA LATERAL (FILTROS E CONTROLE) ---
st.sidebar.title("📚 Lesen - Menu")

st.sidebar.subheader("🔍 Filtros de Leitura")

# Obter os níveis disponíveis na base de dados dinamicamente
niveis_disponiveis = sorted(list(set(t["Nível"] for t in st.session_state["textos"])))
nivel_filtrado = st.sidebar.selectbox("Nível do Texto", niveis_disponiveis)

# Filtrar textos pelo nível selecionado
textos_filtrados = [t for t in st.session_state["textos"] if t["Nível"] == nivel_filtrado]
nomes_textos_filtrados = [t["Título"] for t in textos_filtrados]

# Selectbox de títulos dos textos filtrados
titulo_selecionado = st.sidebar.selectbox("Escolha o Texto", nomes_textos_filtrados)

# Obter objeto completo do texto selecionado
selected_text = next(t for t in st.session_state["textos"] if t["Título"] == titulo_selecionado)

st.sidebar.markdown("---")
st.sidebar.subheader("🎯 Ações do Aluno")

# Verificar se o texto selecionado já foi marcado como lido
texto_selecionado_lido = selected_text["Título"] in st.session_state["lidos"]

if not texto_selecionado_lido:
    if st.sidebar.button("✅ Marcar Texto como Lido", use_container_width=True):
        st.session_state["lidos"].append(selected_text["Título"])
        st.toast("Leitura concluída registrada! Bom trabalho! 🚀", icon="🎉")
        st.rerun()
else:
    st.sidebar.success("Texto lido! Parabéns! ✅")

# Botão discreto para reiniciar o progresso
st.sidebar.markdown("---")
st.sidebar.subheader("⚙️ Configurações")
if st.sidebar.button("🔄 Reiniciar Progresso", use_container_width=True, type="secondary"):
    st.session_state["lidos"] = []
    st.toast("Seu progresso de leitura foi zerado!", icon="🔄")
    st.rerun()


# --- TELA PRINCIPAL (ESTATÍSTICAS & TABS DE CONTEÚDO) ---
st.title("🇩🇪 Lesen - Alemão por Leitura")
st.subheader("Plataforma de Leitura e Vocabulário para Brasileiros")

# Criação das abas de navegação (Estudo e Gestão do Professor)
tab_estudo, tab_professor = st.tabs(["📖 Estudar Texto", "👨‍🏫 Área do Professor"])

# --- PROCESSAMENTO DE ANALYTICS (KPIs) ---
lidos = st.session_state["lidos"]
textos = st.session_state["textos"]
textos_lidos = [t for t in textos if t["Título"] in lidos]

# Card 1: Quantidade total de textos marcados como lido
total_lidos = len(lidos)

# Card 2: Soma de palavras de vocabulário de apoio únicas desbloqueadas
palavras_desbloqueadas = set()
for t in textos_lidos:
    for palavra in t["Vocabulário"].keys():
        palavras_desbloqueadas.add(palavra.lower().strip())
total_palavras_unicas = len(palavras_desbloqueadas)

# Card 3: Maior nível lido pelo usuário
level_ranks = {"B1": 1, "B2": 2, "C1/C2": 3}
if textos_lidos:
    nivel_max = max(textos_lidos, key=lambda t: level_ranks.get(t["Nível"], 0))["Nível"]
else:
    nivel_max = "Nenhum"


# --- ABA DE ESTUDOS ---
with tab_estudo:
    # 1. Cards de Métricas na parte superior
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric(label="📚 Textos Lidos", value=total_lidos)
    with col_m2:
        st.metric(label="🔑 Palavras Novas Desbloqueadas", value=total_palavras_unicas)
    with col_m3:
        st.metric(label="🏆 Nível de Domínio Atual", value=nivel_max)
        
    st.markdown("---")
    
    # 2. Layout de Duas Colunas (Texto à Esquerda, Gráfico e Ações à Direita)
    col_texto, col_analytics = st.columns([1.3, 1])
    
    with col_texto:
        # Título do Texto Selecionado e Badge Dinâmico de Nível
        st.markdown(f"## {selected_text['Título']}")
        st_colors = {"B1": "blue", "B2": "orange", "C1/C2": "red"}
        st.markdown(f"🏷️ **Nível:** :{st_colors.get(selected_text['Nível'], 'blue')}[{selected_text['Nível']}]")
        st.write("")
        
        # Corpo do Texto
        st.info("📖 **Texto Completo em Alemão:**")
        st.markdown(
            f"<div style='font-size:17px; line-height:1.7; text-align:justify; padding:15px; border-radius:8px;'>"
            f"{selected_text['Texto Completo']}"
            f"</div>",
            unsafe_allow_html=True
        )
        st.write("")
        
        # Vocabulário de apoio
        with st.expander("🔍 Vocabulário de Apoio (Português)", expanded=True):
            if selected_text["Vocabulário"]:
                df_vocab_local = pd.DataFrame([
                    {"Palavra em Alemão": k, "Tradução": v}
                    for k, v in selected_text["Vocabulário"].items()
                ])
                st.dataframe(df_vocab_local, use_container_width=True, hide_index=True)
            else:
                st.info("Este texto não possui vocabulário de apoio cadastrado.")
                
    with col_analytics:
        st.markdown("### 📊 Progresso Geral & Analytics")
        
        # Preparação do gráfico Plotly
        contagem_niveis = {"B1": 0, "B2": 0, "C1/C2": 0}
        for t in textos:
            nivel = t["Nível"]
            contagem_niveis[nivel] = contagem_niveis.get(nivel, 0) + len(t["Vocabulário"])
            
        df_grafico = pd.DataFrame([
            {"Nível": nivel, "Quantidade de Palavras": quant}
            for nivel, quant in contagem_niveis.items()
        ])
        
        # Cores elegantes corporativas (tons de azul e laranja/vermelho)
        color_map = {
            "B1": "#1E88E5",      # Azul Corporativo
            "B2": "#FF8F00",      # Laranja
            "C1/C2": "#E64A19"    # Vermelho/Laranja Escuro
        }
        
        fig = px.bar(
            df_grafico,
            x="Nível",
            y="Quantidade de Palavras",
            color="Nível",
            color_discrete_map=color_map,
            text="Quantidade de Palavras",
            title="Palavras de Apoio Disponíveis por Nível de Texto",
            labels={
                "Nível": "Nível de Dificuldade",
                "Quantidade de Palavras": "Nº de Palavras Úteis"
            },
            category_orders={"Nível": ["B1", "B2", "C1/C2"]}
        )
        
        fig.update_layout(
            showlegend=False,
            margin=dict(l=10, r=10, t=40, b=10),
            height=300,
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            yaxis=dict(showgrid=True, gridcolor="rgba(200, 200, 200, 0.15)"),
            xaxis=dict(showgrid=False)
        )
        fig.update_traces(textposition="outside")
        
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
        
        st.markdown("---")
        
        # Relatório de Exportação (Dicionário Pessoal do Estudante)
        st.markdown("### 🎒 Dicionário Pessoal de Revisão")
        st.write("Exporte a lista completa de palavras exclusivas que você já aprendeu (desbloqueou) nos textos lidos:")
        
        # Estruturar o dicionário pessoal
        vocab_desbloqueado = []
        for t in textos_lidos:
            for de, pt in t["Vocabulário"].items():
                vocab_desbloqueado.append({
                    "Alemão": de,
                    "Português": pt,
                    "Texto de Origem": t["Título"],
                    "Nível": t["Nível"]
                })
        
        if vocab_desbloqueado:
            df_vocab = pd.DataFrame(vocab_desbloqueado)
            # Remove duplicatas de palavras se houver repetições entre textos
            df_vocab = df_vocab.drop_duplicates(subset=["Alemão"])
            
            csv_vocab = df_vocab.to_csv(index=False, sep=";").encode("utf-8-sig")
            st.download_button(
                label="📥 Baixar Dicionário Pessoal (CSV)",
                data=csv_vocab,
                file_name="meu_dicionario_alemao.csv",
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.info("Seu dicionário está vazio. Leia textos para desbloquear palavras de vocabulário de apoio!")


# --- ABA DO PROFESSOR (CADASTRAMENTO) ---
with tab_professor:
    st.header("👨‍🏫 Área do Professor")
    st.write("Cadastre novos textos pedagógicos na plataforma para enriquecer os estudos do aluno.")
    
    # Formulário de Cadastro de Novo Texto
    with st.form(key="professor_form", clear_on_submit=True):
        novo_titulo = st.text_input("Título do Texto")
        novo_nivel = st.selectbox("Nível do Texto", ["B1", "B2", "C1/C2"])
        novo_corpo = st.text_area("Texto Completo em Alemão", height=200)
        
        st.subheader("Vocabulário de Apoio")
        st.write("Digite um termo por linha usando o formato: `Palavra em Alemão - Tradução em Português`")
        novo_vocab_texto = st.text_area(
            "Exemplo de preenchimento:\nSprache - Língua / Idioma\nlernen - aprender\nlesen - ler",
            height=150
        )
        
        submit_professor = st.form_submit_button("Cadastrar Novo Texto")
        
        if submit_professor:
            # Validação do formulário
            if not novo_titulo.strip() or not novo_corpo.strip():
                st.error("Erro no cadastro: Os campos de **Título** e **Texto Completo em Alemão** são obrigatórios!")
            else:
                # Processar o dicionário de vocabulário do campo de texto livre
                dicionario_vocab = processar_vocabulario(novo_vocab_texto)
                
                novo_texto_dict = {
                    "Título": novo_titulo.strip(),
                    "Nível": novo_nivel,
                    "Texto Completo": novo_corpo.strip(),
                    "Vocabulário": dicionario_vocab
                }
                
                # Adicionar ao banco em memória
                st.session_state["textos"].append(novo_texto_dict)
                st.session_state["cadastro_texto_sucesso"] = True
                
                # Forçar recarregamento imediato da tela
                st.rerun()
