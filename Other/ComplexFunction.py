# This maps complex functions from an input 2d plane to and output 2d plane in cool colours

import numpy as np

def MapImage(img, f, inputBounds,outputBounds, inputsResolution,outputResolution):

    #Create x and y sampling vectors
    xInput=np.linspace(inputBounds[0], inputBound[1], inputsResolution[1])
    yInput=np.linspace(inputBounds[2], inputBound[3], inputsResolution[0])

    #Put sampling vectors on 2D grid
    x,y=np.meshgrid(xInput,yInput)
    z=x+1j*y

    #Evaluate function
    w=f(z)

    #Linear transformation from complex numbers to pixel indicies:
    reSlope = float(outputResolution[1])/(outputBounds[1]-outputBounds[0])
    imSlope = float(outputResolution[0])/(outputBounds[3]-outputBounds[2])
    reIndex=(w.real*reSlope + outputResolution[1]/2).round().astype('int')
    imIndex=(w.imag*imSlope + outputResolution[0]/2).round().astype('int')

    #Create empty new matrix for mapping
    outputImagesize = outputResolution[:]
    outputImagesize.append(3)

    mappedImage = np.empty(outputImagesize)
    mappedImage[:] = NAN
    whiteThresh = 200

    for i in range(inputsResolution[0]):
        for j in range(inputsResolution[1]):
            if reIndex[i,j] > 0 and reIndex[i,j] < outputResolution[1]:
                #Check if that pixel has been filled yet:
                if isnan(mappedImage[imIndex[i,j],reIndex[i,j],0]):
                    mappedImage[imIndex[i,j],reIndex[i,j],:] = img[i,j,:]
                #Check if non-white:
                elif img[i,j,0] < whiteThresh or img[i,j,1] < whiteThresh or img[i,j,2:] < whiteThresh:
                    mappedImage[imIndex[i,j],reIndex[i,j],:] = img[i,j,:]

    mask = np.zeros((outputResolution[0],outputResolution[1]),dtype='uint8')
    mask[isnan(mappedImage[:,:,0])] = 1

    mappedImage = mappedImage.astype('uint8')

    #Just inpaint central square:
    maskCentral = mask.copy()[75:925,75:925]
    mappedImageCentral = mappedImageInt.copy()[75:925,75:925,:]

    dst1 = cv2.inpaint(mappedImageCentral, maskCentral, 3, cv2.INPAINT_TELEA)

    return dst1
