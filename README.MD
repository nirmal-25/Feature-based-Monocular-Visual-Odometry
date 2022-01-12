# Feature-based Monocular Visual Odometry

###The folder directory is as follows:<br /><p>&nbsp;</p>
####**data** contains the dataset (download dataset - 22 GB, from official KITTI website and place it here), output (ATE and RPE graphs) and results (text files in the KITTI dataset format for rotation and translation matrices - [r11, r12, r13, tx, r21, r22, r23, ty, r31, r32, r33, tz])<br /><p>&nbsp;</p>
####**main** contains our eval_vo.py script which evaluates the results from pySLAM using the evo tool, and run.ipynb file for generating the .txt files for results using pySLAM. The ipynb file has provision for testing different detector-descriptor combinations for KITTI sequences<br /><p>&nbsp;</p>
####**pyslam** contains [pySLAM v2](https://github.com/luigifreda/pyslam), an open-source implementation for monocular visual odometry<br />