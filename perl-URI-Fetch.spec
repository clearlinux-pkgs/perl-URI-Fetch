#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-URI-Fetch
Version  : 0.13
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/URI-Fetch-0.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/URI-Fetch-0.13.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-feed-perl/libxml-feed-perl_0.53+dfsg-1.debian.tar.xz
Summary  : 'Smart URI fetching/caching'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-URI-Fetch-license = %{version}-%{release}
Requires: perl-URI-Fetch-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::ErrorHandler)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(LWP::UserAgent)
BuildRequires : perl(Test::RequiresInternet)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(URI)

%description
This archive contains the distribution URI-Fetch,
version 0.13:
Smart URI fetching/caching

%package dev
Summary: dev components for the perl-URI-Fetch package.
Group: Development
Provides: perl-URI-Fetch-devel = %{version}-%{release}
Requires: perl-URI-Fetch = %{version}-%{release}

%description dev
dev components for the perl-URI-Fetch package.


%package license
Summary: license components for the perl-URI-Fetch package.
Group: Default

%description license
license components for the perl-URI-Fetch package.


%package perl
Summary: perl components for the perl-URI-Fetch package.
Group: Default
Requires: perl-URI-Fetch = %{version}-%{release}

%description perl
perl components for the perl-URI-Fetch package.


%prep
%setup -q -n URI-Fetch-0.13
cd %{_builddir}
tar xf %{_sourcedir}/libxml-feed-perl_0.53+dfsg-1.debian.tar.xz
cd %{_builddir}/URI-Fetch-0.13
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/URI-Fetch-0.13/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-URI-Fetch
cp %{_builddir}/URI-Fetch-0.13/LICENSE %{buildroot}/usr/share/package-licenses/perl-URI-Fetch/f2fe11061bb602ab496f54bf497747f9f93f4c15
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-URI-Fetch/808cdef4c992763637fe5a5a7551c6cd5186080b
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/URI::Fetch.3
/usr/share/man/man3/URI::Fetch::Response.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-URI-Fetch/808cdef4c992763637fe5a5a7551c6cd5186080b
/usr/share/package-licenses/perl-URI-Fetch/f2fe11061bb602ab496f54bf497747f9f93f4c15

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/URI/Fetch.pm
/usr/lib/perl5/vendor_perl/5.30.2/URI/Fetch/Response.pm
