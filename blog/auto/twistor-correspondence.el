(TeX-add-style-hook
 "twistor-correspondence"
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
    "Riem"
    "Enorm"
    "Anorm")
   (LaTeX-add-labels
    "sec:org110e957"
    "thm:min-surface-R3"
    "rem:compl-inn-prod"
    "sec:org17c31e9"
    "sec:orge71a081"
    "rem:null-cone-simple"
    "rem:complex-str-2-vect"
    "thm:SOV-cover"
    "cor:sum-null"
    "sec:org574bc81"
    "rem:orient-twistor"
    "prop:reduced-LC"
    "sec:org65fef00"
    "prop:holo-sec-S"
    "prop:no-1-1"
    "sec:orga46f54f"
    "prop:holo-and-D"
    "thm:D1-integ"
    "thm:integ-Jminus"
    "sec:org5da2a7a"
    "rem:alt-def-Gausslift"
    "thm:twistor-cor"
    "sec:org0e00d14"
    "sec:org2990a00"
    "thm:infty-jet"
    "prop:crit-isol"
    "eq:gen-cauchy-rie"
    "prop:vert-tang"
    "eq:u-v-vertical"
    "sec:orgbe6c7d8"
    "rem:ddbarf"
    "sec:org088b53c"
    "thm:smooth-twistor-cor"
    "eq:smooth-twistor-1"
    "eq:smooth-twistor-2")
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

