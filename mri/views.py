from django.http.response import HttpResponse
from django.shortcuts import render
from .models import MriDdbb

import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
from sklearn.cluster import KMeans


# Create your views here.

def MriHtml(request):
    list_mri = MriDdbb.objects.all()
    return render(request, "mri/mri.html", {"list_mri": list_mri})

def Inlet(request):
    return HttpResponse(request, 'mri/mri.html')

    
def MriAction(request):


    list_mri = MriDdbb.objects.all()
    


    # list_Fotos = ["img_Esclerosis_1.jfif", "img_TDA.jfif", "img_Sano_1.jpg" ,"img_Esclerosis_2.jfif","img_sano_2.jpg", "img_Epilepsia.jpeg", "img_Esclerosis_3.jpg", "img_SHunter.jpg", "img_Lesion-Hipoxico-isquemica-aguda_Niños.jpg", "imgcolor_1.png", "imgcolor_2.gif", "imgcolor_3.jpg", "imgcolor_4.jfif", "captus_1.jpg","captus_5.jpg", "captus_3.jpg","captus_4.jfif"]
    # request = list_mri.append(str(request))
    Foto = ""
    for result in list_mri:
        Foto = result.image
        I1 = Image.open(Foto)
        I1 = I1.convert('L')
        I2 = np.asarray(I1,dtype=np.float)
        
        I2 = (I2-np.min(I2))/(np.max(I2)-np.min(I2))*255
        I2 = Image.fromarray(I2.astype(np.uint8))
        w, h =I2.size
        I2 = I2.convert('RGB')
        colors = I2.getcolors(w * h)


        
        # # I2 = I2.convert('L')
        # # I2 = np.shape((-1, 2))
        # X = I2.reshape((-1, 1))
        # # X = I2
        # # # ******************

        # k_means = KMeans(n_clusters=3)
        # k_means.fit(X) 
        # # # ******************

        # centroides = k_means.cluster_centers_
        # etiquetas = k_means.labels_
        # # # ******************

        # I2_compressed = np.choose(etiquetas, centroides)
        # I2_compressed.shape = I2.shape
        # # # ******************
        
        list = []
        for elem, rgb in colors:
            if (elem == 17 and rgb[0] == 206 and rgb[1] == 206 and rgb[2] == 206) or (elem == 1 and rgb[0] == 232 and rgb[1] == 232 and rgb[2] == 232):
                
                plt.figure(figsize=(8,8))
                plt.imshow(I2)
                plt.axis('off')
                plt.show()
                
                plt.figure(figsize=(8,8))
                plt.imshow(I2.convert('L'),cmap=None)
                plt.axis('off')
                plt.show()

                

                # plt.figure(figsize=(8,8))
                # plt.imshow(I2_compressed,cmap=None)
                # plt.axis('off')
                # plt.show()
                # ******************
                break
    return render(request, "mri/mri.html", {"list_mri": list_mri})
    
