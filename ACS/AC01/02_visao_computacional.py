import cv2

imagem = cv2.imread('rosto_entrada.png')

if imagem is None:
    print("Erro: Arquivo 'rosto_entrada.jpg' não foi encontrado na pasta!")
    exit()

cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

caminho_modelo = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
detector_faces = cv2.CascadeClassifier(caminho_modelo)


faces = detector_faces.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

print(f"Total de faces detectadas: {len(faces)}")
print("Coordenadas obtidas [x, y, largura, altura]:")
print(faces)


for (x, y, w, h) in faces:
    # Parâmetros: imagem, ponto_inicial, ponto_final, cor (BGR), espessura_da_linha
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imwrite('saida_deteccao_rosto.jpg', imagem)
print("Sucesso: Imagem 'saida_deteccao_rosto.jpg' gerada com as detecções!")