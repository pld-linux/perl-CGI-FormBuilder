#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	FormBuilder
Summary:	CGI::FormBuilder - easily generate and process stateful forms
Summary(pl):	CGI::FormBuilder - ³atwe generowanie i przetwarzanie formularzy z obs³ug± stanów
Name:		perl-CGI-FormBuilder
Version:	3.0202
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a1df4a31dda8573d40902f4e7d2b059d
BuildRequires:	perl-CGI
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of CGI::FormBuilder (FormBuilder) is to provide an easy way
for you to generate and process CGI form-based applications. This
module is designed to be smart in that it figures a lot of stuff out
for you. As a result, FormBuilder gives you about a 4:1 ratio of the
code it generates versus what you have to write.

%description -l pl
Celem modu³u CGI::FormBuilder (FormBuildera) jest dostarczenie ³atwego
sposobu generowania i przetwarzania aplikacji CGI opartych na
formularzach. Ten modu³ jest zaprojektowany tak, aby inteligentnie
wykrywa³ wiêkszo¶æ rzeczy za programistê. W efekcie FormBuilder daje
wspó³czynnik kodu generowanego do tego, który trzeba napisaæ oko³o
4:1.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/FormBuilder.pm
%dir %{perl_vendorlib}/CGI/FormBuilder
%{perl_vendorlib}/CGI/FormBuilder/*.pm
%dir %{perl_vendorlib}/CGI/FormBuilder/Template
%{perl_vendorlib}/CGI/FormBuilder/Template/*.pm
%dir %{perl_vendorlib}/CGI/FormBuilder/Source
%{perl_vendorlib}/CGI/FormBuilder/Source/File.pm
%{_mandir}/man3/*
