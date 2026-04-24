import customtkinter as ctk
from tkinter import filedialog, messagebox
from moviepy import VideoFileClip
import os
import threading

# Configuração visual do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Conversor Pro - Miranda Tech")
        self.geometry("500x450")

        # Variáveis
        self.caminho_origem = ""
        self.diretorio_destino = ""

        # UI - Título
        self.label_titulo = ctk.CTkLabel(self, text="Conversor MP4 para MOV", font=("Arial", 20, "bold"))
        self.label_titulo.pack(pady=20)

        # Seleção de Origem
        self.btn_origem = ctk.CTkButton(self, text="Selecionar Vídeo MP4", corner_radius=20, command=self.selecionar_origem)
        self.btn_origem.pack(pady=10)
        self.lbl_origem = ctk.CTkLabel(self, text="Nenhum arquivo selecionado", wraplength=400)
        self.lbl_origem.pack(pady=5)

        # Seleção de Destino (Pasta)
        self.btn_destino = ctk.CTkButton(self, text="Escolher Pasta de Destino", corner_radius=20, command=self.selecionar_destino, fg_color="transparent", border_width=2)
        self.btn_destino.pack(pady=10)
        self.lbl_destino = ctk.CTkLabel(self, text="Nenhuma pasta selecionada", wraplength=400)
        self.lbl_destino.pack(pady=5)

        # Formato (Apenas visual conforme solicitado)
        self.label_fmt = ctk.CTkLabel(self, text="Formato de Saída:")
        self.label_fmt.pack(pady=(10,0))
        self.combo = ctk.CTkComboBox(self, values=[".MOV (QuickTime)"], corner_radius=15)
        self.combo.pack(pady=5)

        # Barra de Progresso (Indeterminada para conversão)
        self.progress = ctk.CTkProgressBar(self, orientation="horizontal", corner_radius=10)
        self.progress.set(0)
        self.progress.pack(pady=20, padx=20, fill="x")

        # Botão Principal
        self.btn_converter = ctk.CTkButton(self, text="Converter Agora", corner_radius=20, command=self.iniciar_thread, fg_color="#2ecc71", hover_color="#27ae60")
        self.btn_converter.pack(pady=20)

    def selecionar_origem(self):
        caminho = filedialog.askopenfilename(filetypes=[("Vídeo MP4", "*.mp4")])
        if caminho:
            self.caminho_origem = caminho
            self.lbl_origem.configure(text=os.path.basename(caminho))

    def selecionar_destino(self):
        pasta = filedialog.askdirectory()
        if pasta:
            self.diretorio_destino = pasta
            self.lbl_destino.configure(text=pasta)

    def iniciar_thread(self):
        # Usamos Thread para a interface não travar durante a conversão
        thread = threading.Thread(target=self.converter)
        thread.start()

    def converter(self):
        if not self.caminho_origem or not self.diretorio_destino:
            messagebox.showwarning("Atenção", "Selecione o arquivo e a pasta de destino!")
            return

        try:
            self.btn_converter.configure(state="disabled", text="Processando...")
            self.progress.start() # Faz a barra de progresso "correr"

            # Lógica do nome do arquivo
            nome_original = os.path.basename(self.caminho_origem)
            nome_sem_ext = os.path.splitext(nome_original)[0]
            nome_final = f"CONVERTIDO_{nome_sem_ext}.mov"
            caminho_final = os.path.join(self.diretorio_destino, nome_final)

            with VideoFileClip(self.caminho_origem) as video:
                video.write_videofile(caminho_final, codec="libx264", audio_codec="aac")

            self.progress.stop()
            self.progress.set(1)
            messagebox.showinfo("Sucesso", f"Salvo como:\n{nome_final}")
        
        except Exception as e:
            messagebox.showerror("Erro", f"Falha: {e}")
        finally:
            self.btn_converter.configure(state="normal", text="Converter Agora")
            self.progress.set(0)

if __name__ == "__main__":
    app = App()
    app.mainloop()