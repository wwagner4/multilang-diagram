from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import datetime


def windchill(t: float, v: float) -> float:
    if v < 0.5:
        return t
    return 13.12 + 0.6215 * t + (0.3965 * t - 11.37) * (v ** 0.16)


def create_diagram(
        out_dir: Path,
        x_label: str,
        y_label: str,
        z_label: str,
) -> str:
    """
    Creates a diagram file in out_dir.
    :param out_dir: Output directory. Must exist
    :param x_label: Text to be used as x label
    :param y_label: Text to be used as y label
    :param z_label: Text to be used as z label
    :return: Name of the created file
    """
    if not out_dir.exists():
        raise AttributeError(f"out dir {out_dir} does not exist")
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
            t1 = windchill(_t, _v)
            td = t1 - _t
            ti.append(_t)
            vi.append(_v)
            t1i.append(t1)
            tdi.append(td)
        ts.append(ti)
        vs.append(vi)
        tds.append(tdi)

    w = 20
    fig = plt.figure(figsize=(w, w))
    ax = fig.add_subplot(projection='3d')
    # fig.suptitle("Gefühlte Temperatur")
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)
    # ax.set_ylim(50, -20)
    surf = ax.plot_surface(np.array(vs),
                           np.array(ts),
                           np.array(tds),
                           cmap=cm.coolwarm,
                           linewidth=0,
                           antialiased=False,
                           alpha=0.8,
                           vmin=-20,
                           vmax=20)
    fig.colorbar(surf, shrink=0.6, aspect=20)
    time_stamp = '{:%H%M%S%f}'.format(datetime.datetime.now())
    diagram_name = f"diagram-{time_stamp}.svg"
    fi = out_dir / diagram_name
    print(f"wrote image to {fi}")
    plt.savefig(fi, bbox_inches='tight')
    return diagram_name


if __name__ == "__main__":
    _out_dir = Path(__file__).parent / "target"
    if not _out_dir.exists():
        _out_dir.mkdir()
        print(f"Created out dir {_out_dir.absolute()}")
    file_name = create_diagram(_out_dir, "X Label", "Y Label", "Z Label")
    print(f"Created diagram {file_name} in {_out_dir.absolute()}")
