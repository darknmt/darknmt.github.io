(TeX-add-style-hook
 "sheaf-cohomology"
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
    "sec:org89ea00e"
    "sec:org32c7c12"
    "sec:org8c61468"
    "sec:orgbad4845"
    "sec:orgdb74180"
    "thm:cohomology-complex"
    "fig:morph-short-sequence"
    "thm:prism-operator"
    "fig:homotopy-operator"
    "sec:org8b30707"
    "thm:Kunneth"
    "sec:org62ef2d8"
    "sec:org65911e0"
    "thm:existence-cohomology"
    "lem:exactness"
    "thm:uniqueness-cohomology"
    "thm:fine-resolution"
    "sec:org6b8dfb5"
    "sec:orgbd2adbd"
    "thm:de-rham-singular"
    "sec:org91022b2"
    "thm:leray"
    "sec:org9316080"
    "sec:orgd0b07bb"
    "sec:org6924367"
    "thm:div-pic-rel")
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

