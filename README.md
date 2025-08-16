# Projeto para Redução de Dimensionalidade em Imagens

Este projeto implementa em Python puro (sem pacotes externos) algoritmos para transformar imagens coloridas em níveis de cinza e depois em imagens binárias (preto e branco).

## Funcionalidades

1. **Conversão RGB para Escala de Cinza**: Converte valores RGB para níveis de cinza usando a fórmula padrão Y = 0.299*R + 0.587*G + 0.114*B
2. **Binarização**: Converte imagens em escala de cinza para binárias (0 e 255) usando um limiar configurável
3. **Geração de Imagens**: Cria arquivos PGM (Portable Gray Map) para visualização

## Estrutura do Código

### Funções Principais

- `rgb_to_grayscale(r, g, b)`: Converte um pixel RGB para escala de cinza
- `grayscale_to_binary(grayscale_value, threshold)`: Converte um valor em escala de cinza para binário
- `process_image_color_to_grayscale(image_data, width, height)`: Processa uma imagem completa
- `process_image_grayscale_to_binary(grayscale_data, threshold)`: Binariza uma imagem em escala de cinza
- `create_simple_image(width, height, pixel_data, filename)`: Salva imagens no formato PGM

### Como Executar

```bash
python reducao_dimensionalidade.py
```

## Saída

O script gera:
- `imagem_cinza.pgm`: Imagem em níveis de cinza
- `imagem_binaria.pgm`: Imagem binária (preto e branco)

## Formato de Entrada para Imagens Reais

Para processar uma imagem real, crie um arquivo de texto com o formato:

```
largura altura
r1 g1 b1
r2 g2 b2
...
```

Onde cada linha contém os valores RGB de um pixel.

## Exemplo de Uso

```python
# Processar uma imagem real
process_real_image_from_file("minha_imagem.txt")
```

## Visualização

As imagens são salvas no formato PGM, que pode ser visualizado com:
- GIMP
- ImageMagick
- Visualizadores online de PGM
- Editores de imagem que suportam PGM

## Algoritmos Implementados

### Conversão para Escala de Cinza
Usa a fórmula padrão de luminância:
```
Y = 0.299 × R + 0.587 × G + 0.114 × B
```

### Binarização
Aplica um limiar (padrão: 128):
```
pixel_binario = 255 se pixel_cinza >= limiar, senão 0
```

## Requisitos

- Python 3.6+
- Apenas bibliotecas padrão do Python (math, struct)

## Autor

[Seu Nome]
Data: [Data Atual]
