import os
import subprocess

# Defina o caminho da pasta de downloads
download_path = 'downloads'

# Função para converter MP4 para MP3
def convert_mp4_to_mp3(file_path):
    base, _ = os.path.splitext(file_path)
    mp3_file = base + '.mp3'
    
    # Comando ffmpeg para converter MP4 para MP3
    command = [
        'ffmpeg', '-i', file_path,
        '-vn', '-ab', '192k', '-ar', '44100',
        '-f', 'mp3', mp3_file
    ]
    
    # Executa o comando
    subprocess.run(command, check=True)
    return mp3_file

# Verificar todos os arquivos na pasta
for file_name in os.listdir(download_path):
    if file_name.endswith('.mp4'):
        file_path = os.path.join(download_path, file_name)
        print(f"Convertendo {file_name} para MP3...")
        
        try:
            mp3_file = convert_mp4_to_mp3(file_path)
            print(f"Arquivo convertido: {mp3_file}")
            
            # Remove o arquivo MP4 original
            os.remove(file_path)
            print(f"Arquivo original removido: {file_path}")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao converter {file_name}: {e}")

print("Conversão e limpeza concluídas.")
