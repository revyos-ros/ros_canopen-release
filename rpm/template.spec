%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/melodic/.*$
%global __requires_exclude_from ^/opt/ros/melodic/.*$

Name:           ros-melodic-canopen-motor-node
Version:        0.8.2
Release:        1%{?dist}
Summary:        ROS canopen_motor_node package

License:        LGPLv3
URL:            http://wiki.ros.org/canopen_motor_node
Source0:        %{name}-%{version}.tar.gz

Requires:       muParser-devel
Requires:       ros-melodic-canopen-402
Requires:       ros-melodic-canopen-chain-node
Requires:       ros-melodic-canopen-master
Requires:       ros-melodic-controller-manager
Requires:       ros-melodic-controller-manager-msgs
Requires:       ros-melodic-filters
Requires:       ros-melodic-hardware-interface
Requires:       ros-melodic-joint-limits-interface
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-urdf
BuildRequires:  muParser-devel
BuildRequires:  ros-melodic-canopen-402
BuildRequires:  ros-melodic-canopen-chain-node
BuildRequires:  ros-melodic-canopen-master
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-controller-manager
BuildRequires:  ros-melodic-controller-manager-msgs
BuildRequires:  ros-melodic-filters
BuildRequires:  ros-melodic-hardware-interface
BuildRequires:  ros-melodic-joint-limits-interface
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rosunit
BuildRequires:  ros-melodic-urdf

%description
canopen_chain_node specialization for handling of canopen_402 motor devices. It
facilitates interface abstraction with ros_control.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/melodic

%changelog
* Mon Nov 04 2019 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.8.2-1
- Autogenerated by Bloom

* Sun Jul 14 2019 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.8.1-1
- Autogenerated by Bloom

* Wed Jul 11 2018 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.8.0-0
- Autogenerated by Bloom

