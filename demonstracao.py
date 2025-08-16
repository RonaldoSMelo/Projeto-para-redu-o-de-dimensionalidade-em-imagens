#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de demonstração para mostrar o processo de conversão
"""

from reducao_dimensionalidade import (
    rgb_to_grayscale, 
    grayscale_to_binary,
    process_image_color_to_grayscale,
    process_image_grayscale_to_binary
)

def demonstrar_conversao():
    """
    Demonstra o processo de conversão passo a passo
    """
    print("=== DEMONSTRAÇÃO DETALHADA DO PROCESSO ===\n")
    
    # Exemplo com cores básicas
    cores_exemplo = [
        (255, 0, 0),    # Vermelho
        (0, 255, 0),    # Verde
        (0, 0, 255),    # Azul
        (255, 255, 0),  # Amarelo
        (255, 0, 255),  # Magenta
        (0, 255, 255),  # Ciano
        (128, 128, 128), # Cinza médio
        (255, 255, 255), # Branco
        (0, 0, 0)       # Preto
    ]
    
    print("Conversão RGB -> Escala de Cinza -> Binária:")
    print("=" * 50)
    print(f"{'RGB':<15} {'Cinza':<8} {'Binário':<8}")
    print("-" * 50)
    
    for r, g, b in cores_exemplo:
        # Converter para escala de cinza
        cinza = rgb_to_grayscale(r, g, b)
        
        # Converter para binário
        binario = grayscale_to_binary(cinza)
        
        print(f"({r:3d},{g:3d},{b:3d}) -> {cinza:6d} -> {binario:6d}")
    
    print("\n" + "=" * 50)
    
    # Demonstrar com diferentes limiares
    print("\nEfeito de diferentes limiares na binarização:")
    print("=" * 60)
    
    cor_teste = (100, 150, 200)
    cinza_teste = rgb_to_grayscale(*cor_teste)
    
    print(f"Cor RGB: {cor_teste} -> Cinza: {cinza_teste}")
    print(f"{'Limiar':<8} {'Resultado':<10}")
    print("-" * 20)
    
    for limiar in [50, 100, 128, 150, 200]:
        resultado = grayscale_to_binary(cinza_teste, limiar)
        print(f"{limiar:6d} -> {resultado:8d}")

def demonstrar_processamento_imagem():
    """
    Demonstra o processamento de uma imagem completa
    """
    print("\n\n=== PROCESSAMENTO DE IMAGEM COMPLETA ===")
    
    # Criar uma imagem 3x3 simples
    imagem = [
        (255, 0, 0), (0, 255, 0), (0, 0, 255),
        (255, 255, 0), (128, 128, 128), (255, 255, 255),
        (0, 0, 0), (100, 150, 200), (200, 100, 50)
    ]
    
    width, height = 3, 3
    
    print(f"Imagem original: {width}x{height} pixels")
    print("Primeiros 6 pixels:")
    for i, (r, g, b) in enumerate(imagem[:6]):
        print(f"  Pixel {i}: RGB({r:3d},{g:3d},{b:3d})")
    
    # Converter para escala de cinza
    print("\nConvertendo para escala de cinza...")
    imagem_cinza = process_image_color_to_grayscale(imagem, width, height)
    
    print("Valores em escala de cinza:")
    for i, cinza in enumerate(imagem_cinza[:6]):
        print(f"  Pixel {i}: {cinza:3d}")
    
    # Converter para binária
    print("\nConvertendo para binária (limiar=128)...")
    imagem_binaria = process_image_grayscale_to_binary(imagem_cinza, threshold=128)
    
    print("Valores binários:")
    for i, binario in enumerate(imagem_binaria[:6]):
        print(f"  Pixel {i}: {binario:3d}")
    
    # Mostrar resumo estatístico
    print(f"\nResumo estatístico:")
    print(f"  Total de pixels: {len(imagem)}")
    print(f"  Pixels brancos (255): {imagem_binaria.count(255)}")
    print(f"  Pixels pretos (0): {imagem_binaria.count(0)}")

if __name__ == "__main__":
    demonstrar_conversao()
    demonstrar_processamento_imagem()
    
    print("\n" + "=" * 60)
    print("Demonstração concluída!")
    print("Execute 'python reducao_dimensionalidade.py' para gerar imagens")

