biber --tool references.bib --output-file=references-clones.bib --config=clones.conf --output-legacy-dates
xelatex main --nouri-encode
bibtexu main
bibtexu sec
xelatex main --nouri-encode
xelatex main --nouri-encode
