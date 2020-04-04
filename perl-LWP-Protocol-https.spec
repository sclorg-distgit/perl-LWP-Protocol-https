%{?scl:%scl_package perl-LWP-Protocol-https}

# Perform tests that need the Internet
%bcond_with perl_LWP_Protocol_https_enables_internet_test

Name:           %{?scl_prefix}perl-LWP-Protocol-https
Version:        6.07
Release:        12%{?dist}
Summary:        Provide HTTPS support for LWP::UserAgent
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/LWP-Protocol-https
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/LWP-Protocol-https-%{version}.tar.gz
# Fix CVE-2014-3230, bug #1094442,
# proposed in https://github.com/libwww-perl/lwp-protocol-https/pull/14
Patch0:         LWP-Protocol-https-6.06-Debian-746576-don-t-disale-verification-if-only-host.patch
# Fix CVE-2014-3230, bug #1094442,
# proposed in https://github.com/libwww-perl/lwp-protocol-https/pull/14
Patch1:         LWP-Protocol-https-6.06-Debian-746576-fix-test-make-it-workable-for-Crypt-SS.patch
BuildArch:      noarch
%if !%{with perl_LWP_Protocol_https_enables_internet_test}
BuildRequires:  coreutils
%endif
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(:VERSION) >= 5.8.1
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(IO::Socket::SSL) >= 1.54
BuildRequires:  %{?scl_prefix}perl(LWP::Protocol::http)
BuildRequires:  %{?scl_prefix}perl(Mozilla::CA) >= 20110101
BuildRequires:  %{?scl_prefix}perl(Net::HTTPS) >= 6
# Tests:
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(IO::Select)
BuildRequires:  %{?scl_prefix}perl(IO::Socket::INET)
BuildRequires:  %{?scl_prefix}perl(LWP::UserAgent) >= 6.06
BuildRequires:  %{?scl_prefix}perl(Socket)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%if %{with perl_LWP_Protocol_https_enables_internet_test}
BuildRequires:  %{?scl_prefix}perl(Test::RequiresInternet)
%endif
BuildRequires:  %{?scl_prefix}perl(warnings)
# Optional tests:
BuildRequires:  %{?scl_prefix}perl(IO::Socket::SSL) >= 1.953
BuildRequires:  %{?scl_prefix}perl(IO::Socket::SSL::Utils)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(IO::Socket::SSL) >= 1.54
Requires:       %{?scl_prefix}perl(Mozilla::CA) >= 20110101
Requires:       %{?scl_prefix}perl(Net::HTTPS) >= 6

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Net::HTTPS\\)\\s*$

%description
The LWP::Protocol::https module provides support for using HTTPS schemed
URLs with LWP. This module is a plug-in to the LWP protocol handling, so
you don't use it directly. Once the module is installed LWP is able to
access sites using HTTP over SSL/TLS.

%prep
%setup -q -n LWP-Protocol-https-%{version}
%patch0 -p1
%patch1 -p1
%if !%{with perl_LWP_Protocol_https_enables_internet_test}
rm t/apache.t
%{?scl:scl enable %{scl} '}perl -i -ne %{?scl:'"}'%{?scl:"'}print $_ unless m{^t/apache.t}%{?scl:'"}'%{?scl:"'} MANIFEST%{?scl:'}
%endif

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor && %{make_build}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}%{make_install}%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Feb 14 2020 Petr Pisar <ppisar@redhat.com> - 6.07-12
- Import to SCL

* Fri Feb 14 2020 Petr Pisar <ppisar@redhat.com> - 6.07-11
- Disable tests that need the Internet by default

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.07-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.07-8
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.07-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 6.07-2
- Perl 5.26 rebuild

* Mon Feb 20 2017 Petr Pisar <ppisar@redhat.com> - 6.07-1
- 6.07 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-5
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Petr Pisar <ppisar@redhat.com> - 6.06-2
- Fix CVE-2014-3230 (incorrect handling of SSL certificate verification if
  HTTPS_CA_DIR or HTTPS_CA_FILE environment variables are set) (bug #1094442)

* Wed Apr 23 2014 Petr Pisar <ppisar@redhat.com> - 6.06-1
- 6.06 bump

* Thu Jan 16 2014 Petr Pisar <ppisar@redhat.com> - 6.04-4
- Modernize spec file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 6.04-2
- Perl 5.18 rebuild

* Thu May 02 2013 Petr Pisar <ppisar@redhat.com> - 6.04-1
- 6.04 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 6.03-2
- Perl 5.16 rebuild

* Mon Feb 20 2012 Petr Pisar <ppisar@redhat.com> - 6.03-1
- 6.03 bump
- Enable tests by default, they detect connectivity now

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 6.02-4
- RPM 4.9 dependency filtering added

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.02-3
- Perl mass rebuild

* Tue Mar 29 2011 Petr Pisar <ppisar@redhat.com> - 6.02-2
- Disable tests because they need network access

* Mon Mar 28 2011 Petr Pisar <ppisar@redhat.com> 6.02-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
