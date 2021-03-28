#
# Conditional build:
%bcond_without	ocaml_opt	# skip building native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Camomile - comprehensive Unicode library for OCaml
Summary(pl.UTF-8):	Camomile - obszerna biblioteka unikodowa dla OCamla
Name:		ocaml-camomile
Version:	1.0.2
Release:	0.1
License:	LGPL v2+ with linking exception
Group:		Libraries
Source0:	https://github.com/yoriyuki/Camomile/releases/download/%{version}/camomile-%{version}.tbz
# Source0-md5:	1a193d43a112bf69eba1bc581d7f4a77
URL:		https://github.com/yoriyuki/Camomile
BuildRequires:	ocaml >= 1:4.02.3
BuildRequires:	ocaml-camlp4
BuildRequires:	ocaml-dune
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{without ocaml_opt}
%define		no_install_post_strip	1
# no opt means no native binary, stripping bytecode breaks such programs
%define		_enable_debug_packages	0
%endif

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
dune build --verbose --profile release

%install
rm -rf $RPM_BUILD_ROOT

dune install \
	--verbose \
	--destdir $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md README.md
%{_datadir}/camomile

%files devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/camomile
%{_libdir}/ocaml/camomile/META
%if %{with ocaml_opt}
%{_libdir}/ocaml/camomile/*.a
%{_libdir}/ocaml/camomile/*.cmx
%{_libdir}/ocaml/camomile/*.cmxa
%endif
%{_libdir}/ocaml/camomile/*.cma
%{_libdir}/ocaml/camomile/*.cmi
