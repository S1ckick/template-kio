biber --tool references.bib --output-file=references-clones.bib --config=clones.conf
xelatex main --nouri-encode
bibtexu main
bibtexu sec
xelatex main --nouri-encode
xelatex main --nouri-encode
