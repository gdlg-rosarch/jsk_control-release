Name:           ros-hydro-eus-qp
Version:        0.1.5
Release:        0%{?dist}
Summary:        ROS eus_qp package

Group:          Development/Libraries
License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-hydro-euslisp
BuildRequires:  eigen3-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-euslisp

%description
eus_qp is an interface of euslisp to solve qp problems with linear constraints.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Jan 08 2015 Noda Shintaro <s-noda@jsk.t.u-tokyo.ac.jp> - 0.1.5-0
- Autogenerated by Bloom

* Sat Oct 11 2014 Noda Shintaro <s-noda@jsk.t.u-tokyo.ac.jp> - 0.1.3-0
- Autogenerated by Bloom

* Thu Sep 04 2014 Noda Shintaro <s-noda@jsk.t.u-tokyo.ac.jp> - 0.1.1-0
- Autogenerated by Bloom

