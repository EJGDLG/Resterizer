from gl import Renderer
from obj import Obj
from ModelLoader import ModelLoader 

width = 480
height = 270

# Crear el renderizador
rend = Renderer(width, height)

rend.glClearColor(0.5, 0.5, 0.7)
rend.glBackgroundTexture("resources/textures/tree.bmp")
rend.glclearBackground()
rend.glLookAt(camPos=(0, 0, -10), eyePos=(0, 0, -5))

# Cargar y agregar modelos
model_loader = ModelLoader(rend)
model_loader.load_models()

# Renderizar y guardar el resultado
rend.glRender()
rend.glFinish("./results/p1.bmp")
