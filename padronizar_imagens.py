from PIL import Image, ImageOps
import os

# Caminho das imagens originais
origem = "imagens"
destino = "imagens/ajustadas"
tamanho_alvo = (1200, 800)

# Cria pasta destino se não existir
os.makedirs(destino, exist_ok=True)

# Processa cada imagem
for nome_arquivo in os.listdir(origem):
    if nome_arquivo.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        caminho_img = os.path.join(origem, nome_arquivo)
        img = Image.open(caminho_img).convert("RGB")

        # Redimensiona mantendo proporção e insere em fundo branco
        img_thumb = ImageOps.fit(img, tamanho_alvo, method=Image.LANCZOS, centering=(0.5, 0.5))
        fundo = Image.new("RGB", tamanho_alvo, (255, 255, 255))
        fundo.paste(img_thumb, (0, 0))

        # Salva a imagem ajustada
        caminho_saida = os.path.join(destino, nome_arquivo)
        fundo.save(caminho_saida, quality=90)

        print(f"Imagem processada: {nome_arquivo}")
