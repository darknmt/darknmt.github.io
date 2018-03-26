(TeX-add-style-hook
 "green-function"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("ulem" "normalem")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "inputenc"
    "fontenc"
    "graphicx"
    "grffile"
    "longtable"
    "wrapfig"
    "rotating"
    "ulem"
    "amsmath"
    "textcomp"
    "amssymb"
    "capt-of"
    "hyperref"
    "amsthm"
    "amscd"
    "mathtools"
    "tikz-cd")
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
   (LaTeX-add-labels
    "rem:green-riem-surf"
    "eq:lap-complex"
    "sec:org5cade25"
    "lem:lap-radial"
    "rem:lap-rad"
    "eq:lap-Hpq"
    "prop:green-formula"
    "eq:green-formula"
    "rem:transposition"
    "eq:transposition-parametrix"
    "sec:org5aec0dd"
    "thm:existence-green"
    "eq:green-int"
    "eq:G-bound"
    "eq:derivative-bound"
    "eq:convo-k"
    "lem:reg-conv"
    "eq:transp-green-int"
    "eq:3"
    "eq:4")
   (LaTeX-add-bibliographies
    "../res/Stage2018")
   (LaTeX-add-amsthm-newtheorems
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

