%define upstream_name    Role-Identifiable
Name:		perl-%{upstream_name}
Version:	0.009
Release:	1

Summary:	A thing with an ident attribute
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Role/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Role)
BuildRequires:	perl(Moose::Util::TypeConstraints)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This is an incredibly simple role. It adds a required 'ident' attribute
that stores a simple string, meant to identify exceptions.

%prep
%setup -q -n Role-Identifiable-0.009

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.5.0-2mdv2011.0
+ Revision: 657466
- rebuild for updated spec-helper

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-1
+ Revision: 639036
- import perl-Role-Identifiable

