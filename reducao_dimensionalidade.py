#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projeto para redução de dimensionalidade em imagens
Implementação em Python para transformar uma imagem colorida para:
1. Níveis de cinza (0 a 255)
2. Binarizada (0 e 255) - preto e branco

Autor: [Seu Nome]
Data: [Data Atual]
"""

import math
import struct

def rgb_to_grayscale(r, g, b):
    """
    Converte valores RGB para escala de cinza usando a fórmula padrão
    Y = 0.299*R + 0.587*G + 0.114*B
    
    Args:
        r (int): Valor vermelho (0-255)
        g (int): Valor verde (0-255)
        b (int): Valor azul (0-255)
    
    Returns:
        int: Valor em escala de cinza (0-255)
    """
    return int(0.299 * r + 0.587 * g + 0.114 * b)

def grayscale_to_binary(grayscale_value, threshold=128):
    """
    Converte um valor em escala de cinza para binário
    
    Args:
        grayscale_value (int): Valor em escala de cinza (0-255)
        threshold (int): Limiar para binarização (padrão: 128)
    
    Returns:
        int: Valor binário (0 ou 255)
    """
    return 255 if grayscale_value >= threshold else 0

def process_image_color_to_grayscale(image_data, width, height):
    """
    Converte uma imagem colorida para níveis de cinza
    
    Args:
        image_data (list): Lista de pixels RGB [(r,g,b), (r,g,b), ...]
        width (int): Largura da imagem
        height (int): Altura da imagem
    
    Returns:
        list: Lista de valores em escala de cinza
    """
    grayscale_data = []
    
    for pixel in image_data:
        r, g, b = pixel
        gray_value = rgb_to_grayscale(r, g, b)
        grayscale_data.append(gray_value)
    
    return grayscale_data

def process_image_grayscale_to_binary(grayscale_data, threshold=128):
    """
    Converte uma imagem em escala de cinza para binária
    
    Args:
        grayscale_data (list): Lista de valores em escala de cinza
        threshold (int): Limiar para binarização
    
    Returns:
        list: Lista de valores binários (0 ou 255)
    """
    binary_data = []
    
    for gray_value in grayscale_data:
        binary_value = grayscale_to_binary(gray_value, threshold)
        binary_data.append(binary_value)
    
    return binary_data

def create_simple_image(width, height, pixel_data, filename, image_type="P5"):
    """
    Cria uma imagem PGM simples (formato binário)
    
    Args:
        width (int): Largura da imagem
        height (int): Altura da imagem
        pixel_data (list): Dados dos pixels
        filename (str): Nome do arquivo de saída
        image_type (str): Tipo da imagem (P5 para binário)
    """
    with open(filename, 'wb') as f:
        # Cabeçalho PGM
        header = f"{image_type}\n{width} {height}\n255\n"
        f.write(header.encode('ascii'))
        
        # Dados dos pixels
        for pixel in pixel_data:
            f.write(struct.pack('B', pixel))

def create_color_image_example():
    """
    Cria uma imagem de exemplo simples para demonstração
    Retorna dados de uma imagem 8x8 com cores básicas
    """
    # Criar uma imagem 8x8 com cores básicas para demonstração
    width, height = 8, 8
    image_data = []
    
    # Padrão de cores simples
    colors = [
        (255, 0, 0),    # Vermelho
        (0, 255, 0),    # Verde
        (0, 0, 255),    # Azul
        (255, 255, 0),  # Amarelo
        (255, 0, 255),  # Magenta
        (0, 255, 255),  # Ciano
        (128, 128, 128), # Cinza médio
        (255, 255, 255)  # Branco
    ]
    
    for y in range(height):
        for x in range(width):
            color_index = (x + y) % len(colors)
            image_data.append(colors[color_index])
    
    return image_data, width, height

def main():
    """
    Função principal que demonstra o processo completo
    """
    print("=== Projeto para Redução de Dimensionalidade em Imagens ===")
    print("Implementação em Python sem pacotes externos\n")
    
    # Criar imagem de exemplo
    print("1. Criando imagem de exemplo 8x8...")
    image_data, width, height = create_color_image_example()
    print(f"   Imagem criada: {width}x{height} pixels")
    
    # Converter para níveis de cinza
    print("\n2. Convertendo para níveis de cinza...")
    grayscale_data = process_image_color_to_grayscale(image_data, width, height)
    print(f"   Conversão concluída: {len(grayscale_data)} pixels processados")
    
    # Converter para binária
    print("\n3. Convertendo para imagem binária...")
    binary_data = process_image_grayscale_to_binary(grayscale_data, threshold=128)
    print(f"   Binarização concluída: {len(binary_data)} pixels processados")
    
    # Salvar imagens
    print("\n4. Salvando imagens...")
    
    # Salvar imagem em níveis de cinza
    create_simple_image(width, height, grayscale_data, "imagem_cinza.pgm")
    print("   Imagem em níveis de cinza salva como 'imagem_cinza.pgm'")
    
    # Salvar imagem binária
    create_simple_image(width, height, binary_data, "imagem_binaria.pgm")
    print("   Imagem binária salva como 'imagem_binaria.pgm'")
    
    # Mostrar alguns exemplos de conversão
    print("\n5. Exemplos de conversão:")
    print("   RGB -> Cinza -> Binário")
    for i in range(min(5, len(image_data))):
        r, g, b = image_data[i]
        gray = grayscale_data[i]
        binary = binary_data[i]
        print(f"   ({r:3d},{g:3d},{b:3d}) -> {gray:3d} -> {binary:3d}")
    
    print("\n=== Processo concluído com sucesso! ===")
    print("Arquivos gerados:")
    print("- imagem_cinza.pgm (níveis de cinza)")
    print("- imagem_binaria.pgm (binária)")
    print("\nPara visualizar as imagens, use um visualizador de imagens PGM")

def process_real_image_from_file(filename):
    """
    Processa uma imagem real a partir de um arquivo (formato simples)
    Esta função assume um formato de arquivo simples com valores RGB
    
    Args:
        filename (str): Nome do arquivo de entrada
    """
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            
        # Primeira linha deve conter width height
        width, height = map(int, lines[0].strip().split())
        
        # Linhas seguintes contêm valores RGB
        image_data = []
        for line in lines[1:]:
            if line.strip():
                r, g, b = map(int, line.strip().split())
                image_data.append((r, g, b))
        
        print(f"Imagem carregada: {width}x{height} pixels")
        
        # Processar a imagem
        grayscale_data = process_image_color_to_grayscale(image_data, width, height)
        binary_data = process_image_grayscale_to_binary(grayscale_data)
        
        # Salvar resultados
        create_simple_image(width, height, grayscale_data, f"{filename}_cinza.pgm")
        create_simple_image(width, height, binary_data, f"{filename}_binaria.pgm")
        
        print(f"Resultados salvos para {filename}_cinza.pgm e {filename}_binaria.pgm")
        
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado")
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")

if __name__ == "__main__":
    # Executar demonstração principal
    main()
    
    # Exemplo de como processar uma imagem real (descomente se tiver um arquivo)
    # process_real_image_from_file("minha_imagem.txt")
