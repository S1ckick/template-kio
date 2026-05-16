biber --tool references.bib --output-file=references-clones.bib --config=clones.conf --output-legacy-dates
perl prepend-en.pl references-en.bib > references-en-prefixed.bib
xelatex main
bibtexu main
bibtexu eng
xelatex main
xelatex main