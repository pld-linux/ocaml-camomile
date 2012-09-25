# $Revision: 1.5 $, $Date: 2011/07/23 06:35:45 $
Summary:	Camomile - comprehensive Unicode library for OCaml
Summary(pl.UTF-8):	Camomile - obszerna biblioteka unikodowa dla OCamla
Name:		ocaml-camomile
Version:	0.8.3
Release:	1
License:	LGPL v2+ with linking exception
Group:		Libraries
Source0:	http://downloads.sourceforge.net/camomile/camomile-%{version}.tar.bz2
# Source0-md5:	c6476bdb4138d222bc14396a82205034
URL:		http://camomile.sourceforge.net/
BuildRequires:	ocaml >= 3.04-7
BuildRequires:	ocaml-camlp4
BuildRequires:	ocaml-findlib
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Camomile is a comprehensive Unicode library for OCaml. Camomile
provides Unicode character type, UTF-8, UTF-16, UTF-32 strings,
conversion to/from about 200 encodings, collation and locale-sensitive
case mappings, and more.

This package contains database files needed to run executables using
Camomile library.

%description -l pl.UTF-8
Camomilw to obszerna biblioteka unikodowa dla OCamla. Camomile
udostępnia typ znaku unikodowego, łańcuchy UTF-8, UTF-16, UTF-32,
konwersję z/do około 200 kodowań, tablice sortowania oraz wielkości
liter zależne od lokalizacji itd.

Ten pakiet zawiera pliki baz danych potrzebne do uruchamiania
programów wykorzystujących bibliotekę Camomile.

%package devel
Summary:	Camomile Unicode library for OCaml - development part
Summary(pl.UTF-8):	Biblioteka unikodowa Camomile dla OCamla - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
Camomile library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
biblioteki Camomile.

%prep
%setup -q -n camomile-%{version}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/camomile

%{__make} install \
	OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml \
	DATADIR=$RPM_BUILD_ROOT%{_datadir}

mv $RPM_BUILD_ROOT%{_libdir}/ocaml/camomile/META $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/camomile
cat >> $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/camomile/META <<EOF
directory = "+camomile"
EOF

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/camomile/camomileLibrary*.mli

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{_datadir}/camomile

%files devel
%defattr(644,root,root,755)
%doc camomileLibrary*.mli
%dir %{_libdir}/ocaml/camomile
%{_libdir}/ocaml/camomile/camomile.a
%{_libdir}/ocaml/camomile/camomile.cm[ax]*
%{_libdir}/ocaml/camomile/camomileLibrary*.cm[ixa]*
%{_libdir}/ocaml/site-lib/camomile
