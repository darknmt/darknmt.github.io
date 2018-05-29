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
    "sec:org495c68b"
    "diag:elliptic"
    "diag:D"
    "thm:elliptic-const"
    "diag:split"
    "thm:split-exact"
    "thm:compact-op-exact"
    "ell-half-plan"
    "sec:orgd1711f0"
    "sec:org8848364"
    "thm:approx-inv-B"
    "sec:org82ddd74"
    "rem:hamilton-sign-issue"
    "sec:org5fde825"
    "thm:approx-inv-A"
    "sec:org2cca0f4"
    "thm:approx-inv-C"
    "thm:exact-half"
    "eq:elliptic-half"
    "sec:org9acbd84"
    "sec:org61a8cc0"
    "thm:exact-open"
    "prop:interior-cube"
    "prop:boundary-cube"
    "lem:ell-loc-cube"
    "lem:ell-loc-bndry"
    "thm:elliptic-general"
    "lem:compose-exact"
    "sec:orgceb049f"
    "thm:ref-kernel"
    "thm:reg-coker"
    "sec:org3fd7474"
    "sec:orgc770b70"
    "sec:global-result-para"
    "sec:org07f15e4"
    "thm:para-causality"
    "rem:init-cond-para"
    "sec:org5e692a3"
    "thm:reg-parabolic"
    "eq:reg-para"
    "sec:orgb15db76"
    "sec:org6b3c0b4"
    "thm:max-princ-para"
    "sec:orga02d3ee"
    "eq:para-system"
    "thm:lin-heat")
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

