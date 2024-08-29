from gl import Renderer,V2,V3,color, Model
from obj import Obj
import shaders
import random


width = 480
height = 270

# width = 500
# height = 620

rend = Renderer(width,height)

# rend.glViewPort(width/4,height/4,width/2,height/2)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.gouradShader

rend.glClearColor(0.5,0.5,0.7)
rend.glBackgroundTexture("resources/textures/tree.bmp")
rend.glclearBackground()

rend.glLookAt(camPos=(0,0,-10),
              eyePos=(0,0,-5))

# # #cargamos los modelos
model1 = Model("./resources/models/PenguinBaseMesh.obj",
              translate=(-1,2.3,-15),
              rotate= (180,130,0),
              scale=(1.5,1.5,1.5))
model1.LoadTexture("./resources/textures/PenguinDiffuseColor1.bmp")
model1.SetShaders(shaders.vertexShader, shaders.pink)

model2 = Model("./resources/models/bracelet.obj",
              translate=(1,1.5,-15),
              rotate= (20,60,180),
              scale=(0.1,0.1,0.1))
model2.LoadTexture("./resources/textures/silk.bmp")
model2.SetShaders(shaders.vertexShader, shaders.tempshader)

model3 = Model("./resources/models/pumpkin.obj",
              translate=(5,3.5,-17),
              rotate= (210,200,0),
              scale=(2,2,2))
model3.LoadTexture("./resources/textures/silk.bmp")
model3.SetShaders(shaders.vertexShader, shaders.negativeShader)

model4 = Model("./resources/models/axe.obj",
              translate=(1.8,2,-20),
              rotate= (140,30,0),
              scale=(0.9,0.9,0.9))
model4.LoadTexture("./resources/textures/skin.bmp")
model4.SetShaders(shaders.vertexShader, shaders.gouradShader)

model5 = Model("./resources/models/PenguinBaseMesh.obj",
              translate=(4,1.15,-17),
              rotate= (180,-10,0),
              scale=(1.5,1.5,1.5))
model5.LoadTexture("./resources/textures/gold.bmp")
model5.SetShaders(shaders.vertexShader, shaders.distortionshader)

rend.glAddModel(model1)
rend.glAddModel(model2)
rend.glAddModel(model3)
rend.glAddModel(model4)
rend.glAddModel(model5)

rend.glRender()
rend.glFinish("./results/p1.bmp")

