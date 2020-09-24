#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ovs
Version  : 2.13.0
Release  : 22
URL      : https://files.pythonhosted.org/packages/93/85/7f783d6872c41c1e95495c5a6ff3e20f7fd276e9fb2394c77d49a07ab6e6/ovs-2.13.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/93/85/7f783d6872c41c1e95495c5a6ff3e20f7fd276e9fb2394c77d49a07ab6e6/ovs-2.13.0.tar.gz
Summary  : Open vSwitch library
Group    : Development/Tools
License  : Apache-2.0
Requires: ovs-python = %{version}-%{release}
Requires: ovs-python3 = %{version}-%{release}
Requires: sortedcontainers
BuildRequires : buildreq-distutils3
BuildRequires : openvswitch-dev
BuildRequires : sortedcontainers

%description
Python library for working with Open vSwitch

%package python
Summary: python components for the ovs package.
Group: Default
Requires: ovs-python3 = %{version}-%{release}

%description python
python components for the ovs package.


%package python3
Summary: python3 components for the ovs package.
Group: Default
Requires: python3-core
Provides: pypi(ovs)
Requires: pypi(sortedcontainers)

%description python3
python3 components for the ovs package.


%prep
%setup -q -n ovs-2.13.0
cd %{_builddir}/ovs-2.13.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587693649
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
