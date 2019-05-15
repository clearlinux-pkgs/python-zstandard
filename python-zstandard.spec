#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-zstandard
Version  : 0.11.1
Release  : 8
URL      : https://github.com/indygreg/python-zstandard/archive/0.11.1/python-zstandard-0.11.1.tar.gz
Source0  : https://github.com/indygreg/python-zstandard/archive/0.11.1/python-zstandard-0.11.1.tar.gz
Summary  : Python bindings to the Zstandard (zstd) compression library
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: python-zstandard-license = %{version}-%{release}
Requires: python-zstandard-python = %{version}-%{release}
Requires: python-zstandard-python3 = %{version}-%{release}
Requires: attrs
Requires: cffi
Requires: enum34
Requires: filelock
Requires: nose
Requires: pycparser
Requires: six
Requires: toml
BuildRequires : attrs
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : enum34
BuildRequires : filelock
BuildRequires : hypothesis
BuildRequires : nose
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pycparser
BuildRequires : pytest
BuildRequires : six
BuildRequires : toml
BuildRequires : tox
BuildRequires : virtualenv

%description
================
python-zstandard
================
This project provides Python bindings for interfacing with the
`Zstandard <http://www.zstd.net>`_ compression library. A C extension
and CFFI interface are provided.

%package license
Summary: license components for the python-zstandard package.
Group: Default

%description license
license components for the python-zstandard package.


%package python
Summary: python components for the python-zstandard package.
Group: Default
Requires: python-zstandard-python3 = %{version}-%{release}

%description python
python components for the python-zstandard package.


%package python3
Summary: python3 components for the python-zstandard package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-zstandard package.


%prep
%setup -q -n python-zstandard-0.11.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557933243
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-zstandard
cp LICENSE %{buildroot}/usr/share/package-licenses/python-zstandard/LICENSE
cp zstd/COPYING %{buildroot}/usr/share/package-licenses/python-zstandard/zstd_COPYING
cp zstd/LICENSE %{buildroot}/usr/share/package-licenses/python-zstandard/zstd_LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-zstandard/LICENSE
/usr/share/package-licenses/python-zstandard/zstd_COPYING
/usr/share/package-licenses/python-zstandard/zstd_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
