biber --tool references.bib --output-file=references-clones.bib --config=clones.conf --output-legacy-dates
biber --tool references-en.bib --output-file=references-en-prefixed.bib --config=prepend-en.conf --output-legacy-dates
xelatex main
bibtexu main
bibtexu eng
xelatex main
xelatex main
