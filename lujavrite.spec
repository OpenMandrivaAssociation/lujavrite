%define lua_libdir %{_libdir}/lua/%(rpm -q --qf '%%{VERSION}' %{_lib}lua-devel |cut -d. -f1-2)

Name:           lujavrite
Version:        1.2.3
Release:        1
Summary:        Lua library for calling Java code
License:        Apache-2.0
URL:            https://github.com/mizdebsk/lujavrite
Source0:        https://github.com/mizdebsk/lujavrite/releases/download/%{version}/lujavrite-%{version}.tar.zst

BuildRequires:  cmake
BuildRequires:  java-current-devel
BuildRequires:  java-gui-current
BuildRequires:  lua-devel

BuildSystem:  cmake

%{?lua_requires}

%description
LuJavRite is a rock-solid Lua library that allows calling Java code
from Lua code.  It does so by launching embedded Java Virtual Machine
and using JNI interface to invoke Java methods.

%prep
%autosetup -p1 -C

%files
%{lua_libdir}/*
%license LICENSE NOTICE
%doc README.md
