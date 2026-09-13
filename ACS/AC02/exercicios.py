import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("graficos", exist_ok=True)

def salvar_poligono(orig, trans, titulo, nome_arquivo):
    plt.figure(figsize=(6, 6))
    plt.plot(*zip(*orig, orig[0]), 'b-o', label="Original")
    plt.plot(*zip(*trans, trans[0]), 'r--s', label="Transformado")
    plt.axhline(0, color='gray', linewidth=0.8, linestyle=':')
    plt.axvline(0, color='gray', linewidth=0.8, linestyle=':')
    plt.title(titulo)
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(f"graficos/{nome_arquivo}.png", dpi=150)
    plt.close()

def salvar_ponto(orig, trans, titulo, nome_arquivo):
    plt.figure(figsize=(6, 6))
    plt.scatter([orig[0]], [orig[1]], color='blue', s=80, label=f"Original {orig}")
    plt.scatter([trans[0]], [trans[1]], color='red', s=80, marker='s', label=f"Transformado {trans}")
    plt.axhline(0, color='gray', linewidth=0.8, linestyle=':')
    plt.axvline(0, color='gray', linewidth=0.8, linestyle=':')
    plt.title(titulo)
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(f"graficos/{nome_arquivo}.png", dpi=150)
    plt.close()

# Ex 1
p1 = np.array([2, 3])
t1 = np.array([4, -2])
salvar_ponto(p1, p1 + t1, "Exercício 1: Translação Simples", "ex01")

# Ex 2
tri2 = np.array([[1, 1], [3, 1], [2, 4]])
salvar_poligono(tri2, tri2 * 2, "Exercício 2: Escala Uniforme (s=2)", "ex02")

# Ex 3
salvar_poligono(tri2, tri2 * np.array([2, 0.5]), "Exercício 3: Escala Não Uniforme (sx=2, sy=0.5)", "ex03")

# Ex 4
rad4 = np.radians(90)
m_rot4 = np.array([[np.cos(rad4), -np.sin(rad4)], [np.sin(rad4), np.cos(rad4)]])
p4 = np.array([1, 0])
salvar_ponto(p4, np.round(p4 @ m_rot4.T, 4), "Exercício 4: Rotação 90° Anti-horário", "ex04")

# Ex 5
quad5 = np.array([[1, 1], [1, 4], [4, 4], [4, 1]])
rad5 = np.radians(-45)
m_rot5 = np.array([[np.cos(rad5), -np.sin(rad5)], [np.sin(rad5), np.cos(rad5)]])
salvar_poligono(quad5, np.round(quad5 @ m_rot5.T, 4), "Exercício 5: Rotação 45° Horário", "ex05")

# Ex 6
p6 = np.array([2, 5])
salvar_ponto(p6, p6 * np.array([-1, 1]), "Exercício 6: Reflexão no Eixo Y", "ex06")

# Ex 7
tri7 = np.array([[2, 3], [4, 3], [3, 5]])
salvar_poligono(tri7, tri7 * np.array([1, -1]), "Exercício 7: Reflexão no Eixo X", "ex07")

# Ex 8
p8 = np.array([2, 3])
m_sh8 = np.array([[1, 0], [2, 1]])  # x' = x + 2y, y' = y
salvar_ponto(p8, p8 @ m_sh8, "Exercício 8: Cisalhamento Horizontal (k=2)", "ex08")

# Ex 9
p9 = np.array([3, 2])
p9_t = p9 + np.array([1, -1])          # P'(4, 1)
p9_tr = np.round(p9_t @ m_rot4.T, 4)   # P''(-1, 4)
p9_final = p9_tr * 2                   # P'''(-2, 8)
salvar_ponto(p9, p9_final, "Exercício 9: Composição de Transformações", "ex09")

# Ex 10
ret10 = np.array([[1, 1], [5, 1], [5, 3], [1, 3]])
ret10_t = ret10 + np.array([-2, 3])
ret10_ts = ret10_t * np.array([1.5, 0.5])
ret10_final = ret10_ts * np.array([-1, 1])
salvar_poligono(ret10, ret10_final, "Exercício 10: Combinação em Figura", "ex10")

print("Todos os 10 gráficos foram gerados na pasta AC02/graficos/")