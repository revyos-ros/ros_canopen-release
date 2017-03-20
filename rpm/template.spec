Name:           ros-kinetic-canopen-chain-node
Version:        0.7.1
Release:        0%{?dist}
Summary:        ROS canopen_chain_node package

Group:          Development/Libraries
License:        LGPLv3
URL:            http://wiki.ros.org/canopen_chain_node
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-canopen-master
Requires:       ros-kinetic-diagnostic-updater
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-socketcan-interface
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-canopen-master
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-diagnostic-updater
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslib
BuildRequires:  ros-kinetic-socketcan-interface
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-std-srvs

%description
ROS node base implementation for CANopen chains with support for management
services and diagnostics

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Mar 20 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.1-0
- Autogenerated by Bloom

* Thu Dec 15 2016 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.0-0
- Autogenerated by Bloom

