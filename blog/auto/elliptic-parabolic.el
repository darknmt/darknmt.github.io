(TeX-add-style-hook
 "elliptic-parabolic"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("ulem" "normalem") ("xy" "all")))
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
    "gcd"
    "Ric"
    "Riem")
   (LaTeX-add-labels
    "sec:org2267616"
    "diag:elliptic"
    "diag:D"
    "thm:elliptic-const"
    "diag:split"
    "thm:split-exact"
    "thm:compact-op-exact"
    "ell-half-plan"
    "sec:org0deb1e7"
    "sec:org52b14de"
    "thm:approx-inv-B"
    "sec:org25e9d81"
    "rem:hamilton-sign-issue"
    "sec:org9757bc8"
    "thm:approx-inv-A"
    "sec:orgac1470a"
    "thm:approx-inv-C"
    "thm:exact-half"
    "eq:elliptic-half"
    "sec:org7498191"
    "sec:orgfa2fb3e"
    "thm:exact-open"
    "prop:interior-cube"
    "prop:boundary-cube"
    "lem:ell-loc-cube"
    "lem:ell-loc-bndry"
    "thm:elliptic-general"
    "lem:compose-exact"
    "sec:orge2f277f"
    "thm:ref-kernel"
    "thm:reg-coker"
    "sec:org414d75c"
    "sec:org4c87ce2"
    "sec:global-result-para"
    "sec:org33fecf2"
    "thm:para-causality"
    "rem:init-cond-para"
    "sec:org13c850a"
    "thm:reg-parabolic"
    "eq:reg-para"
    "sec:org0e058a2"
    "sec:org5395cc9"
    "eq:para-system"
    "thm:lin-heat"
    "sec:org641166d"
    "thm:max-princ-para"
    "thm:infty-comparison"
    "eq:infty-comparison"
    "sec:orgb1e4ade"
    "thm:1-comparison"
    "eq:1-comparison")
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

