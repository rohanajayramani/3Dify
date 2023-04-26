# 3DIFY
## Constructing 3D point clouds out of 2D images
<img src="assets/Screenshot 2023-04-26 at 10.59.23 AM.png"/>
### Inspiration
With the arrival of LiDaR sensors in iPhone 11 Pros, smartphones are now capableof capturing 3D data. Our goal is to enable normal smartphones with the ability to generate 3D data purely out of 2D images.

### How to use 
#### Obtain the camera calibration matrix
1. Take a chessboard and take multiple images of it with variations in shot angle. The chessboard must havean internal corner size of 9,6.
2. Store these images in the folder calibration_images
```
pip install -r requirements
python calib.py

```
3. Note down the calibration matrix of your camera

#### Obtain the point cloud of the object

1. Store the calibration matrix in a file named K.txt in the folder with the images of the object.
2. Insert folder name in <a href="sfm.py">sfm.py</a>.
3.
```
python sfm.py
```
4. The ply file will be stored in the res folder. 
