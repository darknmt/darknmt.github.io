(TeX-add-style-hook
 "sobolev-riemannian"
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
   (LaTeX-add-labels
    "thm:Sobolev-Rn"
    "thm:Kondrachov-Rn"
    "sec:org0d6bfe8"
    "eq:jacobi-field"
    "rem:obvious-jacobi"
    "prop:jacobi-exp"
    "eq:jacobi-exp"
    "fig:jacobi-exp"
    "prop:index-form-variation"
    "eq:second-var"
    "thm:index-ineq"
    "rem:jacobi-existence"
    "sec:orgb6d71b5"
    "sec:org4abfd0a"
    "rem:hairy-ball"
    "thm:vol-comparison"
    "eq:comp-1"
    "eq:comp-2"
    "eq:comp-3"
    "eq:comp-4"
    "rem:on-vol-comp"
    "rem:cor-vol-comp"
    "eq:comp-norm"
    "eq:comp-norm-ap"
    "lem:compare-const-sec-curv"
    "thm:myers"
    "prop:geodesic-convex"
    "sec:org5678b4c"
    "lem:calabi"
    "eq:lem:calabi"
    "lem:vitali-cover"
    "lem:uni-loc-finite-cover"
    "sec:org988defc"
    "thm:sobolev-imbedding"
    "rem:sobolev-def"
    "prop:Cc-dense-W1p"
    "lem:sobolev-case"
    "lem:sobolev-case-holder"
    "fig:sobolev-holder"
    "eq:lem:sobolev-case-holder"
    "prop:sobolev-imbedding-1"
    "thm:aubin-loc"
    "sec:orgb2a0b0a"
    "thm:kondrachov"
    "sec:org8cc1a23"
    "thm:spec-lap"
    "thm:lap-l2"
    "eq:lap-M")
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

