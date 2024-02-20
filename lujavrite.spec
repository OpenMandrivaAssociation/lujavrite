%define lua_libdir %{_libdir}/lua/%(rpm -q --qf '%%{VERSION}' %{_lib}lua-devel |cut -d. -f1-2)

Name:           lujavrite
Version:        1.0.2
Release:        1
Summary:        Lua library for calling Java code
License:        Apache-2.0
URL:            https://github.com/mizdebsk/lujavrite
Source0:        https://github.com/mizdebsk/lujavrite/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  lua-devel
BuildRequires:  jdk-current

%{?lua_requires}

%description
LuJavRite is a rock-solid Lua library that allows calling Java code
from Lua code.  It does so by launching embedded Java Virtual Machine
and using JNI interface to invoke Java methods.

%prep
%autosetup -p1

%build
./build.sh

%install
install -D -p -m 0755 lujavrite.so %{buildroot}%{lua_libdir}/%{name}.so

%check
lua test.lua

%files
%{lua_libdir}/*
%license LICENSE NOTICE
%doc README.md
