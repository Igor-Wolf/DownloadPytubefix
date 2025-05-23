from pytubefix import YouTube
from pytubefix.cli import on_progress
import sys
import io
import os
import re
import unicodedata

# Força a saída UTF-8 (resolve problemas de encoding no Windows)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Cria a pasta 'downloads' se não existir
os.makedirs('downloads', exist_ok=True)

# Função para limpar nomes de arquivos
def sanitize_filename(name):
    # Remove acentos
    name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
    # Remove caracteres inválidos para nomes de arquivos no Windows
    name = re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', name)
    # Remove emojis e símbolos fora do padrão ASCII
    name = re.sub(r'[^\x00-\x7F]', '', name)
    # Substitui múltiplos espaços por um só e remove espaços das pontas
    name = re.sub(r'\s+', ' ', name).strip()
    return name

# Abrir o arquivo de URLs
with open('urls.txt', 'r', encoding='utf-8') as file:
    urls = file.readlines()

# Loop para baixar cada vídeo
for url in urls:
    url = url.strip()
    if url:
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            safe_title = sanitize_filename(yt.title)
            filename = f"{safe_title}.mp4"

            print(f"\n🔽 Baixando: {yt.title}")
            yt.streams.get_highest_resolution().download(output_path='downloads', filename=filename)
            print(f"✅ Download concluído: {filename}")
        except Exception as e:
            print(f"❌ Erro ao baixar {url}: {e}")

print("\n📥 Todos os downloads foram concluídos.")
