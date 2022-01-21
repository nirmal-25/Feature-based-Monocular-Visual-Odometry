# Feature-based Monocular Visual Odometry

This is the project repo for Monocular Visual Odometry using popular feature detectors and descriptors. Open-source repositories pySLAM v2 and evo are used for implementing and evaluating the VO system respectively. The complete pipeline is explained in detail in the report provided - [Project Report](https://velvetthunder25.github.io/Feature-based-Monocular-Visual-Odometry/)<br /><br />

The folder directory is as follows:<br />
- **data** contains the dataset (download dataset - 22 GB, from official KITTI website and place it here), output (ATE and RPE graphs) and results (text files in the KITTI dataset format for rotation and translation matrices - [r11, r12, r13, tx, r21, r22, r23, ty, r31, r32, r33, tz])<br />
- **main** contains the eval_vo.py script which evaluates the results from pySLAM using the evo tool, and run.ipynb file for generating the .txt files for results using pySLAM. The ipynb file has provision for testing different detector-descriptor combinations for KITTI sequences<br />
- **pyslam** contains [pySLAM v2](https://github.com/luigifreda/pyslam), an open-source implementation for monocular visual odometry<br />

![ezgif-3-c55a71831d](https://user-images.githubusercontent.com/51696913/150459529-88ec69a7-be9d-4018-996a-0983843e5554.gif)
