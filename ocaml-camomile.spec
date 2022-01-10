#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		_enable_debug_packages	0

Summary:	Camomile - comprehensive Unicode library for OCaml
Summary(pl.UTF-8):	Camomile - obszerna biblioteka unikodowa dla OCamla
Name:		ocaml-camomile
Version:	1.0.2
Release:	1
License:	LGPL v2+ with linking exception
Group:		Libraries
#Source0Download: https://github.com/yoriyuki/Camomile/releases
Source0:	https://github.com/yoriyuki/Camomile/releases/download/%{version}/camomile-%{version}.tbz
# Source0-md5:	1a193d43a112bf69eba1bc581d7f4a77
URL:		https://github.com/yoriyuki/Camomile
BuildRequires:	ocaml >= 1:4.02.3
BuildRequires:	ocaml-dune >= 1.11
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
Summary(pl.UTF-8):	Biblioteka unikodowa Camomile dla OCamla - część programistyczna
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

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/camomile{,/default_config,/dyn,/lib_default,/library}/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/camomile

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md README.md
%dir %{_libdir}/ocaml/camomile
%{_libdir}/ocaml/camomile/META
%dir %{_libdir}/ocaml/camomile/default_config
%dir %{_libdir}/ocaml/camomile/dyn
%dir %{_libdir}/ocaml/camomile/lib_default
%dir %{_libdir}/ocaml/camomile/library
%{_libdir}/ocaml/camomile/*.cma
%{_libdir}/ocaml/camomile/default_config/*.cma
%{_libdir}/ocaml/camomile/dyn/*.cma
%{_libdir}/ocaml/camomile/lib_default/*.cma
%{_libdir}/ocaml/camomile/library/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/camomile/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/camomile/default_config/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/camomile/dyn/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/camomile/lib_default/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/camomile/library/*.cmxs
%endif
%{_datadir}/camomile

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/camomile/*.cmi
%{_libdir}/ocaml/camomile/*.cmt
%{_libdir}/ocaml/camomile/dune-package
%{_libdir}/ocaml/camomile/opam
%{_libdir}/ocaml/camomile/default_config/*.cmi
%{_libdir}/ocaml/camomile/default_config/*.cmt
%{_libdir}/ocaml/camomile/dyn/*.cmi
%{_libdir}/ocaml/camomile/dyn/*.cmt
%{_libdir}/ocaml/camomile/lib_default/*.cmi
%{_libdir}/ocaml/camomile/lib_default/*.cmt
%{_libdir}/ocaml/camomile/library/*.cmi
%{_libdir}/ocaml/camomile/library/*.cmt
%{_libdir}/ocaml/camomile/library/*.cmti
%{_libdir}/ocaml/camomile/library/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/camomile/*.a
%{_libdir}/ocaml/camomile/*.cmx
%{_libdir}/ocaml/camomile/*.cmxa
%{_libdir}/ocaml/camomile/default_config/*.a
%{_libdir}/ocaml/camomile/default_config/*.cmx
%{_libdir}/ocaml/camomile/default_config/*.cmxa
%{_libdir}/ocaml/camomile/dyn/*.a
%{_libdir}/ocaml/camomile/dyn/*.cmx
%{_libdir}/ocaml/camomile/dyn/*.cmxa
%{_libdir}/ocaml/camomile/lib_default/*.a
%{_libdir}/ocaml/camomile/lib_default/*.cmx
%{_libdir}/ocaml/camomile/lib_default/*.cmxa
%{_libdir}/ocaml/camomile/library/*.a
%{_libdir}/ocaml/camomile/library/*.cmx
%{_libdir}/ocaml/camomile/library/*.cmxa
%endif
