from pytubefix import YouTube

# Abrir o arquivo de URLs
with open('urls.txt', 'r') as file:
    urls = file.readlines()

# Loop para baixar cada vídeo
for url in urls:
    url = url.strip()  # Remove espaços em branco
    if url:  # Verifica se a linha não está vazia
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            print(f"Baixando: {yt.title}")
            stream.download(output_path='downloads')
            print(f"Download concluído: {yt.title}")
        except Exception as e:
            print(f"Erro ao baixar {url}: {e}")

print("Todos os downloads foram concluídos.")
