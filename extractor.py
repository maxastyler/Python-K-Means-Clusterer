from PIL import Image
from skimage import color
from clusterer import k_means
import numpy as np

def get_colours(file_name, thumb_size):
    img=Image.open(file_name)
    img.thumbnail(thumb_size)
    img=np.asarray(img)/255.
    img=color.rgb2lab(img)
    colours=[]
    for i in range(len(img)):
        for j in range(len(img[i])):
            colours.append((img[i][j][0], img[i][j][1], img[i][j][2]))
    return colours

def k_means_to_np_array(k_means_out):
    out_array=np.zeros((1, len(k_means_out), 3))
    for i in range(len(k_means_out)):
        for j in range(3):
            out_array[0][i][j]=k_means_out[i][j]
    return out_array

def extract_colours_from_image(file_name, num_colours, img_sample_size, min_distance=1):
    outed=k_means_to_np_array(k_means(get_colours(file_name, img_sample_size), num_colours, min_distance))
    outed=color.lab2rgb(outed)
    return_colours=[]
    for i in range(len(outed)):
        for j in range(len(outed[i])):
            return_colours.append([])
            for k in range(len(outed[i][j])):
                return_colours[j].append(int(np.round(outed[i][j][k]*255)))
    return return_colours

#print(k_means(get_colours("akira.jpg", (100, 100)), 3, 2))
#get_colours("akira.jpg", (10, 10))
