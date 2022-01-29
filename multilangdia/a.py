from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def pt(t: float, v: float) -> float:
    if v < 0.5:
        return t
    return 13.12 + 0.6215 * t + (0.3965 * t - 11.37) * (v ** 0.16)


def plt1():
    n = 30
    ts_base = np.linspace(-20, 50, n)
    vs_base = np.linspace(0, 100, n)
    ts = []
    vs = []
    tds = []
    for _t in ts_base:
        ti = []
        vi = []
        t1i = []
        tdi = []
        for _v in vs_base:
            t1 = pt(_t, _v)
            td = t1 - _t
            ti.append(_t)
            vi.append(_v)
            t1i.append(t1)
            tdi.append(td)
        ts.append(ti)
        vs.append(vi)
        tds.append(tdi)

    X = np.array(vs)
    Y = np.array(ts)
    Z = np.array(tds)

    w = 20
    fig = plt.figure(figsize=(w, w))
    ax = fig.add_subplot(projection='3d')
    # fig.suptitle("Gefühlte Temperatur")
    ax.set_ylabel("Temperatur (°C)")
    ax.set_zlabel("Gefühlte Temperaturdifferenz (C°)")
    ax.set_xlabel("Windgeschwindigkeit (km/h)")
    # ax.set_ylim(50, -20)
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False, alpha=0.8, vmin=-20, vmax=20)
    fig.colorbar(surf, shrink=0.6, aspect=20)
    target_path = Path(__file__).parent / "target"
    if not target_path.exists():
        target_path.mkdir()
    fi = target_path / "ft.svg"
    print(f"wrote image to {fi}")
    plt.savefig(fi, bbox_inches='tight')


plt1()
