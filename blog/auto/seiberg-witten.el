(TeX-add-style-hook
 "seiberg-witten"
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
    "Anorm"
    "Cl"
    "Spin"
    "Pin"
    "Hom"
    "End")
   (LaTeX-add-labels
    "sec:orge7ff1a8"
    "sec:org4d17e61"
    "sec:orgd12cda9"
    "sec:org6ec9b7c"
    "rem:cl-first"
    "prop:cl-ext"
    "sec:orgc443642"
    "rem:unique-cl"
    "prop:auto-cl"
    "prop:spin-so"
    "def:split-cl"
    "rem:cl0-decomp"
    "prop:alg-str-cl"
    "cor:cl-incr-1"
    "eq:spinc-double"
    "sec:orge02169c"
    "prop:spin-rep-split"
    "cor:spin-rep-split"
    "sec:org33f5150"
    "sec:org77ca816"
    "lem:rep-H"
    "eq:rep-H"
    "sec:orgeaf3734"
    "sec:orgeb8dbb5"
    "sec:orgddbfe22"
    "prop:self-dual-cl"
    "eq:self-dual-cl"
    "sec:org34a6513"
    "prop:exist-spinc"
    "prop:spin-conn-alg"
    "lem:bundle-ext"
    "sec:orgb6b4f78"
    "eq:spin-conn"
    "eq:spinc-conn"
    "sec:org253e03a"
    "eq:dirac-coord"
    "prop:dirac-self-ad"
    "sec:orgd65572d")
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

