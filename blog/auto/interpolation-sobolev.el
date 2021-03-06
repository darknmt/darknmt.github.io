(TeX-add-style-hook
 "interpolation-sobolev"
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
    "sec:orgc3441c8"
    "sec:orgd4a87c1"
    "sec:org7695576"
    "thm:stein-crit"
    "rem:weight"
    "thm:equiv-norm-Sobolev"
    "sec:orgf24d7d0"
    "thm:3-line"
    "fig:interpol-pair"
    "rem:interp-pair"
    "fig:unique-interpol-pair"
    "thm:interp-ineq-ele"
    "thm:interp-ineq-op"
    "lem:interp-ineq"
    "thm:interp-sobolev"
    "thm:dir-sum-interp"
    "thm:interp-closed-emb"
    "eq:ses-interp"
    "thm:compact-interp"
    "sec:orgb45ccd2"
    "def:sobolev-space"
    "rem:hamilton-typo"
    "thm:interp-sobolev-M"
    "sec:orgd932199"
    "def:sobolev-space-b"
    "lem:equiv-norm-sobolev"
    "sec:org043596f"
    "sec:orge91e420"
    "eq:ses-S"
    "lem:construction-varphi"
    "eq:ses-S-split"
    "eq:Eplus-Rplus"
    "rem:coupling-S"
    "eq:ses-S-Sstar"
    "thm:sobolev-def-ses"
    "eq:ses-S-W-Sstar"
    "sec:org163f9fc"
    "eq:S-W-S-3d"
    "rem:funct-Dy"
    "thm:descrpt-sobolev"
    "sec:orgfbd3028"
    "thm:vanishing-trace"
    "lem:Nplus"
    "ex:vanishing-trace"
    "thm:def-trace"
    "thm:trace-reg"
    "eq:def-trace-1"
    "eq:def-trace-2"
    "eq:def-trace-3"
    "thm:patching"
    "sec:orgbb83fb6")
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

