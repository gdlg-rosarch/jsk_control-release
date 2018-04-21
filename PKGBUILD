# Script generated with Bloom
pkgdesc="ROS - jsk_footstep_planner"
url='http://ros.org/wiki/jsk_footstep_planner'

pkgname='ros-kinetic-jsk-footstep-planner'
pkgver='0.1.14_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-geometry-msgs'
'ros-kinetic-jsk-footstep-msgs'
'ros-kinetic-jsk-interactive-marker'
'ros-kinetic-jsk-recognition-utils'
'ros-kinetic-jsk-rviz-plugins'
'ros-kinetic-jsk-topic-tools'
'ros-kinetic-message-generation'
'ros-kinetic-pcl-ros'
'ros-kinetic-roscpp'
'ros-kinetic-roseus'
'ros-kinetic-visualization-msgs'
)

depends=('ros-kinetic-dynamic-reconfigure'
'ros-kinetic-geometry-msgs'
'ros-kinetic-jsk-footstep-msgs'
'ros-kinetic-jsk-interactive-marker'
'ros-kinetic-jsk-pcl-ros'
'ros-kinetic-jsk-recognition-msgs'
'ros-kinetic-jsk-recognition-utils'
'ros-kinetic-jsk-rviz-plugins'
'ros-kinetic-jsk-topic-tools'
'ros-kinetic-pcl-ros'
'ros-kinetic-roscpp'
'ros-kinetic-roseus'
'ros-kinetic-visualization-msgs'
)

conflicts=()
replaces=()

_dir=jsk_footstep_planner
source=()
md5sums=()

prepare() {
    cp -R $startdir/jsk_footstep_planner $srcdir/jsk_footstep_planner
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

