#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ovs
Version  : 2.9.2
Release  : 9
URL      : https://files.pythonhosted.org/packages/43/a1/78f54030f34ae8b818d85fcbafcd9ae148f97c0d0f7955ecc217a30d6a10/ovs-2.9.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/43/a1/78f54030f34ae8b818d85fcbafcd9ae148f97c0d0f7955ecc217a30d6a10/ovs-2.9.2.tar.gz
Summary  : Open vSwitch library
Group    : Development/Tools
License  : Apache-2.0
Requires: ovs-python3
Requires: ovs-python
Requires: sortedcontainers
BuildRequires : buildreq-distutils3
BuildRequires : openvswitch-dev
BuildRequires : sortedcontainers

%description
Python library for working with Open vSwitch

%package python
Summary: python components for the ovs package.
Group: Default
Requires: ovs-python3

%description python
python components for the ovs package.


%package python3
Summary: python3 components for the ovs package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ovs package.


%prep
%setup -q -n ovs-2.9.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533876835
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
