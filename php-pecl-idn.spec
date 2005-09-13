%define		_modname	idn
%define		_status		beta
Summary:	idn - binding to the GNU libidn
Summary(pl):	idn - wi±zanie do GNU libidn
Name:		php-pecl-idn
Version:	0.1
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	ef8635ec22348325a76abd2abddca4a1
URL:		http://pecl.php.net/package/idn/
BuildRequires:	libidn-devel
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-idn
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
Binding to the GNU libidn for using Internationalized Domain Names.

In PECL status of this package is: %{_status}.

%description -l pl
Wi±zanie do GNU libidn do u¿ywania umiêdzynarodowionych nazw domen
(Internationalized Domain Names).

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/CREDITS
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
