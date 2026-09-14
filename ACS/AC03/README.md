# AC03: Transformações Geométricas 2D e 3D no Blender 4.5 LTS

## 1. Descrição da Atividade e Transformações Aplicadas

Nesta atividade prática foi desenvolvida a cena tridimensional **"Parque Geométrico"**, integrando primitivas bidimensionais no plano cartesiano XY e sólidos no espaço afim 3D. 

* **Transformações 2D (Plano XY):** Foram aplicadas operações de translação linear de coordenadas, rotação pura em torno do eixo $Z$ e escala anisotrópica nos eixos $X$ e $Y$ sobre as primitivas planas (`obj2d_quadrado`, `obj2d_triangulo` e `obj2d_circulo`).
* **Transformações 3D (Espaço Tridimensional):** Sobre os sólidos (`obj3d_cubo`, `obj3d_cilindro` e `obj3d_esfera`), foram executadas translações no eixo vertical $Z$, rotações combinadas em múltiplos eixos (ângulos de Euler) e escalas diferenciais nos eixos $X$, $Y$ e $Z$.
* **Automação vs. Manual:** A hierarquia de coleções, inserção paramétrica das primitivas, conversão trigonométrica de rotações e interpolação temporal de keyframes (quadros 1 a 120) foram automatizadas via Python (`bpy`). O enquadramento focal da câmera e inspeção dos canais de iluminação receberam ajustes finos via interface gráfica do Blender.

---

## 2. Renderização da Cena Final

| Render da Cena: Parque Geométrico |
| :---: |
| ![Render Final](AC03_AlexOliveira.png) |
| *Composição espacial contendo elementos 2D (plano XY) e sólidos 3D transformados* |

---

## 3. Respostas das Questões Teóricas

* **1. Diferença entre translação, rotação e escala em computação gráfica:**  
  * *Translação:* Operação afim aditiva que desloca a posição dos vértices no espaço por meio da soma de um vetor $(t_x, t_y, t_z)$, alterando a localização sem modificar orientação ou dimensões.
  * *Rotação:* Operação linear multiplicativa que gira o objeto em torno de um eixo ou centro geométrico por um ângulo $\theta$, modificando sua orientação espacial sem alterar proporções métricas ou distâncias relativas entre vértices.
  * *Escala:* Operação multiplicativa que altera as dimensões e volume do objeto através de fatores de multiplicação $(s_x, s_y, s_z)$, podendo ser uniforme (preserva a forma) ou não-uniforme (provoca deformação anisotrópica).

* **2. Diferença entre transformar um objeto no espaço local e no espaço global:**  
  * *Espaço Global (World Space):* É o sistema de coordenadas universal e fixo da cena. Qualquer rotação ou translação toma como base a origem $(0, 0, 0)$ e os eixos absolutos do mundo.
  * *Espaço Local (Object Space):* É o sistema de eixos próprio do objeto, centrado no seu ponto de pivô (*origin*). Se um objeto é rotacionado, os seus eixos locais giram juntos; assim, mover o objeto no eixo $X$ local resultará em uma trajetória inclinada em relação ao mundo global.

* **3. Por que rotações em eixos diferentes podem gerar resultados visuais distintos em uma cena 3D?**  
  A rotação em três dimensões é uma operação **não-comutativa**. Matematicamente, a multiplicação de matrizes de rotação depende da ordem de aplicação ($R_x \cdot R_y \neq R_y \cdot R_x$). Rotacionar um corpo primeiro no eixo $X$ e depois no $Y$ produz uma orientação final completamente diferente de aplicar primeiro $Y$ e depois $X$, fenômeno frequentemente associado à convenção de ângulos de Euler e ao risco de travamento de cardan (*gimbal lock*).

* **4. No Blender, por que usar `math.radians()` ao definir `rotation_euler` por script?**  
  A interface gráfica do Blender exibe ângulos em **graus sexagesimais** ($0^\circ$ a $360^\circ$) por convenção humana, mas o motor interno de computação gráfica e a API Python (`bpy`) operam exclusivamente em **radianos** ($0$ a $2\pi$) para simplificar os cálculos trigonométricos nas funções seno e cosseno das matrizes de transformação. A função `math.radians()` faz a conversão direta de escala ($\text{rad} = \text{graus} \cdot \frac{\pi}{180}$).

* **5. Exemplo prático de quando vale mais a pena usar Python em vez de transformar manualmente:**  
  Automação procedimental e operações repetitivas em larga escala. Por exemplo: criar uma floresta com 2.000 árvores onde cada uma precisa de pequenas variações aleatórias de escala e rotação no chão, ou gerar uma escada em caracol de 100 degraus onde cada degrau precisa ser transladado no eixo $Z$ e rotacionado em $15^\circ$ em relação ao anterior. Fazer isso manualmente pela interface seria lento e propenso a erros humanos; via script, resolve-se com um laço `for` de poucas linhas em fração de segundo.