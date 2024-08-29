from gl import Model
import shaders

class ModelLoader:
    def __init__(self, renderer):
        self.renderer = renderer
    
    def load_models(self):
        # Cargar los modelos
        model1 = Model("./resources/models/PenguinBaseMesh.obj",
                      translate=(-1, 2.3, -15),
                      rotate=(180, 130, 0),
                      scale=(1.5, 1.5, 1.5))
        model1.LoadTexture("./resources/textures/PenguinDiffuseColor1.bmp")
        model1.SetShaders(shaders.vertexShader, shaders.pink)
        
        model2 = Model("./resources/models/bracelet.obj",
                      translate=(1, 1.5, -15),
                      rotate=(20, 60, 180),
                      scale=(0.1, 0.1, 0.1))
        model2.LoadTexture("./resources/textures/silk.bmp")
        model2.SetShaders(shaders.vertexShader, shaders.tempshader)
        
        model3 = Model("./resources/models/pumpkin.obj",
                      translate=(5, 3.5, -17),
                      rotate=(210, 200, 0),
                      scale=(2, 2, 2))
        model3.LoadTexture("./resources/textures/silk.bmp")
        model3.SetShaders(shaders.vertexShader, shaders.negativeShader)
        
        model4 = Model("./resources/models/axe.obj",
                      translate=(1.8, 2, -20),
                      rotate=(140, 30, 0),
                      scale=(0.9, 0.9, 0.9))
        model4.LoadTexture("./resources/textures/skin.bmp")
        model4.SetShaders(shaders.vertexShader, shaders.gouradShader)
        
        model5 = Model("./resources/models/PenguinBaseMesh.obj",
                      translate=(4, 1.15, -17),
                      rotate=(180, -10, 0),
                      scale=(1.5, 1.5, 1.5))
        model5.LoadTexture("./resources/textures/gold.bmp")
        model5.SetShaders(shaders.vertexShader, shaders.distortionshader)
        
        # Agregar modelos al renderizador
        self.renderer.glAddModel(model1)
        self.renderer.glAddModel(model2)
        self.renderer.glAddModel(model3)
        self.renderer.glAddModel(model4)
        self.renderer.glAddModel(model5)
