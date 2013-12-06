# revision 23454
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-srbook-mem
Version:	20111104
Release:	6
Summary:	TeXLive srbook-mem package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srbook-mem.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srbook-mem.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 756162
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719572
- texlive-srbook-mem
- texlive-srbook-mem
- texlive-srbook-mem
- texlive-srbook-mem

