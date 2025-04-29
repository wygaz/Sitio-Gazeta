
# atualizar_caminhos_imagens.py

# Caminho do arquivo HTML original
arquivo_original = 'index.html'
# Caminho do novo arquivo gerado
arquivo_novo = 'index_atualizado.html'

# Ler o conteúdo do index.html
with open(arquivo_original, 'r', encoding='utf-8') as f:
    conteudo = f.read()

# Substituir .png por .jpg
conteudo_atualizado = conteudo.replace('.png', '.jpg')

# Salvar o novo arquivo atualizado
with open(arquivo_novo, 'w', encoding='utf-8') as f:
    f.write(conteudo_atualizado)

print("✅ Arquivo atualizado criado como 'index_atualizado.html'!")
