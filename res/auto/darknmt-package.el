(TeX-add-style-hook
 "darknmt-package"
 (lambda ()
   (TeX-run-style-hooks
    "amsthm"
    "amsmath"
    "amscd"
    "amssymb"
    "mathtools"
    "tikz-cd"
    "svg")
   (TeX-add-symbols
    '("transp" ["argument"] 1)
    '("restr" 2)
    "im"
    "supp"
    "ord"
    "Spec"
    "vol"
    "sff"
    "tr"
    "const")
   (LaTeX-add-environments
    "remark"
    "theorem"
    "lemma"
    "corollary"
    "conjecture"
    "proposition"
    "problem"
    "exampl"
    "definition"
    "propdef"))
 :latex)

