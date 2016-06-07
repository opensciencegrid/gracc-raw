FILES=gracc-raw.conf gracc-raw-template.json \
	  gracc-raw.service gracc-raw@.service \
	  README.md

rpm: $(FILES)
	tar czf $(HOME)/rpmbuild/SOURCES/gracc-raw.tar.gz $(FILES)
	rpmbuild -ba gracc-raw.spec
