import bpy
import math

#Limpeza inicial
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

#Criar coleção organizada "AC03_transformacoes"
colecao = bpy.data.collections.new("AC03_transformacoes")
bpy.context.scene.collection.children.link(colecao)

def vincular_na_colecao(obj):
    # Move o objeto da Master Collection para a nossa colecao dedicada
    for col in obj.users_collection:
        col.objects.unlink(obj)
    colecao.objects.link(obj)

#Quadrado
bpy.ops.mesh.primitive_plane_add(size=2, location=(-4, -2, 0))
quadrado = bpy.context.active_object
quadrado.name = "obj2d_quadrado"
quadrado.scale = (1.2, 0.8, 1.0) # Escala nao-uniforme 2D
quadrado.rotation_euler = (0, 0, math.radians(25)) # Rotacao no plano XY
vincular_na_colecao(quadrado)

#Triangulo
bpy.ops.mesh.primitive_circle_add(vertices=3, radius=1.2, fill_type='NGON', location=(-4, 2, 0))
triangulo = bpy.context.active_object
triangulo.name = "obj2d_triangulo"
triangulo.rotation_euler = (0, 0, math.radians(60))
vincular_na_colecao(triangulo)

#Circulo
bpy.ops.mesh.primitive_circle_add(vertices=32, radius=1.0, fill_type='NGON', location=(-1, 0, 0))
circulo = bpy.context.active_object
circulo.name = "obj2d_circulo"
vincular_na_colecao(circulo)

#Cubo
bpy.ops.mesh.primitive_cube_add(size=1.5, location=(2, -2, 1))
cubo = bpy.context.active_object
cubo.name = "obj3d_cubo"
cubo.rotation_euler = (math.radians(30), math.radians(20), math.radians(45))
cubo.scale = (1.0, 1.3, 0.7)
vincular_na_colecao(cubo)

#Cilindro
bpy.ops.mesh.primitive_cylinder_add(radius=0.8, depth=2, location=(2, 2, 1))
cilindro = bpy.context.active_object
cilindro.name = "obj3d_cilindro"
cilindro.rotation_euler = (math.radians(15), 0, 0)
vincular_na_colecao(cilindro)

#Esfera
bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0, location=(5, 0, 1))
esfera = bpy.context.active_object
esfera.name = "obj3d_esfera"
vincular_na_colecao(esfera)

cena = bpy.context.scene
cena.frame_start = 1
cena.frame_end = 120

cena.frame_set(1)
quadrado.location = (-4, -2, 0)
quadrado.rotation_euler = (0, 0, 0)
quadrado.keyframe_insert(data_path="location", frame=1)
quadrado.keyframe_insert(data_path="rotation_euler", frame=1)

cena.frame_set(120)
quadrado.location = (-2, -1, 0) # Transladou
quadrado.rotation_euler = (0, 0, math.radians(180)) # Rotacionou 180 graus
quadrado.keyframe_insert(data_path="location", frame=120)
quadrado.keyframe_insert(data_path="rotation_euler", frame=120)

cena.frame_set(1)
cubo.scale = (1.0, 1.0, 1.0)
cubo.rotation_euler = (0, 0, 0)
cubo.keyframe_insert(data_path="scale", frame=1)
cubo.keyframe_insert(data_path="rotation_euler", frame=1)

cena.frame_set(120)
cubo.scale = (1.5, 0.6, 2.0) # Escala nao-uniforme 3D
cubo.rotation_euler = (math.radians(90), math.radians(45), math.radians(180)) # Rotacao multi-eixo
cubo.keyframe_insert(data_path="scale", frame=120)
cubo.keyframe_insert(data_path="rotation_euler", frame=120)

# Adicionar Luz do Sol
bpy.ops.object.light_add(type='SUN', location=(5, -5, 10))
luz = bpy.context.active_object
luz.data.energy = 3.0
vincular_na_colecao(luz)

# Adicionar Camera perspectiva geral
bpy.ops.object.camera_add(location=(1, -12, 9))
cam = bpy.context.active_object
cam.rotation_euler = (math.radians(55), 0, math.radians(5))
cena.camera = cam
vincular_na_colecao(cam)

cena.frame_set(1)
print("AC03: Cena construida e animada com sucesso!")