%define		php_name	php%{?php_suffix}
%define		modname	idn
%define		status	beta
Summary:	%{modname} - binding to the GNU libidn
Summary(pl.UTF-8):	%{modname} - wiązanie do GNU libidn
Name:		%{php_name}-pecl-idn
Version:	0.2.0
Release:	2
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	f42dadf9b15bfc897458ff8735f05f78
URL:		http://pecl.php.net/package/idn/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	libidn-devel
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Binding to the GNU libidn for using Internationalized Domain Names.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
Wiązanie do GNU libidn do używania umiędzynarodowionych nazw domen
(Internationalized Domain Names).

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d

%{__make} install \
	EXTENSION_DIR=%{php_extensiondir} \
	INSTALL_ROOT=$RPM_BUILD_ROOT
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
