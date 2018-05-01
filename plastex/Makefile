export TEXINPUTS=.:./commontex:./texinputs/:

pdf: sobolev-riemannian.aux
	pdflatex sobolev-riemannian

html:
	plastex test-sobolev

html5:
	plastex --renderer=HTML5 test-sobolev

sobolev-riemannian.aux:
	pdflatex sobolev-riemannian

clean:
	rm -rf plastex *.idx *.paux *.aux *.out *.syn *.log *.toc plastex.pdf
