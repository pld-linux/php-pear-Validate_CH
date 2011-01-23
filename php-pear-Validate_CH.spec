%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Validate_CH
Summary:	%{_pearname} - Validation class for CH
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Szwajcarii
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	2
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c8aa959cab643d8e55798f604f01928f
URL:		http://pear.php.net/package/Validate_CH/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
Requires:	php-pear-Validate >= 0.5.0
Obsoletes:	php-pear-Validate_CH-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for CH such as:
- SSN
- Postal Code
- Student ID

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Szwajcarii danych takich jak:
- numer ubezpieczenia społecznego (SSN)
- kod pocztowy
- numer identyfikacyjny studenta

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/CH.php
%dir %{php_pear_dir}/data/Validate_CH
%{php_pear_dir}/data/Validate_CH/CH_postcodes.txt
