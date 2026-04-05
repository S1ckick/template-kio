python3 extract_cites.py main.tex ieee_init.tex ieee.tex
pdflatex ieee
biber ieee
pdflatex ieee
pdflatex ieee
pdflatex main
biber main
pdflatex main
pdflatex main