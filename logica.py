import yt_dlp
import os


def baixar_video_ou_audio(url, formato, pasta_destino):
    if not url:
        raise ValueError("URL do vídeo é obrigatória.")
    
    if not pasta_destino:
        raise ValueError("A pasta de destino é obrigatória.")
    
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Melhor qualidade
            'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),  # Local e nome do arquivo
            'ffmpeg_location': r'C:\ffmpeg\bin\ffmpeg.exe',  # Caminho do FFmpeg
        }

        if formato == 'mp3':
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegAudioConvertor',
                'preferredformat': 'mp3',  # Conversão para MP3
            }]
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        return True
    
    except Exception as e:
        raise Exception(f"Erro ao baixar: {e}")
