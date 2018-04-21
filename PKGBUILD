# Script generated with Bloom
pkgdesc="ROS - The jsk_control package"


pkgname='ros-kinetic-jsk-control'
pkgver='0.1.14_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-eus-nlopt'
'ros-kinetic-eus-qp'
'ros-kinetic-eus-qpoases'
'ros-kinetic-joy-mouse'
'ros-kinetic-jsk-calibration'
'ros-kinetic-jsk-footstep-controller'
'ros-kinetic-jsk-footstep-planner'
'ros-kinetic-jsk-ik-server'
'ros-kinetic-jsk-teleop-joy'
)

conflicts=()
replaces=()

_dir=jsk_control
source=()
md5sums=()

prepare() {
    cp -R $startdir/jsk_control $srcdir/jsk_control
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

