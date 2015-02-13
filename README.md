# jsk_calibration

This is a utility package for hand/eye calibration using
[ros-perception/calibration](https://github.com/ros-perception/calibration).

This package generates sampling poses automaticaly using
[euslisp](https://github.com/euslisp/jskeus) robot models.

## Calibrate robot
calibration process has two steps.

1. capture data.

  Move robot and capturing data into a bag file.
  ```sh
  roslaunch capture_data.launch
  ```
2. estimate parameters.

  Estimate calibration parameter from the bag file.
  ```sh
  ./calibrate_${ROBOT}.sh
  ```

  And you will have calibrated urdf file.

  You can check progress of estimation parameters by rviz:
  ```sh
  rosrun rviz rviz -d view_results/pose_guesses.rviz
  ```
  ![pose_guesses](imaegs/pose_guesses.png)

## Update sampling poses
* HRP2JSKNT
```lisp
roseus euslis/hrp2-calibration.l
$ (generate-hrp2jsknt-calibration)
```

## Algorithm
1. Sampling several joint angles (for example, head joints).
2. Sampling distance from camera to checker board.
3. Sampling agnles around x, y and z axis of checker board.
4. Solve ik toward target coordinates of checker board.
5. Check self-collision.
6. For all specified sampling joints and angles, compute collision-free poses by 1-5
7. Choose good poses randomly and sparsely
8. Check self-collision for interpolated poses
9. Remove colliding poses
10. Get collision-free and different poses
