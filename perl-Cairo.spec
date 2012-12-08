%define upstream_name    Cairo
%define upstream_version 1.070

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    8

Summary:	Perl module for the Cairo library
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=160888
Source0:    http://prdownloads.sourceforge.net/gtk2-perl/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	pkgconfig(cairo)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Test::Number::Delta)
BuildRequires:  perl-devel

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
%make OPTIMIZE="%{optflags}"
%make test || :

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%doc LICENSE examples README NEWS TODO 
%{_mandir}/*/*
%{perl_vendorarch}/%{upstream_name}
%{perl_vendorarch}/%{upstream_name}.pm
%{perl_vendorarch}/auto/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.70.0-7mdv2012.0
+ Revision: 765078
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.70.0-6
+ Revision: 763494
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.70.0-5
+ Revision: 667038
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.70.0-4mdv2011.0
+ Revision: 564384
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.70.0-3mdv2011.0
+ Revision: 555262
- rebuild

* Tue Jul 20 2010 Thierry Vignaud <tv@mandriva.org> 1.70.0-2mdv2011.0
+ Revision: 555172
- adjust filelist
- new release

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.61.0-2mdv2010.1
+ Revision: 504938
- rebuild using %%perl_convert_version

* Mon May 04 2009 Thierry Vignaud <tv@mandriva.org> 1.061-1mdv2010.0
+ Revision: 371799
- new release

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.060-2mdv2009.1
+ Revision: 351681
- rebuild

* Mon Jun 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.060-1mdv2009.0
+ Revision: 227965
- update to new version 1.060

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.053-2mdv2009.0
+ Revision: 223570
- rebuild

* Mon Feb 25 2008 Thierry Vignaud <tv@mandriva.org> 1.053-1mdv2008.1
+ Revision: 174751
- new release

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 1.052-1mdv2008.1
+ Revision: 166532
- new release

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.050-2mdv2008.1
+ Revision: 151275
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 22 2007 Thierry Vignaud <tv@mandriva.org> 1.050-1mdv2008.1
+ Revision: 111323
- new release

* Mon Oct 15 2007 Thierry Vignaud <tv@mandriva.org> 1.043-1mdv2008.1
+ Revision: 98517
- new release

* Wed Oct 10 2007 Thierry Vignaud <tv@mandriva.org> 1.042-1mdv2008.1
+ Revision: 96737
- BuildRequires perl-Test-Number-Delta
- new release

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 1.041-2mdv2008.0
+ Revision: 36190
- rebuild with correct optflags

* Tue Jun 05 2007 Thierry Vignaud <tv@mandriva.org> 1.041-1mdv2008.0
+ Revision: 35871
- new release

* Mon May 14 2007 Thierry Vignaud <tv@mandriva.org> 1.040-1mdv2008.0
+ Revision: 26721
- new release


* Tue Feb 27 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.023-1mdv2007.0
+ Revision: 126582
- new release

* Thu Jan 04 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.022-1mdv2007.1
+ Revision: 104209
- new release

* Thu Nov 23 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.021-1mdv2007.1
+ Revision: 86821
- new release

* Wed Oct 18 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.01-1mdv2007.1
+ Revision: 65974
- new release
- Import perl-Cairo

* Wed Sep 06 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.00-1mdv2007.0
- new release

* Thu Aug 17 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.92-1mdv2007.0
- new release

* Wed Jul 26 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.90-1mdv2007.0
- new release

* Sat Jun 24 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.04-1mdv2007.0
- new release

* Tue Jan 31 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.03-1mdk
- new release

* Fri Sep 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.02-1mdk
- 0.02
- Build and spec fixes, change group, enable "make test"

* Thu Aug 18 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.01-1mdk
- initial release

