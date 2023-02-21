#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-zstandard
Version  : 0.20.0
Release  : 35
URL      : https://github.com/indygreg/python-zstandard/archive/0.20.0/python-zstandard-0.20.0.tar.gz
Source0  : https://github.com/indygreg/python-zstandard/archive/0.20.0/python-zstandard-0.20.0.tar.gz
Summary  : Zstandard bindings for Python
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: python-zstandard-filemap = %{version}-%{release}
Requires: python-zstandard-lib = %{version}-%{release}
Requires: python-zstandard-license = %{version}-%{release}
Requires: python-zstandard-python = %{version}-%{release}
Requires: python-zstandard-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(atomicwrites)
BuildRequires : pypi(attrs)
BuildRequires : pypi(bashlex)
BuildRequires : pypi(bracex)
BuildRequires : pypi(certifi)
BuildRequires : pypi(cffi)
BuildRequires : pypi(cibuildwheel)
BuildRequires : pypi(colorama)
BuildRequires : pypi(exceptiongroup)
BuildRequires : pypi(execnet)
BuildRequires : pypi(filelock)
BuildRequires : pypi(hypothesis)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(iniconfig)
BuildRequires : pypi(mypy)
BuildRequires : pypi(mypy_extensions)
BuildRequires : pypi(packaging)
BuildRequires : pypi(platformdirs)
BuildRequires : pypi(pluggy)
BuildRequires : pypi(pycparser)
BuildRequires : pypi(sortedcontainers)
BuildRequires : pypi(tomli)
BuildRequires : pypi(typed_ast)
BuildRequires : pypi(typing_extensions)
BuildRequires : pypi(wheel)
BuildRequires : pypi(zipp)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
================
python-zstandard
================
| |ci-test| |ci-wheel| |ci-typing| |ci-sdist| |ci-anaconda| |ci-sphinx|

%package filemap
Summary: filemap components for the python-zstandard package.
Group: Default

%description filemap
filemap components for the python-zstandard package.


%package lib
Summary: lib components for the python-zstandard package.
Group: Libraries
Requires: python-zstandard-license = %{version}-%{release}
Requires: python-zstandard-filemap = %{version}-%{release}

%description lib
lib components for the python-zstandard package.


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
Requires: python-zstandard-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(zstandard)
Requires: pypi(atomicwrites)
Requires: pypi(attrs)
Requires: pypi(bashlex)
Requires: pypi(bracex)
Requires: pypi(certifi)
Requires: pypi(cffi)
Requires: pypi(cibuildwheel)
Requires: pypi(colorama)
Requires: pypi(exceptiongroup)
Requires: pypi(execnet)
Requires: pypi(filelock)
Requires: pypi(hypothesis)
Requires: pypi(importlib_metadata)
Requires: pypi(iniconfig)
Requires: pypi(mypy)
Requires: pypi(mypy_extensions)
Requires: pypi(packaging)
Requires: pypi(platformdirs)
Requires: pypi(pluggy)
Requires: pypi(pycparser)
Requires: pypi(sortedcontainers)
Requires: pypi(tomli)
Requires: pypi(typed_ast)
Requires: pypi(typing_extensions)
Requires: pypi(wheel)
Requires: pypi(zipp)

%description python3
python3 components for the python-zstandard package.


%prep
%setup -q -n python-zstandard-0.20.0
cd %{_builddir}/python-zstandard-0.20.0
pushd ..
cp -a python-zstandard-0.20.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676999638
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-zstandard
cp %{_builddir}/python-zstandard-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/python-zstandard/bdfd20ae0e3f88b5609da6191fbb89f33933d948 || :
cp %{_builddir}/python-zstandard-%{version}/zstd/COPYING %{buildroot}/usr/share/package-licenses/python-zstandard/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8 || :
cp %{_builddir}/python-zstandard-%{version}/zstd/LICENSE %{buildroot}/usr/share/package-licenses/python-zstandard/d5e630eee1d3500039f2e16bed21d0f0cd580994 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-python-zstandard

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-zstandard/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
/usr/share/package-licenses/python-zstandard/bdfd20ae0e3f88b5609da6191fbb89f33933d948
/usr/share/package-licenses/python-zstandard/d5e630eee1d3500039f2e16bed21d0f0cd580994

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
