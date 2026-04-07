biber --tool references.bib --output-file=references-clones.bib --config=clones.conf --output-legacy-dates
xelatex main
bibtexu main
bibtexu eng
xelatex main
xelatex main
