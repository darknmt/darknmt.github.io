(TeX-add-style-hook
 "Berger-remark-complex"
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
    "sec:org8dadc8b"
    "sec:orgd7c3657"
    "thm:Berger"
    "org8c4787f"
    "sec:org7941aae"
    "sec:org5370687"
    "sec:org053d618"
    "sec:org057f73c"
    "sec:orgee3692a"
    "sec:orgaca95b1"
    "lem:alg-exterior"
    "orgaa395a7"
    "fig:dz"
    "fig:dzbar")
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

