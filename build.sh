biber --tool references.bib --output-file=references-clones.bib --config=clones.conf
pdflatex main
bibtexu main
bibtexu sec
pdflatex main
pdflatex main
