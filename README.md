# Conversor de Vídeo Pro - Miranda Tech 🎥

Uma ferramenta de desktop moderna desenvolvida em Python para converter vídeos do formato MP4 para MOV (QuickTime). Esta versão conta com interface gráfica profissional, processamento em segundo plano e automação de nomenclatura.

## 🌟 Funcionalidades

- **Interface Moderna:** Botões arredondados e suporte a Dark Mode automático.
- **Automação de Nome:** Adiciona automaticamente o prefixo `CONVERTIDO_` ao arquivo original.
- **Seleção de Diretório:** O usuário escolhe apenas a pasta de destino; o programa cuida do nome do arquivo.
- **Barra de Progresso:** Feedback visual em tempo real durante a conversão.
- **Multi-threading:** A interface não trava (não fica "parada") enquanto o vídeo é processado.

## 🚀 Tecnologias Utilizadas

- [Python 3.13+](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (Interface Visual)
- [MoviePy v2.0+](https://zulko.github.io/moviepy/) (Motor de Conversão)
- [Threading](https://docs.python.org/3/library/threading.html) (Processamento Paralelo)

## 📋 Pré-requisitos

Para rodar este projeto, você precisará instalar as bibliotecas abaixo via terminal:

```bash
pip install moviepy customtkinter

🛠️ Como Usar
Execute o arquivo converter_video.py no seu VS Code.

Clique em "Selecionar Vídeo MP4" para escolher o arquivo de origem.

Clique em "Escolher Pasta de Destino" para definir onde o novo arquivo será salvo.

Escolha o formato de saída (atualmente .MOV).

Clique em "Converter Agora" e acompanhe a barra de progresso.

📂 Estrutura do Nome de Saída
O sistema segue a seguinte lógica:

Origem: video_projeto.mp4

Saída: CONVERTIDO_video_projeto.mov

Desenvolvido por Alex Miranda para automação de infraestrutura e gestão de ativos digitais.
