(TeX-add-style-hook
 "twistor-correspondence"
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
    "Riem"
    "Enorm"
    "Anorm")
   (LaTeX-add-labels
    "sec:org3d556b1"
    "thm:min-surface-R3"
    "rem:compl-inn-prod"
    "sec:orgac80af6"
    "sec:org6a209ff"
    "rem:null-cone-simple"
    "rem:complex-str-2-vect"
    "thm:SOV-cover"
    "cor:sum-null"
    "sec:orge30020e"
    "rem:orient-twistor"
    "prop:reduced-LC"
    "sec:org30c6e1b"
    "prop:holo-sec-S"
    "prop:no-1-1"
    "sec:org4b76a05"
    "prop:holo-and-D"
    "thm:D1-integ"
    "thm:integ-Jminus"
    "sec:org5fe93d5"
    "rem:alt-def-Gausslift"
    "thm:twistor-cor"
    "sec:org2329e55"
    "sec:org026812b"
    "thm:infty-jet"
    "prop:crit-isol"
    "eq:gen-cauchy-rie"
    "prop:vert-tang"
    "eq:u-v-vertical"
    "sec:org7410886"
    "sec:org1232989"
    "sec:org96ae2dc")
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

