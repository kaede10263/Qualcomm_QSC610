import cv2
import os
import sys
import numpy as np
import subprocess

def enumerate_input(dir):
    count = len([f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f)) and f.endswith(".jpg")])//2
    return [ ["{}/{:05d}L.jpg".format(dir, i), "{}/{:05d}R.jpg".format(dir, i)] for i in range(count) ]

def prepare_image(image_pairs, output):
    if os.path.isdir(output):
        subprocess.run([ "rm", "-r", output ])
    os.makedirs(output)
    with open("filelist.txt", "w") as lst:
        lst.write("# functional_1/up_sampling2d_2/resize/ResizeBilinear:0\n")
        for i, (l, r) in enumerate(image_pairs):
            lim = cv2.imread(l)
            rim = cv2.imread(r)
            c = np.concatenate((lim, rim), axis=1)
            c = cv2.cvtColor(c, cv2.COLOR_BGR2RGB)
            c = cv2.resize(c, (512, 256)).astype(np.float32)/255
            with open("{}/{}.raw".format(output, i), 'wb') as f:
                f.write(c.tobytes())
            lst.write("input_1:0:=inputs/{}.raw\n".format(i))
    return "filelist.txt"

def run_inference(model, filelist, output = "output"):
    import time
    t = time.time()
    ret = subprocess.run(["snpe-net-run", "--perf_profile=high_performance" ,"--container={}".format(model), "--input_list={}".format(filelist), "--output_dir={}".format(output)])
    print(time.time() - t)
    return ret.returncode == 0

def generate_result(count, input, output, result):
    if os.path.isdir(result):
        subprocess.run([ "rm", "-r", result ])
    os.makedirs(result, exist_ok=True)

    for i in range(count):
        src = np.fromfile("{}/{}.raw".format(input, i), np.float32).reshape(256,512,3)*255
        res = np.fromfile("{}/Result_{}/Identity:0.raw".format(output, i), np.float32).reshape(256,512,2)
        cls = np.argmax(res, axis=2)
        mask = np.zeros((256,512,3))
        mask[cls==1, 0] = 255
        out = cv2.cvtColor((src*0.8+mask*0.2).astype(np.uint8), cv2.COLOR_RGB2BGR)
        cv2.imwrite("{}/{}.png".format(result, i), out)

# source image, input tensors, output tensors, result image,
s,i,o,r,*_ = sys.argv[1:]
im_pair = enumerate_input(s)
print(im_pair)
lst = prepare_image(im_pair, i)
if run_inference("BiSeNet.dlc", lst):
    generate_result(len(im_pair), i, o, r)
