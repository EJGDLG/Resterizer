import meth as metha
import math

def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]

    vt = [vertex[0],
          vertex[1],
          vertex[2],
          1]
    
    vt = metha.multiplyMatrixVector(vt,metha.multiplymatrix(metha.multiplymatrix(metha.multiplymatrix(vpMatrix,projectionMatrix),viewMatrix),modelMatrix))

    vt = [vt[0]/vt[3],
          vt[1]/vt[3],
          vt[2]/vt[3]]

    return vt

def fatShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]
    normal = kwargs["normal"]

    blowAmount = 0.05

    vt = [vertex[0] + (normal[0]*blowAmount),
          vertex[1] + (normal[1]*blowAmount),
          vertex[2] + (normal[2]*blowAmount),
          1]
    
    vt = metha.multiplyMatrixVector(vt,metha.multiplymatrix(metha.multiplymatrix(metha.multiplymatrix(vpMatrix,projectionMatrix),viewMatrix),modelMatrix))


    vt = [vt[0]/vt[3],
          vt[1]/vt[3],
          vt[2]/vt[3]]

    return vt

def fragmentShader(**kwargs):
    tA,tB,tC = kwargs["texCoords"]
    texture = kwargs["texture"]
    u,v,w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        tU = u*tA[0] + v*tB[0] + w*tC[0]
        tV = u*tA[1] + v*tB[1] + w*tC[1]

        textureColor = texture.getColor(tU,tV)
        b = textureColor[2]
        g = textureColor[1]
        r = textureColor[0]

    return r,g,b

def pink(**kwargs):
    tA,tB,tC = kwargs["texCoords"]
    texture = kwargs["texture"]
    u,v,w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        tU = u*tA[0] + v*tB[0] + w*tC[0]
        tV = u*tA[1] + v*tB[1] + w*tC[1]

        textureColor = texture.getColor(tU,tV)
        b = textureColor[2]
        g = textureColor[1]
        r = textureColor[0]

    pink = (1,0.784,0.866)

    b *= pink[2]
    g *= pink[1]
    r *= pink[0]

    return r,g,b

