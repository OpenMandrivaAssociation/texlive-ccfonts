# revision 17122
# category Package
# catalog-ctan /macros/latex/contrib/ccfonts
# catalog-date 2010-02-21 01:29:55 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-ccfonts
Version:	1.1
Release:	10
Summary:	Support for Concrete text and math fonts in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ccfonts
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccfonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccfonts.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccfonts.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%define		_unpackaged_subdirs_terminate_build	0

%description
LaTeX font definition files for the Concrete fonts and a LaTeX
package for typesetting documents using Concrete as the default
font family. The files support OT1, T1, TS1, and Concrete
mathematics including AMS fonts (Ulrik Vieth's concmath).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ccfonts/ccfonts.sty
%{_texmfdistdir}/tex/latex/ccfonts/t1ccr.fd
%{_texmfdistdir}/tex/latex/ccfonts/ts1ccr.fd
%doc %{_texmfdistdir}/doc/latex/ccfonts/ccfonts.pdf
%doc %{_texmfdistdir}/doc/latex/ccfonts/readme
#- source
%doc %{_texmfdistdir}/source/latex/ccfonts/cc.fdd
%doc %{_texmfdistdir}/source/latex/ccfonts/ccfonts.dtx
%doc %{_texmfdistdir}/source/latex/ccfonts/ccfonts.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 750146
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718018
- texlive-ccfonts
- texlive-ccfonts
- texlive-ccfonts
- texlive-ccfonts
- texlive-ccfonts

