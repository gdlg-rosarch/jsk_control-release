# Script generated with Bloom
pkgdesc="ROS - jsk_teleop_joy"
url='http://ros.org/wiki/jsk_teleop_joy'

pkgname='ros-kinetic-jsk-teleop-joy'
pkgver='0.1.14_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-interactive-markers'
'ros-kinetic-joy-mouse'
'ros-kinetic-jsk-footstep-msgs'
'ros-kinetic-jsk-interactive-marker'
'ros-kinetic-jsk-rviz-plugins'
'ros-kinetic-ps3joy'
'ros-kinetic-tf'
'ros-kinetic-view-controller-msgs'
'ros-kinetic-visualization-msgs'
)

depends=('python2-pygame'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-image-view2'
'ros-kinetic-interactive-markers'
'ros-kinetic-joy-mouse'
'ros-kinetic-jsk-footstep-msgs'
'ros-kinetic-jsk-interactive-marker'
'ros-kinetic-jsk-rviz-plugins'
'ros-kinetic-ps3joy'
'ros-kinetic-tf'
'ros-kinetic-view-controller-msgs'
'ros-kinetic-visualization-msgs'
)

conflicts=()
replaces=()

_dir=jsk_teleop_joy
source=()
md5sums=()

prepare() {
    cp -R $startdir/jsk_teleop_joy $srcdir/jsk_teleop_joy
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

