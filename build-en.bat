biber --tool references.bib --output-file=references-clones.bib --config=clones.conf --output-legacy-dates
perl prepend-en.pl references-en.bib > references-en-prefixed.bib
xelatex main-en
bibtexu main-en
bibtexu eng
xelatex main-en
xelatex main-en