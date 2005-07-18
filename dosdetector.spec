Summary:	Suspicious network traffic analyser and detector
Summary(pl):	Analizator i wykrywacz podejrzanego ruchu sieciowego
Name:		dosdetector
Version:	20050711
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://darkzone.ma.cx/resources/unix/dosdetector/%{name}-%{version}.tar.gz
# Source0-md5:	4a2771a1dcaf19d4e6a969710b7a1c1f
Patch0:		%{name}-ncurses.patch
URL:		http://darkzone.ma.cx/resources/unix/dosdetector/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libcap-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DoSDetector analyses and detects most of suspicious traffic from IP
and alerts about it. It can detect worm traffic, SYN flood, icmp
flood, udp flood etc... It's configurable via a set of rules which
have some points assigned to IP according to a matching rule. When the
point limit for a given IP is exceeded, DoSDetector prints warning.

%description -l pl
DoSDetector analizuje i wykrywa wiêkszo¶æ podejrzanego ruchu
sieciowego i informuje o tym. Potrafi wykryæ ruch powodowany przez
robaki, SYN flood, icmp flood, udp flood itp... Jest konfigurowalny
przez zestaw zasad które dopisuj± punkty do IP zgodnie z pasuj±c±
regu³±. Kiedy limit punktów dla danego IP zostanie przekroczony,
DoSDetector wy¶wietla ostrze¿enie. Program jest u¿yteczny do
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
