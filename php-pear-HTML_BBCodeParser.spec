%define		_class		HTML
%define		_subclass	BBCodeParser
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.2.2
Release:	10
Summary:	Parser to replace UBB style tags with their HTML equivalents
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_BBCodeParser/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This is a parser to replace UBB style tags with their HTML
equivalents. It does not simply do some regex calls, but is complete
stack based parse engine. This ensures that all tags are properly
nested, if not, extra tags are added to maintain the nesting. This
parser should only produce XHTML 1.0 compliant code. All tags are
validated and so are all their attributes. It should be easy to extend
this parser with your own tags.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/%{_subclass}/example
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-8mdv2012.0
+ Revision: 741989
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-7
+ Revision: 679340
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-6mdv2011.0
+ Revision: 613667
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.2-5mdv2010.1
+ Revision: 477859
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Fri Oct 02 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-4mdv2010.0
+ Revision: 452658
- fix #54217 (php-pear-HTML_BBCodeParser unresolved dependency)

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.2.2-3mdv2010.0
+ Revision: 441111
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-2mdv2009.1
+ Revision: 322084
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.2-1mdv2009.0
+ Revision: 278917
- update to new version 1.2.2

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1-9mdv2009.0
+ Revision: 236849
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Nov 12 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1-8mdv2007.0
+ Revision: 83318
- rebuild

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1-7mdv2007.1
+ Revision: 81605
- Import php-pear-HTML_BBCodeParser

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdk
- initial Mandriva package (PLD import)

