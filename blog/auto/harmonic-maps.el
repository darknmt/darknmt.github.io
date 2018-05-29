(TeX-add-style-hook
 "harmonic-maps"
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
    "gcd")
   (LaTeX-add-labels
    "sec:orgb2b8fc5"
    "sec:org3a32bb7"
    "sec:org5d8b4be"
    "lem:var-energy"
    "prop:holo-harmonic"
    "eq:tangent-exp"
    "sec:org562e6c9"
    "sec:org7b30a2d"
    "sec:org5c035e0"
    "sec:org25624e1"
    "sec:orgef11969"
    "ex:pullback-tangent"
    "lem:calculs-general"
    "eq:laplace-Q"
    "rem:calculs-general"
    "eq:Q-negative"
    "sec:org8cba122"
    "sec:general-calcul"
    "sec:orgfbbf7a0"
    "prop:calculs-pullback-tangent"
    "sec:org42cacba"
    "lem:calculs-Q-pullback"
    "sec:org726b9c7"
    "cor:signed-curvature"
    "sec:org3f73858"
    "sec:orgfe7593c"
    "lem:second-fund-form"
    "eq:second-fund-form"
    "sec:org221723f"
    "prop:harm-imm-curvature"
    "sec:orgc6c84be"
    "sec:org83f306b"
    "thm:Ehresmann-Hermann"
    "eq:g-product"
    "trivalising-map"
    "thm:Hermann"
    "eq:calcul-Hermann"
    "sec:org04130fa"
    "prop:tension-fibration"
    "sec:org1f696cb"
    "prop:composition-general"
    "eq:sff-composition"
    "eq:tension-field-composition"
    "prop:compo-immersion"
    "prop:compo-submersion"
    "cor:compo-with-submersion"
    "sec:orgf459a97"
    "sec:org5ec4516"
    "eq:loc-heat-flow"
    "thm:eells-sampson"
    "thm:hamilton-bndry-Dirichlet"
    "sec:orgf68ba1e"
    "sec:orgcc38f33"
    "thm:global-eq"
    "eq:global-heat"
    "thm:unique-nonlinear-heat"
    "eq:dev-sig-unique"
    "eq:sym-red-beta"
    "eq:first-order-w"
    "rem:hamilton-alg-rig")
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

