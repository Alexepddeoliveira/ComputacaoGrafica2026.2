## 1. Processamento de Imagens

### Aplicação: Detecção de Bordas com Algoritmo de Canny (OpenCV)

O Processamento de Imagens tem como foco a manipulação e transformação de dados visuais, operando no modelo onde a **entrada é uma imagem digital** e a **saída é outra imagem modificada**. 

O Filtro de Canny aplica esse princípio para realçar bordas através de quatro etapas sequenciais:

* **1. Suavização Gaussiana (Redução de Ruído):**  
  Câmeras e sensores digitais geram variações aleatórias de brilho (ruídos de alta frequência). O cálculo de derivadas diretamente sobre a imagem bruta interpretaria cada grão de ruído como uma borda falsa. A convolução com um filtro gaussiano borra levemente a imagem para atenuar essas imperfeições antes da análise.

* **2. Cálculo do Gradiente (Magnitude e Direção):**  
  O algoritmo aplica operadores diferenciais (filtros de Sobel) nos eixos horizontal ($G_x$) e vertical ($G_y$). Isso quantifica a taxa de variação de intensidade luminosa entre pixels vizinhos. Regiões com transições abruptas de cor geram magnitudes de gradiente elevadas, apontando candidatos a contorno.

* **3. Supressão de Não-Máximos (Afinamento das Linhas):**  
  O mapa de gradientes inicial produz contornos espessos e difusos. O algoritmo percorre a matriz na direção ortogonal à borda e verifica se o pixel atual corresponde ao pico local de intensidade. Caso contrário, o valor é suprimido (zerado), reduzindo o contorno à espessura de 1 único pixel.

* **4. Limiarização por Histerese (Filtro de Decisão Final):**  
  São aplicados dois limiares de corte (`minVal = 100` e `maxVal = 200`):
  * **Acima de 200:** Pixels classificados como bordas definitivas e consolidadas.
  * **Abaixo de 100:** Pixels descartados sumariamente como ruído de fundo.
  * **Entre 100 e 200:** Pixels aceitos apenas se possuírem continuidade espacial com uma borda forte já validada.

---

### Demonstração Prática

| Imagem de Entrada | Imagem de Saída (Canny) |
| :---: | :---: |
| ![Entrada](entrada.png) | ![Saída Canny](saida_canny.jpg) |
| *Matriz original em escala de cinza* | *Bordas binárias detectadas* |