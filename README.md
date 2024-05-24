# 3D Gaussian Splatting for Real-Time Radiance Field Rendering

This is a 'frozen' version of the official [Gausian Splatting repository](https://github.com/graphdeco-inria/gaussian-splatting).

This is a Windows only implementation

# Installing

## Software

- Install [Miniconda](https://repo.anaconda.com/miniconda/Miniconda3-py310_24.4.0-0-Windows-x86_64.exe) (we are using Pyhton 3.10 version) Make it easy on yourself and automatically add the PATH environment variable.
![envvar](https://raw.githubusercontent.com/tooldigital/StableDiffusionAPI/main/readme/conda.png) 
- Install [Colmap](https://github.com/colmap/colmap/releases/download/3.9.1/COLMAP-3.9.1-windows-cuda.zip) and set the environment variables. We are using CUDA version 3.9.1
![envvar](https://raw.githubusercontent.com/tooldigital/Gaussian-Splatting-For-Dummies/main/github_images/env_var.png)

## Python environment

Now setup the Python environment. Use the Command Line tool and to be safe make sure you are in the location of the project. This can take a while.

```bash
conda env create -f environment.yml
```
![envvar](https://raw.githubusercontent.com/tooldigital/Gaussian-Splatting-For-Dummies/main/github_images/cmd_1.png)

now activate the conda environment

```bash
conda activate toolofna-gaussian_splatting
```
![envvar](https://raw.githubusercontent.com/tooldigital/Gaussian-Splatting-For-Dummies/main/github_images/cmd_2.png)


With the conda environment activated we now have two install two extra submodules.

```bash
pip install ./submodules/diff-gaussian-rasterization
```

```bash
pip install ./submodules/simple-knn
```

# Prepare your data
We have created 2 scripts to prepare your data.

The easiest way to assemble data is taking frames from a video or using photos from your scene or object. We advise especially to run the images script - 1a_export_images.py -  scripts even if you already have images ready. We noticed that orientation data coming from images taken with a phone can  influence the Guassian Splat the wrong way. 

Open one of the provided scripts - 1a_export_images.py or 1b_export_video.py, either for images or video and adjust the source and destination target paths.

![envvar](https://raw.githubusercontent.com/tooldigital/Gaussian-Splatting-For-Dummies/main/github_images/paths.png)

Now run the script and you see your images will be created in the output folder you specified.

```bash
python 1a_export_images.py
```
or 
```bash
python 1b_export_video.py
```

Make sure that before creating your Gaussian Splat your images are in a folder called 'input'

```
<location>
|---input
    |---<image 0>
    |---<image 1>
    |---...
```

![image](https://raw.githubusercontent.com/tooldigital/Gaussian-Splatting-For-Dummies/main/github_images/folder_structure.png)


# Create the Gaussian Splat

Creating a Gaussian Splat is a two step process. First we use COLMAP to create a pointcloud and camera calibration from your source images. 
Second this data is then used to create the actual Gaussian Splat.

## COLMAP

Make sure you are in the project root folder and run the following script. 

location is the folder of your images at the position of where 'input' resides. So do not include 'input' in the location variable. 

```bash
python convert.py -s <location>
```

For example if this is where you have your input images/dataset stored

```
|---Gaussian-Splatting-For-Dummies
    |---dataset
        |---guitar
            |---input
                |---<image 1>
                |---<image 2>
                |---...
```

Make sure you are in the root of the project, then the location is: ./dataset/guitar

Also make sure the conda environment is active.

![image](https://raw.githubusercontent.com/tooldigital/Gaussian-Splatting-For-Dummies/main/github_images/colmap_location.png)

When everything goes well the result should look something like this

![image](https://raw.githubusercontent.com/tooldigital/Gaussian-Splatting-For-Dummies/main/github_images/result.png)

And you should see a bunch of new folders next to your input folder

![image](https://raw.githubusercontent.com/tooldigital/Gaussian-Splatting-For-Dummies/main/github_images/folders_colmap_reult.png)

Now we will use this data to create the actual Gaussian Splat

## Gausian Splat creation

Now we will use the train script to create the actual splat.

```bash
python train.py -s <path to COLMAP>
```

The path to COLMAP is actually the same folder you used for the COLMAP generation.
