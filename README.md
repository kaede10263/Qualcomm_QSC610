# Qualcomm_QSC610
 
## Abstract
![](https://i.imgur.com/j1vUBl2.png)

## research
device check:
![](https://i.imgur.com/5vzNLyt.png)

push script
![](https://i.imgur.com/jqUSgjt.png)

excute prepare.py
![](https://i.imgur.com/zjkhJ5E.png)

excute raw2img.py
![](https://i.imgur.com/gHnPKX8.png)

output
```
The output of model : 

/data/misc/snpe # python3
Python 3.5.6 (default, Jul 17 2022, 02:20:37)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> a = np.fromfile("output/Result_0/Identity:0.raw", np.float32)
>>> a = a.reshape(256,512,2)
>>> a[:2,:2,:]
array([[[ 0.3417609 , -3.3565354 ],
        [ 0.3417609 , -3.3565354 ]],

       [[ 0.34176087, -3.3565357 ],
        [ 0.34176087, -3.3565354 ]]], dtype=float32)
>>> a[125:127,125:127,:]
array([[[ 0.6921668 , -0.02086171],
        [ 0.6782332 , -0.02377823]],

       [[ 0.60884655,  0.04313333],
        [ 0.5913134 ,  0.04448493]]], dtype=float32)
>>> a[126:128,448:450,:]
array([[[-1.3914882,  1.5720341],
        [-1.3858252,  1.550932 ]],

       [[-1.4344666,  1.6104436],
        [-1.422902 ,  1.5921738]]], dtype=float32)
>>>
```

## instruction
![](https://i.imgur.com/I9vQXZF.png)

```
git clone https://github.com/kaede10263/Qualcomm_QSC610.git
```
download [platform-tools](https://developer.android.com/studio/releases/platform-tools) 
![](https://i.imgur.com/WwWPrnN.png)

```
cd Qualcomm_QSC610
.\run.ps1
```
![](https://i.imgur.com/YA56ZQe.png)

## final
We have already test three images to inference. The FPS is about 2.If the input image size is 3Mb, it will generate 6.25Mb of memory space, the current available capacity is 2.4Gb. We estimate the maximum number of input images to be 750.
