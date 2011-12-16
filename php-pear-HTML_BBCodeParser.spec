%define		_class		HTML
%define		_subclass	BBCodeParser
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.2.2
Release:	%mkrel 8
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
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/%{_subclass}/example
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
