import tkinter as tk
from tkinter import filedialog, messagebox
import os
from logica import baixar_video_ou_audio


def baixar_video_ou_audio_com_interface():
    url = entry_url.get()
    formato = var_formato.get()
    pasta_destino = entry_destino.get()

    if not url:
        messagebox.showerror("Erro", "Por favor, insira a URL do vídeo.")
        return
    
    if not pasta_destino:
        messagebox.showerror("Erro", "Por favor, selecione a pasta de destino.")
        return

    try:
        sucesso = baixar_video_ou_audio(url, formato, pasta_destino)
        
        if sucesso:
            messagebox.showinfo("Sucesso", "Download concluído com sucesso!")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar: {e}")


def selecionar_pasta():
    pasta = filedialog.askdirectory(title="Selecione a pasta de destino")
    if pasta:
        entry_destino.delete(0, tk.END)
        entry_destino.insert(0, pasta)


root = tk.Tk()
root.title("Baixar Vídeos ou Áudios")
root.geometry("400x300")

# URL
label_url = tk.Label(root, text="URL do vídeo:")
label_url.pack(pady=5)
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

# Formato
label_formato = tk.Label(root, text="Escolha o formato:")
label_formato.pack(pady=5)

var_formato = tk.StringVar(value="mp4")
radio_mp4 = tk.Radiobutton(root, text="MP4", variable=var_formato, value="mp4")
radio_mp4.pack(pady=5)
radio_mp3 = tk.Radiobutton(root, text="MP3", variable=var_formato, value="mp3")
radio_mp3.pack(pady=5)

# Pasta de destino
label_destino = tk.Label(root, text="Pasta de destino:")
label_destino.pack(pady=5)
entry_destino = tk.Entry(root, width=50)
entry_destino.pack(pady=5)

botao_destino = tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta)
botao_destino.pack(pady=5)

# Botão de download
botao_download = tk.Button(root, text="Baixar", command=baixar_video_ou_audio_com_interface)
botao_download.pack(pady=20)

# Iniciar o loop da interface
root.mainloop()
