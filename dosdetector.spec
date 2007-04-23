Summary:	Suspicious network traffic analyser and detector
Summary(pl.UTF-8):	Analizator i wykrywacz podejrzanego ruchu sieciowego
Name:		dosdetector
Version:	20060621
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://darkzone.ma.cx/resources/unix/dosdetector/%{name}-%{version}.tar.gz
# Source0-md5:	b2230048725657dbc7fde290c2fdfa08
Patch0:		%{name}-ncurses.patch
URL:		http://darkzone.ma.cx/resources/unix/dosdetector/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libcap-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DoSDetector analyses and detects most of suspicious traffic from IP
and alerts about it. It can detect worm traffic, SYN flood, ICMP
flood, UDP flood etc... It's configurable via a set of rules which
have some points assigned to IP according to a matching rule. When the
point limit for a given IP is exceeded, DoSDetector prints warning.

%description -l pl.UTF-8
DoSDetector analizuje i wykrywa większość podejrzanego ruchu
sieciowego i informuje o tym. Potrafi wykryć ruch powodowany przez
robaki, SYN flood, ICMP flood, UDP flood itp... Jest konfigurowalny
przez zestaw zasad które dopisują punkty do IP zgodnie z pasującą
regułą. Kiedy limit punktów dla danego IP zostanie przekroczony,
DoSDetector wyświetla ostrzeżenie. Program jest użyteczny do
zbudowania sieciowego systemu antywirusowego.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CFLAGS="$CFLAGS -DHAVE_LIBNCURSES_NCURSES"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/dosdetector
%{_mandir}/man1/dosdetector*
