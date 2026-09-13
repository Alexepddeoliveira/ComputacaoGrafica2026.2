import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

superficie = ax.plot_surface(
    X, Y, Z,
    cmap='viridis',
    edgecolor='none',
    antialiased=True
)

# Adicionar anotações visuais para interpretação humana
ax.set_title("Visualização Científica: Superfície 3D de Onda Escalar", fontsize=14)
ax.set_xlabel("Eixo X (Coordenada Espacial)")
ax.set_ylabel("Eixo Y (Coordenada Espacial)")
ax.set_zlabel("Eixo Z (Amplitude f(X, Y))")

fig.colorbar(superficie, ax=ax, shrink=0.5, aspect=10, label="Magnitude de Z")

plt.tight_layout()
plt.savefig('saida_visualizacao.png', dpi=300)
print("Sucesso: Imagem 'saida_visualizacao.png' gerada a partir dos dados numéricos!")