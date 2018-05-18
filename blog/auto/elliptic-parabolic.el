(TeX-add-style-hook
 "elliptic-parabolic"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("ulem" "normalem") ("xy" "all")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
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
    "svg"
    "xy"
    "pgfplots")
   (TeX-add-symbols
    '("transp" ["argument"] 1)
    '("restr" 2)
    "re"
    "im"
    "coker"
    "supp"
    "ord"
    "Spec"
    "vol"
    "sff"
    "tr"
    "const"
    "lcm"
    "gcd")
   (LaTeX-add-labels
    "sec:org143e298"
    "diag:elliptic"
    "diag:D"
    "thm:elliptic-const"
    "diag:split"
    "thm:split-exact"
    "thm:compact-op-exact"
    "ell-half-plan"
    "sec:org27d3d1a"
    "sec:org82f2cf5"
    "thm:approx-inv-B"
    "sec:orgdb25748"
    "rem:hamilton-sign-issue"
    "sec:org5ebc369"
    "thm:approx-inv-A"
    "sec:org263a7ba"
    "thm:approx-inv-C"
    "thm:exact-half"
    "eq:elliptic-half"
    "sec:org06c852d"
    "sec:org07f6ca2"
    "thm:exact-open"
    "prop:interior-cube"
    "prop:boundary-cube"
    "lem:ell-loc-cube"
    "lem:ell-loc-bndry"
    "thm:elliptic-general"
    "lem:compose-exact"
    "sec:orgfee3976"
    "thm:ref-kernel"
    "thm:reg-coker"
    "sec:org2a2daf7"
    "sec:orgb076da7"
    "sec:orgabf9470"
    "thm:para-causality"
    "sec:org9caca77")
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

