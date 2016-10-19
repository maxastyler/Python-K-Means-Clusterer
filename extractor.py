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

def rgb2hsv(colour):
    r=colour[0]/255.
    g=colour[1]/255.
    b=colour[2]/255.
    cmax=max(r, max(g, b))
    cmin=min(r, min(g, b))
    delta=cmax-cmin
    if delta==0: h=0
    else:
        if cmax==r: h=60.*(((g-b)/delta)%6.)
        elif cmax==g: h=60.*((b-r)/delta+2.)
        else: h=60.*((r-g)/delta+4.)

    if cmax==0: s=0.
    else: s=delta/cmax

    v=cmax
    return [h, s, v]

def hsv2rgb(colour):
    h, s, v=colour
    c=v*s
    x=c*(1-abs((h/60.)%2.-1))
    m=v-c
    if h>=0 and h<60.:
        r=c
        g=x
        b=0
    elif h>=60. and h<120.:
        r=x
        g=c
        b=0
    elif h>=120. and h<180.:
        r=0
        g=c
        b=x
    elif h>=180. and h<240.:
        r=0
        g=x
        b=c
    elif h>=240. and h<300.:
        r=x
        g=0
        b=c
    else:
        r=c
        g=0
        b=x
    return [int(round((r+m)*255.)), int(round((g+m)*255.)), int(round((b+m)*255.))]

def get_hue(colour):
    r, g, b = colour
    mini = min(r, min(g, b))
    maxi = max(r, max(g, b))
    if (maxi==mini): return int(round(360*r/255.))
    if maxi==r: hue = (g-b)/(maxi-mini)
    elif maxi==g: hue = 2.+(b-r)/(maxi-mini)
    else: hue = 4. + (r-g)/(maxi-mini)
    hue*=60
    if hue<0: hue+=360
    return int(round(hue))

def scale(v, vmin, vmax, mmin, mmax):
    return ((v-vmin)/(vmax-vmin)*(mmax-mmin)+mmin)


