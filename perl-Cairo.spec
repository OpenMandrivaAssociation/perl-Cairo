%define upstream_name    Cairo
%define upstream_version 1.070

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Perl module for the Cairo library
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=160888
Source0:    http://prdownloads.sourceforge.net/gtk2-perl/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	cairo-devel
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Test::Number::Delta)
BuildRequires:  perl-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides perl access to the Cairo library.

Cairo provides anti-aliased vector-based rendering for X. Paths
consist of line segments and cubic splines and can be rendered at any
width with various join and cap styles. All colors may be specified
with optional translucence (opacity/alpha) and combined using the
extended Porter/Duff compositing algebra as found in the X Render
Extension.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"
%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc LICENSE examples README NEWS TODO 
%{_mandir}/*/*
%{perl_vendorarch}/%{upstream_name}
%{perl_vendorarch}/%{upstream_name}.pm
%{perl_vendorarch}/auto/*
