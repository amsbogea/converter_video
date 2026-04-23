from moviepy import VideoFileClip
import os

def converter_mp4_para_mov(arquivo_entrada, arquivo_saida):
    try:
        # Carregar o vídeo MP4
        print(f"Carregando o vídeo: {arquivo_entrada}")
        video = VideoFileClip(arquivo_entrada)
        
        # Salvar o vídeo no formato MOV
        # O codec 'libx264' é amplamente compatível para vídeos MOV
        video.write_videofile(arquivo_saida, codec='libx264')
        
        print(f"Conversão concluída: {arquivo_saida}")
    except Exception as e:
        print(f"Erro durante a conversão: {e}")
    finally:
        # Fechar o vídeo para liberar recursos
        if 'video' in locals():
            video.close()

# Exemplo de uso
input_file = r"C:\Users\alexsilva\Videos\Gravações de Tela\Gravação de Tela 2026-04-23 121012.mp4"  # Substitua pelo caminho do seu arquivo MP4
output_file = r"C:\Users\alexsilva\Videos\Gravações de Tela\CONVERTIDO_Gravação de Tela 2026-04-23 121012.mov"  # Substitua pelo caminho desejado para o arquivo MOV
converter_mp4_para_mov(input_file, output_file)