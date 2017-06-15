(TeX-add-style-hook
 "de-rham-decomposition"
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
    "tikz-cd")
   (LaTeX-add-labels
    "sec:orge9ef341"
    "orgdba7781"
    "thm:Frobenius"
    "org0b71a21"
    "sec:orgfa8426c"
    "prop:uniqueness"
    "orgd364943"
    "lem:uniqueness-fiber"
    "orgc745ef1"
    "lem:unique-representation"
    "org1eacae9"
    "sec:org08f8c91")
   (LaTeX-add-environments
    "remark"
    "theorem"
    "lemma"
    "corollary"
    "conjecture"
    "proposition"
    "problem"
    "example"
    "definition"))
 :latex)

