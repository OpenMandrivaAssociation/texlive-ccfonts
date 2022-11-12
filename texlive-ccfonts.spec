Name:		texlive-ccfonts
Version:	61431
Release:	1
Summary:	Support for Concrete text and math fonts in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ccfonts
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccfonts.r61431.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccfonts.doc.r61431.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccfonts.source.r61431.tar.xz
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
%{_texmfdistdir}/tex/latex/ccfonts
%doc %{_texmfdistdir}/doc/latex/ccfonts
#- source
%doc %{_texmfdistdir}/source/latex/ccfonts

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
