(TeX-add-style-hook
 "sheaf-cohomology"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("ulem" "normalem")))
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
    "tikz-cd")
   (TeX-add-symbols
    "im"
    "supp"
    "ord")
   (LaTeX-add-labels
    "sec:orgb21ab35"
    "sec:org3a8407f"
    "sec:org1a74cb6"
    "thm:cohomology-complex"
    "fig:morph-short-sequence"
    "thm:prism-operator"
    "fig:homotopy-operator"
    "sec:orgc84cfe1"
    "thm:Kunneth"
    "sec:orgb3169b7"
    "sec:orgb23aff9"
    "thm:existence-cohomology"
    "lem:exactness"
    "thm:uniqueness-cohomology"
    "thm:fine-resolution"
    "sec:orga925396"
    "sec:orgfec47f3"
    "thm:de-rham-singular"
    "sec:org97a966e"
    "sec:org97c2406"
    "sec:org070ad7f"
    "sec:orga94f1e5"
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
    "propdef"))
 :latex)

