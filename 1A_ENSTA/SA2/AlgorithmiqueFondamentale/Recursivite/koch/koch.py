# -*- coding: utf-8 -*-
"""
@author: Christophe Osswald. WTFPL.
"""

import koch_drawer as kd


def decoupe(pd, pf, n):
    if n == 0:
        kd.draw(pd, pf)
        return

    # Calcule les points p1/3, ps et p2/3
    p1 = ((2 * pd[0] + pf[0]) / 3, (2 * pd[1] + pf[1]) / 3)
    p2 = ((pd[0] + 2 * pf[0]) / 3, (pd[1] + 2 * pf[1]) / 3)
    ps = (
        (pd[0] + pf[0]) / 2 - (pf[1] - pd[1]) / (2 * (3**0.5)),
        (pd[1] + pf[1]) / 2 + (pf[0] - pd[0]) / (2 * (3**0.5)),
    )

    # Appels récursifs
    decoupe(pd, p1, n - 1)
    decoupe(p1, ps, n - 1)
    decoupe(ps, p2, n - 1)
    decoupe(p2, pf, n - 1)


if __name__ == "__main__":
    x = (0, 0)
    y = (1, 0)

    n = 5
    decoupe(x, y, n)

    print(round(kd.longueur(), 2))  # arrondi à 1/100 près
    kd.draw_koch()
