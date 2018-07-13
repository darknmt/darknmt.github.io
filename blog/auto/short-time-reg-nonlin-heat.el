(TeX-add-style-hook
 "short-time-reg-nonlin-heat"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("ulem" "normalem") ("xy" "all")))
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
    "sec:org22faf28"
    "sec:org5671233"
    "thm:interp-sobolev-d"
    "thm:Sobolev-Rn-d"
    "thm:Kondrachov-Rn-d"
    "sec:org4cdc2fe"
    "sec:org886825b"
    "sec:org76293a6"
    "thm:elliptic-d"
    "thm:para-existence-d"
    "thm:para-eq-d "
    "sec:org4cffd64"
    "thm:max-princ-d"
    "thm:infty-comparison-d"
    "thm:1-comparison-d"
    "sec:orgfeacc02"
    "thm:reg-quad"
    "eq:cond:thm:reg-poly-diff"
    "sec:orgfe7e1e0"
    "thm:reg-nonlin-heat"
    "sec:orgbdcaf31"
    "thm:short-time")
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
    "assertion"))
 :latex)

