# 🏰 A Crônica do Manchado

<div align="center">

🏰⚔️

**O companheiro definitivo de rastreamento de chefes para Elden Ring — em Português do Brasil**

[![Última Versão](https://img.shields.io/github/v/release/felipesenpaidd/A-Cronica-do-Manchado?style=for-the-badge)](https://github.com/felipesenpaidd/A-Cronica-do-Manchado/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/felipesenpaidd/A-Cronica-do-Manchado/total?style=for-the-badge)](https://github.com/felipesenpaidd/A-Cronica-do-Manchado/releases)
[![Licença](https://img.shields.io/github/license/felipesenpaidd/A-Cronica-do-Manchado?style=for-the-badge)](LICENSE)

</div>

---

## 📖 Sobre

**A Crônica do Manchado** é uma aplicação desktop completa para Windows desenvolvida para fãs de Elden Ring que desejam acompanhar detalhadamente sua jornada pelas Terras Intermédias. Não é apenas uma lista estática — é um companheiro interativo e visualmente agradável que monitora seu progresso em tempo real e motiva você a explorar cada canto do mundo do jogo.

> Esta é uma versão totalmente em **Português do Brasil**, com nomes de chefes e localizações conforme a tradução oficial da Bandai Namco.
>
> Projeto original (em inglês) por [RysanekDavid](https://github.com/RysanekDavid/The-Tarnished-Chronicle).

### ✨ Funcionalidades Principais

- **🎯 Rastreamento em Tempo Real** — Detecta automaticamente os chefes derrotados monitorando seu arquivo de save
- **📍 Organização por Localização** — Chefes organizados por áreas do jogo com indicadores de progressão
- **⚔️ Cobertura Completa** — Inclui tanto o jogo base quanto a DLC Sombra da Árvore do Érdtree
- **📊 Estatísticas Detalhadas** — Monitore mortes, tempo de jogo e percentuais de conclusão
- **🎮 Overlay em Jogo** — Overlay mostrando seu progresso atual enquanto joga
- **📹 Integração com OBS** — Exporta estatísticas para arquivos de texto para setups de streaming
- **🔄 Atualizações Automáticas** — Notificações e instalação automática de atualizações
- **🔗 Suporte a Coop** — Compatível com saves Vanilla (.sl2) e Seamless Coop Mod (.co2)

---

## 🚀 Início Rápido

### Instalação

1. **Baixe** o código-fonte ou clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute: `python src/main.py`

### Primeira Configuração

1. **Selecionar Arquivo de Save** — Navegue até seu arquivo de save do Elden Ring:
   - **Elden Ring Padrão**: `ER0000.sl2` (local padrão: `%APPDATA%\EldenRing\[Steam_ID]\ER0000.sl2`)
   - **Seamless Coop Mod**: `ER0000.co2` (mesmo local)
2. **Escolher Personagem** — Selecione qual slot de personagem deseja monitorar
3. **Jogue!** — O aplicativo monitorará seu progresso automaticamente

---

## 📋 Funcionalidades em Detalhe

### 🎯 Rastreamento de Chefes

- **Detecção Automática**: Monitora seu arquivo de save para novos chefes derrotados
- **Marcação Manual**: Clique nas caixas de seleção para marcar chefes manualmente como derrotados
- **Informações Detalhadas**: Clique no nome do chefe para ver estatísticas, número de mortes e registros de abates
- **Função de Busca**: Encontre rapidamente chefes ou localizações específicas

### 📊 Estatísticas

- **Contador de Chefes**: Acompanhe chefes derrotados vs. total disponível
- **Rastreamento de Mortes**: Monitore mortes por chefe e no geral
- **Tempo de Jogo**: Rastreamento de tempo em tempo real e total
- **Percentual de Conclusão**: Indicadores visuais de progresso

### 🎮 Overlay em Jogo

- **Exibição Personalizável**: Mostrar/ocultar diferentes estatísticas (chefes, mortes, tempo, último chefe morto)
- **Personalização de Cor**: Escolha sua cor de texto preferida
- **Tamanho de Fonte**: Ajuste o tamanho do texto do overlay (10-30pt)
- **Sempre Visível**: O overlay permanece visível durante o jogo

### 📹 Integração com OBS

- **Exportação para Arquivo de Texto**: Exporta estatísticas para arquivos `.txt` para fontes de texto do OBS
- **Formatos Personalizáveis**: Defina seus próprios formatos de texto para cada estatística
- **Atualizações em Tempo Real**: Os arquivos atualizam automaticamente enquanto você joga
- **Pronto para Stream**: Perfeito para transmissões ao vivo do seu gameplay no Elden Ring

### 🔄 Filtros de Conteúdo

- **Jogo Base / DLC**: Filtre para mostrar apenas conteúdo do jogo base ou da DLC
- **Ocultar Derrotados**: Opção para ocultar chefes já concluídos
- **Busca por Localização**: Encontre chefes por localização ou nome

---

## 🔧 Configuração

### Configurações do Overlay

- **Ativar Overlay**: Liga/desliga o overlay em jogo
- **Opções de Exibição**: Escolha quais informações mostrar
  - Contador de chefes
  - Contador de mortes
  - Tempo de jogo (com/sem segundos)
  - Último chefe morto
- **Aparência**: Personalize cor do texto e tamanho da fonte

### Configuração da Integração com OBS

1. **Ativar Saída OBS** — Habilite a geração de arquivos OBS
2. **Definir Pasta de Saída** — Escolha onde salvar os arquivos de texto
3. **Configurar Arquivos**:
   - `bosses.txt` — Contador de chefes (ex.: "Chefes: 45/207")
   - `deaths.txt` — Contador de mortes (ex.: "Mortes: 127")
   - `time.txt` — Tempo de jogo (ex.: "Tempo: 25:30:15")
   - `last_boss.txt` — Último chefe derrotado (ex.: "Última Morte: Margit (14:23:45)")
4. **Formatos Personalizados** — Defina seus próprios modelos de texto usando marcadores

### Funcionalidades Avançadas

- **Resetar Contador de Mortes**: Zere o contador de mortes do OBS sem afetar as estatísticas reais
- **Troca de Personagem**: Alterne entre saves de diferentes personagens
- **Atualizações Automáticas**: Verifique e instale novas versões automaticamente

---

## 🎮 Jogos Suportados

- **Elden Ring** (Jogo Base) ✅
- **Elden Ring: Sombra da Árvore do Érdtree** (DLC) ✅

---

## 💻 Requisitos do Sistema

- **SO**: Windows 10/11 (64-bit)
- **RAM**: 4 GB mínimo, 8 GB recomendado
- **Armazenamento**: 500 MB disponíveis
- **Adicional**: Instalação ativa do Elden Ring

---

## 🐛 Solução de Problemas

### Problemas Comuns

**O app não detecta o arquivo de save:**

- Certifique-se de que o Elden Ring está instalado e foi iniciado pelo menos uma vez
- Verifique o caminho do arquivo de save no Windows Explorer
- Tente executar o aplicativo como administrador

**O overlay não aparece:**

- Verifique se o overlay está ativado nas configurações
- Certifique-se de que o jogo está rodando em modo janela ou sem bordas
- Tente desativar e reativar o overlay

**Os arquivos do OBS não atualizam:**

- Verifique se o caminho da pasta de saída está correto
- Confirme que a geração de arquivos OBS está ativada
- Certifique-se de que os arquivos não estão sendo usados por outro aplicativo

**Problemas de desempenho:**

- Feche aplicativos desnecessários
- Desative o monitoramento em tempo real em hardware mais antigo

### Obtendo Ajuda

Se encontrar problemas não cobertos aqui:

1. Verifique as [issues existentes](https://github.com/felipesenpaidd/A-Cronica-do-Manchado/issues)
2. Crie uma [nova issue](https://github.com/felipesenpaidd/A-Cronica-do-Manchado/issues/new) com:
   - Descrição detalhada do problema
   - Especificações do seu sistema
   - Passos para reproduzir o problema
   - Qualquer mensagem de erro

---

## 🔄 Atualizações

### Atualizações Recentes

- **v1.0.6-ptbr** — Versão completamente traduzida para Português do Brasil; nomes de chefes e localizações conforme localização oficial Bandai Namco; caminhos de imagens corrigidos

### 🔮 Funcionalidades Planejadas

- **👥 Comparação com Amigos** — Compare suas estatísticas com amigos
- **⏱️ Rastreamento de Speedrun** — Cronometragem para tentativas de speedrun e recordes pessoais
- **📊 Estatísticas Avançadas** — Análises detalhadas dos seus padrões de gameplay
- **🏆 Placar Global** — Compare tempos de conclusão com a comunidade
- **🎯 Modos de Desafio** — Modos especiais para runs sem morte, SL1, etc.

---

## 🤝 Feedback e Relatórios de Bugs

**Feedback e relatórios de bugs são muito bem-vindos!**

### 🐛 Relatórios de Bugs

Encontrou um bug? Por favor, reporte:

1. **Verifique as [issues existentes](https://github.com/felipesenpaidd/A-Cronica-do-Manchado/issues)** para evitar duplicatas
2. **Crie uma [nova issue](https://github.com/felipesenpaidd/A-Cronica-do-Manchado/issues/new)** com:
   - Descrição detalhada do problema
   - Passos para reproduzir o problema
   - Especificações do seu sistema
   - Capturas de tela, se aplicável

### 💡 Sugestões de Funcionalidades

Tem uma ideia para uma nova funcionalidade? Crie uma [issue de sugestão](https://github.com/felipesenpaidd/A-Cronica-do-Manchado/issues/new) e descreva sua ideia.

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT — veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 🙏 Agradecimentos

- **FromSoftware** — Por criar a obra-prima que é Elden Ring
- **RysanekDavid** — Pelo projeto original [The Tarnished's Chronicle](https://github.com/RysanekDavid/The-Tarnished-Chronicle)
- **Bandai Namco** — Pela tradução oficial para Português do Brasil
- **Colaboradores da Comunidade** — Por feedback, relatórios de bugs e sugestões

---

<div align="center">

**Feito com ❤️ para a comunidade brasileira de Elden Ring**

[⬇️ Baixar Última Versão](https://github.com/felipesenpaidd/A-Cronica-do-Manchado/releases/latest) |
[🐛 Reportar Bug](https://github.com/felipesenpaidd/A-Cronica-do-Manchado/issues) |
[💡 Solicitar Recurso](https://github.com/felipesenpaidd/A-Cronica-do-Manchado/issues)

</div>
