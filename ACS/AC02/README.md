# AC02: Transformações Geométricas 2D com Matplotlib

Este trabalho apresenta a fundamentação teórica, a resolução analítica e a implementação computacional das principais transformações geométricas bidimensionais (Translação, Escala, Rotação, Reflexão, Cisalhamento e Composição de Matrizes), validadas graficamente com a biblioteca Matplotlib.

---

### Exercício 1: Translação Simples

* **Enunciado:** Dado o ponto $P(2, 3)$, aplique a translação com vetor $(4, -2)$.
* **Cálculo Analítico:**
  * $x' = x + t_x = 2 + 4 = 6$
  * $y' = y + t_y = 3 + (-2) = 1$
* **Respostas:**
  * Nova posição: $P'(6, 1)$
  * Coordenadas alteradas: Ambas as coordenadas ($x$ e $y$) sofreram alteração.

![Exercício 1](graficos/ex01.png)

---

### Exercício 2: Escala Uniforme

* **Enunciado:** Triângulo com vértices $A(1, 1)$, $B(3, 1)$ e $C(2, 4)$. Aplique escala uniforme com fator $s = 2$.
* **Cálculo Analítico ($x' = 2x, y' = 2y$):**
  * $A'(1 \cdot 2, 1 \cdot 2) = A'(2, 2)$
  * $B'(3 \cdot 2, 1 \cdot 2) = B'(6, 2)$
  * $C'(2 \cdot 2, 4 \cdot 2) = C'(4, 8)$
* **Respostas:**
  * Novas coordenadas: $A'(2, 2)$, $B'(6, 2)$ e $C'(4, 8)$.
  * Efeito geométrico: O comprimento das arestas dobra e a área total da figura quadruplica ($2^2 = 4\times$), preservando a proporção angular original.

![Exercício 2](graficos/ex02.png)

---

### Exercício 3: Escala Não Uniforme

* **Enunciado:** Aplicar escala não uniforme ao triângulo do Exercício 2, com $s_x = 2$ e $s_y = 0.5$.
* **Cálculo Analítico ($x' = 2x, y' = 0.5y$):**
  * $A'(1 \cdot 2, 1 \cdot 0.5) = A'(2, 0.5)$
  * $B'(3 \cdot 2, 1 \cdot 0.5) = B'(6, 0.5)$
  * $C'(2 \cdot 2, 4 \cdot 0.5) = C'(4, 2)$
* **Resposta:**
  * Novas coordenadas: $A'(2, 0.5)$, $B'(6, 0.5)$ e $C'(4, 2)$. A figura sofre distorção anisotrópica (expansão na base e compressão na altura).

![Exercício 3](graficos/ex03.png)

---

### Exercício 4: Rotação em Torno da Origem

* **Enunciado:** Rotacionar o ponto $P(1, 0)$ em $90^\circ$ no sentido anti-horário em torno da origem.
* **Cálculo Analítico ($\theta = 90^\circ, \cos(90^\circ) = 0, \sin(90^\circ) = 1$):**
  * $x' = x\cos(\theta) - y\sin(\theta) = 1(0) - 0(1) = 0$
  * $y' = x\sin(\theta) + y\cos(\theta) = 1(1) + 0(0) = 1$
* **Resposta:**
  * Nova posição: $P'(0, 1)$.

![Exercício 4](graficos/ex04.png)

---

### Exercício 5: Rotação de um Polígono

* **Enunciado:** Quadrado com vértices $A(1, 1)$, $B(1, 4)$, $C(4, 4)$, $D(4, 1)$. Aplicar rotação de $45^\circ$ no sentido horário ($\theta = -45^\circ$).
* **Cálculo Analítico ($\cos(-45^\circ) \approx 0.7071, \sin(-45^\circ) \approx -0.7071$):**
  * $x' \approx 0.7071(x + y)$
  * $y' \approx 0.7071(y - x)$
  * $A': x' = 0.7071(2) \approx 1.414, \quad y' = 0.7071(0) = 0 \implies A'(1.414, 0)$
  * $B': x' = 0.7071(5) \approx 3.536, \quad y' = 0.7071(3) \approx 2.121 \implies B'(3.536, 2.121)$
  * $C': x' = 0.7071(8) \approx 5.657, \quad y' = 0.7071(0) = 0 \implies C'(5.657, 0)$
  * $D': x' = 0.7071(5) \approx 3.536, \quad y' = 0.7071(-3) \approx -2.121 \implies D'(3.536, -2.121)$
