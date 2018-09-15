(TeX-add-style-hook
 "minimal-immersion-S2"
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
    "sec:org54655aa"
    "sec:org474e7cc"
    "sec:org6a8c7e4"
    "thm:Palais-1"
    "thm:Palais-2"
    "cor:Palais-1-2"
    "sec:orgb256c24"
    "rem:tangent-palais"
    "lem:local-isom-e"
    "sec:org145c6ae"
    "prop:crit-val-1"
    "fact:alg-top-Omega-M-N"
    "thm:3-nontrivial-crit"
    "sec:org4c60dc3"
    "rem:rescal-Euclide"
    "lem:main-est"
    "thm:4-trivial-energy"
    "thm:extension-sacks-uhlenbeck"
    "sec:orgd0df0b5"
    "lem:key-sacks-uhlenbeck"
    "rem:topo-C1"
    "prop:2-sacks-uhlenbeck"
    "thm:5-convergence-crit-map"
    "sec:org42b70be"
    "thm:6-final-sacks-uhlenbeck"
    "assert:3-star"
    "prop:3-star"
    "rem:final-sacks-uhlenbeck"
    "sec:orgfdcd974")
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
    "propdef"
    "fact"
    "assertion")
   (LaTeX-add-bibliographies
    "../res/Stage2018"))
 :latex)

