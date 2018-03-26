(TeX-add-style-hook
 "harmonic-maps"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("ulem" "normalem")))
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
    "tikz-cd")
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
    "sec:orga0770cb"
    "sec:orgc583005"
    "sec:org7fb8702"
    "lem:var-energy"
    "prop:holo-harmonic"
    "eq:tangent-exp"
    "sec:orgde542c5"
    "sec:orga475ee1"
    "sec:orgf77e3b3"
    "sec:orge4db110"
    "sec:org09d51c1"
    "ex:pullback-tangent"
    "lem:calculs-general"
    "eq:laplace-Q"
    "rem:calculs-general"
    "eq:Q-negative"
    "sec:orge32ae52"
    "sec:general-calcul"
    "sec:orgce54bf2"
    "prop:calculs-pullback-tangent"
    "sec:org75bf29d"
    "lem:calculs-Q-pullback"
    "sec:org54c4eb4"
    "cor:signed-curvature"
    "sec:orgde0028d"
    "sec:org46dcaf2"
    "lem:second-fund-form"
    "eq:second-fund-form"
    "sec:org9b63041"
    "prop:harm-imm-curvature"
    "sec:org80dc4ea"
    "sec:orgc15dcd7"
    "thm:Ehresmann-Hermann"
    "eq:g-product"
    "trivalising-map"
    "thm:Hermann"
    "eq:calcul-Hermann"
    "sec:org4589654"
    "prop:tension-fibration"
    "sec:org95f4faf"
    "prop:composition-general"
    "eq:sff-composition"
    "eq:tension-field-composition"
    "prop:compo-immersion"
    "prop:compo-submersion"
    "cor:compo-with-submersion"
    "sec:orgcf5b6e5")
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

