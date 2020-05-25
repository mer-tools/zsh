Name:       zsh
Summary:    The Z shell
Version:    0
Release:    1
Group:      Applications/System
License:    MIT
URL:        https://github.com/mer-tools/zsh
Source0:    zsh-%{version}.tar.bz2
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  libcap-devel
BuildRequires:  texinfo
BuildRequires:  autoconf

%description
Zsh is a shell designed for interactive use, although
it is also a powerful scripting language. Many of the
useful features of bash, ksh, and tcsh were incorporated
into zsh; many original features were added.


%prep
%setup -q -n %{name}-%{version}

%build
autoreconf

%configure --disable-static \
    --with-tcsetpgrp

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_datadir}/zsh/5.0.2/scripts/*
%{_datadir}/zsh/5.0.2/functions/*
%{_libdir}/zsh/5.0.2/zsh/*.so
%{_libdir}/zsh/5.0.2/zsh/net/*.so
%{_bindir}/zsh*
