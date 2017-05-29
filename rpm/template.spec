Name:           ros-lunar-canopen-chain-node
Version:        0.7.5
Release:        0%{?dist}
Summary:        ROS canopen_chain_node package

Group:          Development/Libraries
License:        LGPLv3
URL:            http://wiki.ros.org/canopen_chain_node
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-canopen-master
Requires:       ros-lunar-diagnostic-updater
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-pluginlib
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-roslib
Requires:       ros-lunar-socketcan-interface
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-std-srvs
BuildRequires:  ros-lunar-canopen-master
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-diagnostic-updater
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-pluginlib
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-roslib
BuildRequires:  ros-lunar-socketcan-interface
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-std-srvs

%description
ROS node base implementation for CANopen chains with support for management
services and diagnostics

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Mon May 29 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.5-0
- Autogenerated by Bloom

* Tue Apr 25 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.4-0
- Autogenerated by Bloom

* Tue Apr 25 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.3-0
- Autogenerated by Bloom

* Tue Apr 25 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.2-0
- Autogenerated by Bloom

