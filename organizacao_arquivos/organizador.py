import os
import shutil

# Caminho da pasta que deseja organizar
pasta_origem = os.path.expanduser('~/Downloads')

# Dicionário de extensões e pastas de destino
pastas_destino = {
    'Documentos': ['.pdf', '.docx', '.doc', '.odt', '.xlsx', '.txt'],
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Vídeos': ['.mp4', '.mov', '.avi'],
    'Aúdio': ['.mp3'],
    'Compactados': ['.zip', '.rar', '.7z'],
    'Torrents': ['.torrent'],
    'Aplicativos': ['.exe', '.msi'],
    'Arquivos APK': ['.apk'],
    'Arquivos XML': ['.xml'],
    'Arquivos HTML': ['.webp'],
    'Arquivos SVG': ['.svg'],
    'Outros': []
}

# Criar as pastas de destino se não existirem
for pasta in pastas_destino.keys():
    caminho = os.path.join(pasta_origem, pasta)
    os.makedirs(caminho, exist_ok=True)

# Percorrer os arquivos na pasta
for arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, arquivo)
    
    # Ignorar se for pasta
    if os.path.isdir(caminho_arquivo):
        continue

    # Pegar extensão do arquivo
    _, extensao = os.path.splitext(arquivo)
    extensao = extensao.lower()

    # Definir a pasta de destino
    movido = False
    for pasta, extensoes in pastas_destino.items():
        if extensao in extensoes:
            destino = os.path.join(pasta_origem, pasta, arquivo)
            shutil.move(caminho_arquivo, destino)
            print(f'Movido: {arquivo} → {pasta}')
            movido = True
            break

    # Se não encontrar a extensão, mandar para "Outros"
    if not movido:
        destino = os.path.join(pasta_origem, 'Outros', arquivo)
        shutil.move(caminho_arquivo, destino)
        print(f'Movido: {arquivo} → Outros')

print('Organização concluída!')
