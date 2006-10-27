Summary:	fax2png - 1-bit multipage TIFF (fax or scan) to PNG image converter
Summary(pl):	fax2png - konwerter 1-bitowych, wielostronnych obrazów TIFF (faksów lub skanów) do PNG
Name:		fax2png
Version:	1.0
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://www.boutell.com/fax2png/%{name}.tar.gz
# Source0-md5:	c7af8429ae707ee4fc9b461f059d9887
URL:		http://www.boutell.com/fax2png/
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extracts a specified page from a 1-bit black and white TIFF image,
such as a fax, and efficiently converts it to PNG format without the
performance overhead of netpbm-based solutions. Antialiasing is
supported to produce attractive reductions to typical web browser
widths. 90-degree-interval rotations and flips are also supported.

%description -l pl
fax2png wyci±ga podan± stronê z 1-bitowego, czarno-bia³ego obrazu TIFF
(jak fax) i wydajnie konwertuje go do formatu PNG bez wydajno¶ciowego
narzutu jak w przypadku u¿ycia netpbm. Obs³ugiwany jest antyaliasing w
celu tworzenia ³adniejszych pomniejszeñ do rozdzielczo¶ci typowych dla
przegl±darki WWW. Obs³ugiwane s± tak¿e obroty co 90 stopni.

%prep
%setup -q -n %{name}

%build
%{__cc} %{rpmldflags} %{rpmcflags} -o fax2png fax2png.c -lpng -ltiff

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install fax2png $RPM_BUILD_ROOT%{_bindir}
install fax2png.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt fax2png.pl
%attr(755,root,root) %{_bindir}/fax2png
%{_mandir}/man1/fax2png.1*
