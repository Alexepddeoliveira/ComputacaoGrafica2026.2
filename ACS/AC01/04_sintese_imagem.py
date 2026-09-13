import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Definição do Universo Geométrico 
vertices = np.array([
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
])

# Conectividade dos vértices
faces = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],
    [vertices[4], vertices[5], vertices[6], vertices[7]], 
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[2], vertices[3], vertices[7], vertices[6]], 
    [vertices[1], vertices[2], vertices[6], vertices[5]],
    [vertices[4], vertices[7], vertices[3], vertices[0]]  
]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

colecao_poligonos = Poly3DCollection(
    faces,
    facecolors=['cyan', 'deepskyblue', 'dodgerblue', 'cornflowerblue', 'steelblue', 'royalblue'],
    linewidths=1.5,
    edgecolors='black',
    alpha=0.85
)
ax.add_collection3d(colecao_poligonos)

# Câmera Virtual 
ax.view_init(elev=25, azim=45)
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Rótulos espaciais
ax.set_title("Síntese de Imagens: Renderização de Malha Poligonal 3D", fontsize=13)
ax.set_xlabel("X (Largura)")
ax.set_ylabel("Y (Profundidade)")
ax.set_zlabel("Z (Altura)")

plt.tight_layout()
plt.savefig('saida_sintese.png', dpi=300)
print("Sucesso: Imagem 'saida_sintese.png' sintetizada e gerada na pasta!")