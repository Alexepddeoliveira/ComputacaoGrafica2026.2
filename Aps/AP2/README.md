# AP2 — Peça Audiovisual: "Ibmec em 15 Segundos"

**Instituição:** Ibmec Barra da Tijuca / Rio  
**Disciplina:** Computação Gráfica (IBM0168/8001)  
**Aluno:** Alex Euzebio Pereira Dias de Oliveira (Alex Oliveira)  
**Data de Apresentação:** 18/11/2026 (Lab 212)  
**Ambiente de Desenvolvimento:** Blender 4.5 LTS  

---

## 1. Título, Conceito e Resumo da Sequência

* **Título:** *Conhecimento em Movimento: Da Engenharia à Consolidação Institucional*
* **Conceito:** A animação integra a narrativa iniciada na AP1, explorando a transição entre a escala micro-mecânica/tecnológica e a solidez arquitetônica da instituição. A narrativa demonstra a convergência entre inovação ativa e tradição acadêmica.
* **Resumo:** A sequência abre em plano detalhe com o núcleo tecnológico (`autoral_01`) iniciando seu ciclo físico por rolamento e queda gravitacional sobre a haste da letra "I". Simultaneamente, as letras "E" e "C" entram em rotação dinâmica convergindo para o centro, enquanto o bloco propulsor (`autoral_02`) executa uma manobra de sustentação e descida síncrona junto à letra "M" antes de se desacoplar. A peça encerra estabilizando na visão frontal clássica, apresentando a marca Ibmec e o edifício corporativo (`autoral_03`) plenamente integrados sob iluminação natural.

---

## 2. Descrição dos Momentos, Planos e Ações Animadas (Storyboard Atualizado)

| Momento / Plano | Frames (24 fps) | Tempo | Enquadramento | Ação Dramática dos Elementos |
| :--- | :--- | :--- | :--- | :--- |
| **Ato 1: O Despertar Dinâmico** | Frames 1 a 120 | 0.0s – 5.0s | *Close-up* lateral / Plano detalhe | O núcleo esférico (`autoral_01`) rola pela quina e cai com aceleração gravitacional sobre a haste do "I", assentando com quique mecânico seco (frame 91). |
| **Ato 2: Convergência e Sustentação** | Frames 121 a 240 | 5.0s – 10.0s | Movimento em arco | As letras "E" e "C" chegam rolando no eixo X da direita para a esquerda e travam em seus encaixes. O conjunto propulsor e a letra "M" realizam descida amortecida conjunta, separando-se no frame 233. |
| **Ato 3: A Consolidação Heroica** | Frames 241 a 360 | 10.0s – 15.0s | Plano Geral Frontal | A câmera desacelera (*ease-out*) e fixa o enquadramento institucional da AP1. A composição atinge o repouso com o logotipo Ibmec em evidência, os reflexos nos painéis de vidro e as texturas de concreto e metal. |

---

## 3. Propriedades Animadas e Decisões de Timing / Interpolação

* **Câmera:** Animação contínua nos canais de `Location` e `Rotation Euler`. As curvas no Graph Editor foram ajustadas com interpolação **Bézier**, com aceleração gradual de saída e desaceleração suave no ato final para assegurar conforto visual e leitura da marca.
* **Núcleo Esférico (`autoral_01`):** Translação e rotação física calculada proporcionalmente ao raio ($d\theta = ds / R$). Na curva de `Location Z`, as alças de aproximação ao solo foram tratadas com tangentes verticais acentuadas e impacto em **Vector**, transmitindo densidade e peso estrutural sem flutuação artificial.
* **Letras "E" e "C":** Translação em $X$ combinada com rotações no próprio eixo, desacelerando até a parada exata nos respectivos índices da marca.
* **Letra "M" e Propulsores (`autoral_02`):** Sincronização rigorosa de curvas no eixo vertical ($Z$) durante a descida para eliminar discrepâncias de interpolação (*sliding* / *double transform*), seguida pelo desacoplamento independente dos propulsores.

