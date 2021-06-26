(TeX-add-style-hook
 "polynomial-besov"
 (lambda ()
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (LaTeX-add-labels
    "sec:orgde1591a"
    "thm:reg-poly-diff"
    "eq:cond:thm:reg-poly-diff"
    "lem:loc-reg-poly-diff"
    "sec:org9828763"
    "thm:besov-sobolev"
    "thm:estimate-product"
    "eq:estimate-product-1"
    "eq:estimate-product-2"
    "thm:compo-besov"
    "sec:org63db1f4"
    "eq:term-small"
    "eq:term-c"
    "eq:term-f"
    "eq:est-term-small"
    "eq:est-term-c"
    "eq:est-term-f"
    "eq:est-del-c"
    "eq:est-del-f"
    "lem:loc-est-reg"
    "eq:fin-del-small"
    "eq:fin-del-c"
    "eq:fin-del-f"))
 :latex)

