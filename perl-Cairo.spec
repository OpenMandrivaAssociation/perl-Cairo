%define	modname	Cairo
%define modver 1.106

Summary:	Perl module for the Cairo library

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=160888
Source0:	http://sourceforge.net/projects/gtk2-perl/files/%{modname}/%{modver}/%{modname}-%{modver}.tar.gz
Source100:	%{name}.rpmlintrc
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Test::Number::Delta)
BuildRequires:	pkgconfig(cairo)

%description
This module provides perl access to the Cairo library.

Cairo provides anti-aliased vector-based rendering for X. Paths
consist of line segments and cubic splines and can be rendered at any
width with various join and cap styles. All colors may be specified
with optional translucence (opacity/alpha) and combined using the
extended Porter/Duff compositing algebra as found in the X Render
Extension.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test || :

%install
%makeinstall_std

%files
%doc LICENSE examples README NEWS TODO
%{perl_vendorarch}/%{modname}
%{perl_vendorarch}/%{modname}.pm
%{perl_vendorarch}/auto/*
%{_mandir}/man3/*
