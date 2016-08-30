FILES=gracc-raw.conf gracc-raw-template.json defaults.env \
	  gracc-raw.service gracc-raw@.service \
	  README.md

.PHONY: rpm
rpm: $(FILES)
	tar czf $(HOME)/rpmbuild/SOURCES/gracc-raw.tar.gz $(FILES)
	rpmbuild -ba gracc-raw.spec

.PHONY: docker
docker:
	docker build --no-cache -t opensciencegrid/gracc-stash-raw:0 .
