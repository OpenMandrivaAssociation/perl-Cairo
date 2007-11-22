%define module Cairo

Summary:	Perl module for the Cairo library
Name:		perl-%module
Version:	1.050
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=160888
Source:		http://prdownloads.sourceforge.net/gtk2-perl/%module-%version.tar.bz2
URL:		http://gtk2-perl.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	cairo-devel perl-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig
BuildRequires:	perl-Test-Number-Delta

%description
This module provides perl access to the Cairo library.

Cairo provides anti-aliased vector-based rendering for X. Paths
consist of line segments and cubic splines and can be rendered at any
width with various join and cap styles. All colors may be specified
with optional translucence (opacity/alpha) and combined using the
extended Porter/Duff compositing algebra as found in the X Render
Extension.

%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} OPTIMIZE="$RPM_OPT_FLAGS"
%{__make} test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc LICENSE examples README NEWS TODO ChangeLog
%{_mandir}/*/*
%{perl_vendorarch}/%module
%{perl_vendorarch}/%module.pm
%{perl_vendorarch}/auto/*