def flatShader(**kwargs):
    dLight = kwargs["dLight"]
    normal = kwargs["normals"]
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        textureColor = texture.getColor(texCoords[0],texCoords[1])
        b = textureColor[2]
        g = textureColor[1]
        r = textureColor[0]


    dLight = list(dLight)
    for e in range(len(dLight)):
        dLight[e] = -1 * dLight[e]

    intensity = metha.dotProd(normal,dLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r,g,b
    else:
        return (0,0,0)
    
def gouradShader(**kwargs):
    dLight = kwargs["dLight"]
    nA,nB,nC = kwargs["normals"]
    tA,tB,tC = kwargs["texCoords"]
    texture = kwargs["texture"]
    u,v,w = kwargs["bCoords"]
    modelMatrix = kwargs["modelMatrix"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        tU = u*tA[0] + v*tB[0] + w*tC[0]
        tV = u*tA[1] + v*tB[1] + w*tC[1]

        textureColor = texture.getColor(tU,tV)
        b = textureColor[2]
        g = textureColor[1]
        r = textureColor[0]

    normal = [u*nA[0] + v*nB[0] + w*nC[0],
              u*nA[1] + v*nB[1] + w*nC[1],
              u*nA[2] + v*nB[2] + w*nC[2],
              0]
    
    normal = metha.multiplyMatrixVector(normal,modelMatrix)
    normal = [normal[0], normal[1], normal[2]]
    
    dLight = list(dLight)
    for e in range(len(dLight)):
        dLight[e] = -1 * dLight[e]

    intensity = metha.dotProd(normal,dLight)
    
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0.0:
        r = max(0.0, min(1.0, r))
        g = max(0.0, min(1.0, g))
        b = max(0.0, min(1.0, b))
        return r,g,b
    else:
        return (0,0,0)
    
def negativeShader(**kwargs):
    dLight = kwargs["dLight"]
    nA,nB,nC = kwargs["normals"]
    tA,tB,tC = kwargs["texCoords"]
    texture = kwargs["texture"]
    u,v,w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        tU = u*tA[0] + v*tB[0] + w*tC[0]
        tV = u*tA[1] + v*tB[1] + w*tC[1]

        textureColor = texture.getColor(tU,tV)
        b = textureColor[2]
        g = textureColor[1]
        r = textureColor[0]

    normal = [u*nA[0] + v*nB[0] + w*nC[0],
              u*nA[1] + v*nB[1] + w*nC[1],
              u*nA[2] + v*nB[2] + w*nC[2],]
    
    dLight = list(dLight)
    for e in range(len(dLight)):
        dLight[e] = -1 * dLight[e]

    intensity = metha.dotProd(normal,dLight)
    
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        r = 1.0 - r
        g = 1.0 - g
        b = 1.0 - b
        r = max(0.0, min(1.0, r))
        g = max(0.0, min(1.0, g))
        b = max(0.0, min(1.0, b))
        return r,g,b
    else:
        return (1,1,1) 

def tempshader(**kwargs):
    dLight = kwargs["dLight"]
    nA,nB,nC = kwargs["normals"]
    tA,tB,tC = kwargs["texCoords"]
    texture = kwargs["texture"]
    u,v,w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        tU = u*tA[0] + v*tB[0] + w*tC[0]
        tV = u*tA[1] + v*tB[1] + w*tC[1]

        textureColor = texture.getColor(tU,tV)
        b = textureColor[2]
        g = textureColor[1]
        r = textureColor[0]

    normal = [u*nA[0] + v*nB[0] + w*nC[0],
              u*nA[1] + v*nB[1] + w*nC[1],
              u*nA[2] + v*nB[2] + w*nC[2],]
    
    dLight = list(dLight)
    for e in range(len(dLight)):
        dLight[e] = -1 * dLight[e]

    intensity = metha.dotProd(normal,dLight)

    if intensity > 0:
        hue = (intensity + 1) / 2
        if 0 <= hue < 1/6:
            r = 1.0
            g = hue * 6
            b = 0.0
        elif 1/6 <= hue < 2/6:
            r = 1.0 - (hue - 1/6) * 6
            g = 1.0
            b = 0.0
        elif 2/6 <= hue < 3/6:
            r = 0.0
            g = 1.0
            b = (hue - 2/6) * 6
        elif 3/6 <= hue < 4/6:
            r = 0.0
            g = 1.0 - (hue - 3/6) * 6
            b = 1.0
        elif 4/6 <= hue < 5/6:
            r = (hue - 4/6) * 6
            g = 0.0
            b = 1.0
        else:
            r = 1.0
            g = 0.0
            b = 1.0 - (hue - 5/6) * 6

        r = max(0.0, min(1.0, r))
        g = max(0.0, min(1.0, g))
        b = max(0.0, min(1.0, b))
        return r, g, b
    else:
        return (0,0,0)
    
def distortionshader(**kwargs):
    dLight = kwargs["dLight"]
    nA,nB,nC = kwargs["normals"]
    tA,tB,tC = kwargs["texCoords"]
    texture = kwargs["texture"]
    u,v,w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    distortion = 0.02

    if texture != None:
        tU = (u + math.sin(v * 10) * distortion) * tA[0] + \
             (v + math.cos(u * 10) * distortion) * tB[0] + \
             (w + math.sin((u + v) * 10) * distortion) * tC[0]

        tV = (u + math.sin(v * 10) * distortion) * tA[1] + \
             (v + math.cos(u * 10) * distortion) * tB[1] + \
             (w + math.sin((u + v) * 10) * distortion) * tC[1]

        textureColor = texture.getColor(tU,tV)
        if textureColor != None:
            b = textureColor[2]
            g = textureColor[1]
            r = textureColor[0]

    normal = [u*nA[0] + v*nB[0] + w*nC[0],
              u*nA[1] + v*nB[1] + w*nC[1],
              u*nA[2] + v*nB[2] + w*nC[2],]
    
    dLight = list(dLight)
    for e in range(len(dLight)):
        dLight[e] = -1 * dLight[e]

    intensity = metha.dotProd(normal,dLight)
    
    b *= intensity
    g *= intensity
    r *= intensity

    r = max(0.0, min(1.0, r))
    g = max(0.0, min(1.0, g))
    b = max(0.0, min(1.0, b))

    if intensity > 0:
        return r,g,b
    else:
        return (0,0,0)