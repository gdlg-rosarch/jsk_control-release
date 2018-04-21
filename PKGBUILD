# Script generated with Bloom
pkgdesc="ROS - The jsk_footstep_controller package"


pkgname='ros-kinetic-jsk-footstep-controller'
pkgver='0.1.14_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-genmsg'
'ros-kinetic-geometry-msgs'
'ros-kinetic-jsk-footstep-msgs'
'ros-kinetic-jsk-footstep-planner'
'ros-kinetic-jsk-pcl-ros'
'ros-kinetic-jsk-topic-tools'
'ros-kinetic-kdl-conversions'
'ros-kinetic-kdl-parser'
'ros-kinetic-message-filters'
'ros-kinetic-message-generation'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
'ros-kinetic-tf2'
'ros-kinetic-urdf'
)

depends=('ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-genmsg'
'ros-kinetic-geometry-msgs'
'ros-kinetic-jsk-footstep-msgs'
'ros-kinetic-jsk-footstep-planner'
'ros-kinetic-jsk-pcl-ros'
'ros-kinetic-jsk-topic-tools'
'ros-kinetic-kdl-conversions'
'ros-kinetic-kdl-parser'
'ros-kinetic-message-filters'
'ros-kinetic-message-generation'
'ros-kinetic-sensor-msgs'
'ros-kinetic-sound-play'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
'ros-kinetic-tf2'
'ros-kinetic-urdf'
)

conflicts=()
replaces=()

_dir=jsk_footstep_controller
source=()
md5sums=()

prepare() {
    cp -R $startdir/jsk_footstep_controller $srcdir/jsk_footstep_controller
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

