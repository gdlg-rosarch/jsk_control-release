Name:           ros-indigo-jsk-footstep-planner
Version:        0.1.10
Release:        0%{?dist}
Summary:        ROS jsk_footstep_planner package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_footstep_planner
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-jsk-footstep-msgs
Requires:       ros-indigo-jsk-interactive-marker
Requires:       ros-indigo-jsk-recognition-msgs
Requires:       ros-indigo-jsk-recognition-utils
Requires:       ros-indigo-jsk-rviz-plugins
Requires:       ros-indigo-jsk-topic-tools
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roseus
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-jsk-footstep-msgs
BuildRequires:  ros-indigo-jsk-interactive-marker
BuildRequires:  ros-indigo-jsk-recognition-utils
BuildRequires:  ros-indigo-jsk-rviz-plugins
BuildRequires:  ros-indigo-jsk-topic-tools
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roseus
BuildRequires:  ros-indigo-visualization-msgs

%description
jsk_footstep_planner

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Dec 15 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.10-0
- Autogenerated by Bloom

* Wed Mar 23 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.9-0
- Autogenerated by Bloom

* Mon Nov 02 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.8-0
- Autogenerated by Bloom

* Sun Nov 01 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.7-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.6-0
- Autogenerated by Bloom

* Fri Feb 13 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.5-0
- Autogenerated by Bloom

