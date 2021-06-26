(TeX-add-style-hook
 "2018-report"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("geometry" "a4paper" "margin=1in") ("inputenc" "utf8") ("fontenc" "T1") ("ulem" "normalem") ("xy" "all")))
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
    "geometry"
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
    "Ric"
    "Riem"
    "Enorm"
    "Anorm"
    "Cl"
    "Spin"
    "Pin"
    "Hom"
    "End")
   (LaTeX-add-labels
    "sec:org8b4671d"
    "sec:org7475457"
    "eq:energy-def"
    "eq:tension-def"
    "eq:tension-flow"
    "thm:eells-sampson"
    "eq:alg-top-cond"
    "lem:main-est"
    "eq:main-est-1"
    "eq:main-est-2"
    "sec:orgb5043c6"
    "lem:existence-sbdf"
    "sec:orgcde7df1"
    "eq:A-M-Anorm"
    "rem:Neumann-2-Dirichlet"
    "sec:org6396e24"
    "sec:orge80d2e9"
    "lem:ren-en"
    "eq:en-1"
    "eq:en-2"
    "rem:bndry-cond"
    "lem:intermediate-cond"
    "sec:org3b8746b"
    "thm:crit-renorm"
    "eq:cond-Q"
    "eq:expansion-Q"
    "eq:cond-Q-2"
    "lem:var-domain"
    "sec:org71ecf8c"
    "lem:enorm-var"
    "eq:Enorm-var"
    "eq:E-L-Anorm"
    "sec:orgeceecba"
    "prop:unbound-Anorm"
    "thm:anderson-H3"
    "prop:bound-Anorm-minimal")
   (LaTeX-add-bibliographies
    "../res/GeoDiff")
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
    "propdef"
    "fact"
    "assertion"))
 :latex)

