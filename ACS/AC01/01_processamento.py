import cv2

imagem = cv2.imread('entrada.png', cv2.IMREAD_GRAYSCALE)

if imagem is None:
    print("Erro: Arquivo 'entrada.jpg' não encontrado na pasta!")
    exit()

# - 100: limiar mínimo para conexão por histerese
# - 200: limiar máximo para bordas fortes definitivas
bordas = cv2.Canny(imagem, 100, 200)

cv2.imwrite('saida_canny.jpg', bordas)
print("Processamento concluído com sucesso! Arquivo 'saida_canny.jpg' gerado.")