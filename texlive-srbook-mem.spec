Name:		texlive-srbook-mem
Version:	45818
Release:	1
Summary:	TeXLive srbook-mem package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srbook-mem.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srbook-mem.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive srbook-mem package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/srbook-mem/srbook-mem.sty
%doc %{_texmfdistdir}/doc/latex/srbook-mem/README
%doc %{_texmfdistdir}/doc/latex/srbook-mem/SerbianBookMem.pdf
%doc %{_texmfdistdir}/doc/latex/srbook-mem/SerbianBookMem.tex
%doc %{_texmfdistdir}/doc/latex/srbook-mem/Test.pdf
%doc %{_texmfdistdir}/doc/latex/srbook-mem/Test.tex
%doc %{_texmfdistdir}/doc/latex/srbook-mem/TestLight.pdf
%doc %{_texmfdistdir}/doc/latex/srbook-mem/TestLight.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