* **Resposta:**
  * Vértices rotacionados: $A'(1.414, 0)$, $B'(3.536, 2.121)$, $C'(5.657, 0)$ e $D'(3.536, -2.121)$.

![Exercício 5](graficos/ex05.png)

---

### Exercício 6: Reflexão Simples

* **Enunciado:** Dado o ponto $P(2, 5)$, aplicar reflexão em relação ao eixo $y$.
* **Cálculo Analítico ($x' = -x, y' = y$):**
  * $x' = -2$
  * $y' = 5$
* **Resposta:**
  * Nova posição: $P'(-2, 5)$.

![Exercício 6](graficos/ex06.png)

---

### Exercício 7: Reflexão de um Triângulo

* **Enunciado:** Triângulo com vértices $A(2, 3)$, $B(4, 3)$ e $C(3, 5)$. Aplicar reflexão em relação ao eixo $x$.
* **Cálculo Analítico ($x' = x, y' = -y$):**
  * $A'(2, -3)$
  * $B'(4, -3)$
  * $C'(3, -5)$
* **Resposta:**
  * Novas coordenadas: $A'(2, -3)$, $B'(4, -3)$ e $C'(3, -5)$.

![Exercício 7](graficos/ex07.png)

---

### Exercício 8: Cisalhamento Horizontal

* **Enunciado:** Dado o ponto $P(2, 3)$, aplicar cisalhamento horizontal com fator $k = 2$.
* **Cálculo Analítico ($x' = x + k \cdot y, y' = y$):**
  * $x' = 2 + (2 \cdot 3) = 2 + 6 = 8$
  * $y' = 3$
* **Resposta:**
  * Nova posição: $P'(8, 3)$.

![Exercício 8](graficos/ex08.png)

---

### Exercício 9: Composição de Transformações

* **Enunciado:** Dado o ponto $P(3, 2)$, aplicar sequencialmente:
  1. Translação com vetor $(1, -1)$.
  2. Rotação de $90^\circ$ anti-horário.
  3. Escala uniforme com fator $2$.
* **Cálculo Analítico Passo a Passo:**
  * **Passo 1 (Translação):** $P_1(3 + 1, 2 - 1) = P_1(4, 1)$
  * **Passo 2 (Rotação $90^\circ$):** $x_2 = -y_1 = -1, \quad y_2 = x_1 = 4 \implies P_2(-1, 4)$
  * **Passo 3 (Escala $\times 2$):** $x_3 = -1 \cdot 2 = -2, \quad y_3 = 4 \cdot 2 = 8 \implies P_3(-2, 8)$
* **Resposta:**
  * Posição final após a composição: $P'(-2, 8)$.

![Exercício 9](graficos/ex09.png)

---

### Exercício 10: Combinação de Transformações em uma Figura

* **Enunciado:** Retângulo com vértices $A(1, 1)$, $B(5, 1)$, $C(5, 3)$, $D(1, 3)$. Aplicar:
  1. Translação com vetor $(-2, 3)$.
  2. Escala não uniforme ($s_x = 1.5, s_y = 0.5$).
  3. Reflexão em relação ao eixo $y$.
* **Cálculo Analítico:**
  * **Etapa 1 (Translação: $x + (-2), y + 3$):**  
    * $A_1(-1, 4), \quad B_1(3, 4), \quad C_1(3, 6), \quad D_1(-1, 6)$
  * **Etapa 2 (Escala: $1.5x, 0.5y$):**  
    * $A_2(-1.5, 2.0), \quad B_2(4.5, 2.0), \quad C_2(4.5, 3.0), \quad D_2(-1.5, 3.0)$
  * **Etapa 3 (Reflexão em Y: $-x, y$):**  
    * $A'(1.5, 2.0), \quad B'(-4.5, 2.0), \quad C'(-4.5, 3.0), \quad D'(1.5, 3.0)$
* **Resposta:**
  * Vértices finais: $A'(1.5, 2.0)$, $B'(-4.5, 2.0)$, $C'(-4.5, 3.0)$ e $D'(1.5, 3.0)$.

![Exercício 10](graficos/ex10.png)