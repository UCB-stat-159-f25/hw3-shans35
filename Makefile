
# create and configure ligo. If it already exists, update it with environment.yml
.PHONY: env
env:
	@if conda env list | grep -q "ligo"; then \
		conda env update -n ligo -f environment.yml; \
	else \
		conda env create -f environment.yml; \
	fi

# build the html rendering of the MyST site
.PHONY: html
html:
	myst build --html

# clean up the figures, audio and _build folders
.PHONY: clean
clean:
	rm -rf figures/*
	rm -rf audio/*
	rm -rf _build/*