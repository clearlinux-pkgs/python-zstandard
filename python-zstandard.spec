#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-zstandard
Version  : 0.14.1
Release  : 21
URL      : https://github.com/indygreg/python-zstandard/archive/0.14.1/python-zstandard-0.14.1.tar.gz
Source0  : https://github.com/indygreg/python-zstandard/archive/0.14.1/python-zstandard-0.14.1.tar.gz
Summary  : Zstandard bindings for Python
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: python-zstandard-license = %{version}-%{release}
Requires: python-zstandard-python = %{version}-%{release}
Requires: python-zstandard-python3 = %{version}-%{release}
Requires: apipkg
Requires: atomicwrites
Requires: attrs
Requires: cffi
Requires: colorama
Requires: contextlib2
Requires: execnet
Requires: filelock
Requires: funcsigs
Requires: more-itertools
Requires: packaging
Requires: pathlib2
Requires: pycparser
Requires: pyparsing
Requires: six
Requires: sortedcontainers
Requires: toml
Requires: wcwidth
Requires: zipp
BuildRequires : apipkg
BuildRequires : atomicwrites
BuildRequires : attrs
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : colorama
BuildRequires : contextlib2
BuildRequires : execnet
BuildRequires : filelock
BuildRequires : funcsigs
BuildRequires : hypothesis
BuildRequires : hypothesis-python
BuildRequires : more-itertools
BuildRequires : packaging
BuildRequires : pathlib2
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pycparser
BuildRequires : pyparsing
BuildRequires : pytest
BuildRequires : six
BuildRequires : sortedcontainers
BuildRequires : toml
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : wcwidth
BuildRequires : zipp

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
Provides: pypi(zstandard)

%description python3
python3 components for the python-zstandard package.


%prep
%setup -q -n python-zstandard-0.14.1
cd %{_builddir}/python-zstandard-0.14.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607360706
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-zstandard
cp %{_builddir}/python-zstandard-0.14.1/LICENSE %{buildroot}/usr/share/package-licenses/python-zstandard/bdfd20ae0e3f88b5609da6191fbb89f33933d948
cp %{_builddir}/python-zstandard-0.14.1/zstd/COPYING %{buildroot}/usr/share/package-licenses/python-zstandard/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
cp %{_builddir}/python-zstandard-0.14.1/zstd/LICENSE %{buildroot}/usr/share/package-licenses/python-zstandard/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-zstandard/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
/usr/share/package-licenses/python-zstandard/bdfd20ae0e3f88b5609da6191fbb89f33933d948
/usr/share/package-licenses/python-zstandard/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
