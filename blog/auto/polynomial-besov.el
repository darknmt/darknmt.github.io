(TeX-add-style-hook
 "polynomial-besov"
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
    "gcd"
    "Ric"
    "Riem")
   (LaTeX-add-labels
    "sec:org0744758"
    "sec:org59b4c4d"
    "thm:reg-poly-diff"
    "eq:cond:thm:reg-poly-diff"
    "lem:loc-reg-poly-diff"
    "sec:org44fac2b"
    "thm:besov-sobolev"
    "thm:estimate-product"
    "eq:estimate-product-1"
    "eq:estimate-product-2"
    "thm:compo-besov"
    "sec:org9631d3c"
    "eq:term-small"
    "eq:term-c"
    "eq:term-f"
    "eq:est-term-small"
    "eq:est-term-c"
    "eq:est-term-f"
    "eq:est-del-c"
    "eq:est-del-f"
    "lem:loc-est-reg"
    "eq:fin-del-small"
    "eq:fin-del-c"
    "eq:fin-del-f"
    "sec:orge66e875"
    "thm:reg-nonlin-heat"
    "sec:org5d82ff9"
    "thm:short-time")
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

