Summary:	safecat: Write Data Safely to a Directory
Summary(pl.UTF-8):   safecat - bezpieczny zapis danych do katalogu
Name:		safecat
Version:	1.13
Release:	1
License:	BSD
Group:		Applications/File
Source0:	http://jeenyus.net/~budney/linux/software/safecat/%{name}-%{version}.tar.gz
# Source0-md5:	41f76b6c8c47f467556651855ea027a7
Patch0:		%{name}.patch
URL:		http://jeenyus.net/~budney/linux/software/safecat.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
safecat implements Dan Bernstein's maildir algorithm, copying standard
input safely to a specified directory. With safecat, the user is
offered two assurances. First, if safecat returns successfully, then
all data is guaranteed to be saved in the destination directory.
Second, if a file exists in the destination directory, placed there by
safecat, then the file is guaranteed to be complete.

%description -l pl.UTF-8
safecat implementuje algorytm maildir Dana Bernsteina kopiując
bezpiecznie dane ze standardowego wejścia do podanego katalogu.
Używając safecata użytkownik może być pewien dwóch rzeczy. Po
pierwsze, jeśli safecat zakończy działanie z sukcesem, gwarantowane
jest, że wszystkie dane zostały zapisane w katalogu docelowym. Po
drugie, jeśli plik został umieszczony w katalogu docelowym przez
safecata, gwarantowane jest, że plik jest kompletny.

%prep
%setup -q
%patch0 -p1

%build
echo '%{__cc} %{rpmcflags} -D_LARGEFILE64_SOURCE' > conf-cc
echo '%{__cc}' > conf-ld
echo '%{_prefix}' > conf-root
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} setup \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/maildir
%attr(755,root,root) %{_bindir}/safecat
%{_mandir}/man1/maildir.1*
%{_mandir}/man1/safecat.1*