---

## 4. Configuração Geral de Iluminação e Renderização

* **Motor:** Blender EEVEE Next configurado com gerenciamento de cor **AgX (Look: Medium High Contrast)**.
* **Setup de Luzes:**
  * Luz Direcional Solar (*Sun Light*): Inclinada a $45^\circ$, responsável pelas sombras volumétricas rasantes que destacam o relevo do concreto.
  * Luz de Preenchimento (*Area Light* a 45 W): Posicionada para abrir penumbras, impedindo sombras totalmente negras nas faces não iluminadas.
  * Iluminação Global Procedural: Céu diurno atmosférico (*Hosek-Wilkie*).
* **Parâmetros de Renderização:** Resolução de 1920x1080 pixels (Full HD), 24 quadros por segundo constantes, totalizando 360 quadros renderizados.
* **Codec de Saída:** Contêiner MP4, codificação de vídeo H.264, taxa de compressão perceptual perceptually lossless (*CRF Medium*).

---

## 5. Materiais e Texturas da AC05 Reutilizados e Ajustados

* **`autoral_03_predio_ibmec` (`MAT_Concreto_PBR`):** Três mapas de textura conectados via nós `Texture Coordinate (UV)` e `Mapping` (fator de escala arquitetônica calibrado):
  * *Base Color*: Espaço de cor `sRGB`.
  * *Roughness*: Espaço de cor `Non-Color`.
  * *Normal Map*: Espaço de cor `Non-Color` intermediado pelo nó **Normal Map** em espaço tangente (`Strength = 0.25`).
* **`autoral_02_propulsores_do_negocio` (`MAT_Metal_Industrial_PBR`):** Metal PBR (`Metallic = 1.0`) com mapas de reflexão escovada e rugosidade em `Non-Color`.
* **`autoral_01_nucleo_energia`:** Preservado com metal condutor de alta reflexão especular (`Roughness = 0.05`), maquinário interno com engrenagens prateadas, buchas de cobre e cilindro central.
* **Pele de Vidro Modular (`MAT_Vidro_Arquitetonico`):** Superfície dielétrica com transmissão e rugosidade controlada simulando esquadrias e painéis corporativos.
* **Marca `Ibmec`:** Azul Institucional oficial (`#002F6C`) em acabamento acetinado (`Roughness = 0.35`) preservando a legibilidade e a identidade visual corporativa da instituição.

---

## 6. Desafios Encontrados e Soluções Adotadas

1. **Alteração na API de Curvas no Blender 4.5:** O novo sistema de *Slotted Actions* inviabilizou o acesso direto a `action.fcurves` em scripts legados. A manipulação das curvas foi adaptada diretamente no Graph Editor e através da nova estrutura de propriedades.
2. **Sincronização de Objetos em Queda:** O propulsor e a letra M desciam em taxas desiguais devido à divergência nas curvaturas das alças Bézier. O problema foi sanado transferindo e igualando a curva analítica de translação vertical entre ambos até o ponto exato da separação.
3. **Sensação de Peso na Queda Livre da Esfera:** A curva padrão de descida gerava desaceleração pré-impacto. As tangentes do frame de colisão foram ajustadas para o tipo *Vector*, conferindo aceleração gravitacional realista e choque contra o topo do "I".

---

## 7. Fontes e Licenças dos Recursos Externos

* **Texturas PBR (Concreto e Metal):** Obtidas nos repositórios públicos [ambientCG](https://ambientcg.com) e [Poly Haven](https://polyhaven.com).
* **Licenciamento:** *Creative Commons CC0 1.0 Universal Public Domain Dedication* (livre para estudos, modificação e uso acadêmico).
* **Empacotamento:** Todos os arquivos externos estão incorporados ao arquivo `.blend` por meio da rotina *Pack Resources*.