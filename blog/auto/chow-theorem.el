(TeX-add-style-hook
 "chow-theorem"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("ulem" "normalem")))
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
    "thm:chow"
    "sec:org26820ef"
    "prop:alg"
    "prop:ana"
    "prop:fact-1"
    "prop:fact-2"
    "sec:orge2d2e7d"
    "prop:mult"
    "lem:schwarz")
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
    "propdef"))
 :latex)

