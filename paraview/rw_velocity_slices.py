from bisect import bisect
from pathlib import Path

import numpy as np
#  import matplotlib.pyplot as plt
import xarray as xr
from nekio import NekReader


scratch = Path("/run/media/avmo/Scratch/data")
filename = (
    # scratch / "abl_rot_30x48x20_V1pix1.x1.571_2020-02-09_17-40-03/abl.nek5000"
    scratch / "abl_rot_30x48x20_V1pix1.x1.571_2020-04-10_03-50-27/abl.nek5000"
)
assert filename.exists()

key_arrays = tuple(f"{ax}_velocity" for ax in ("x", "y", "z"))
print(key_arrays)
reader = NekReader(filename, arrays=key_arrays)

# Time
ts_start = 15  # approx
ts_idx = bisect(reader.timesteps, ts_start) - 1
reader.time = reader.timesteps[ts_idx]

# Wall normal: y
vert = reader.get_slice(x=0.1, normal=(1, 0, 0))
_, ys, _, _ = vert.get_coords(normal=0, reshape=False)
ys = np.unique(ys)
# ys = ys[1::80]
ys = np.hstack((ys[0:15], ys[15:100:20], ys[100::50]))
# ys = ys[:30];
ys[0] = 1e-14
print("ys =", ys)


def mk_data():
    s = reader.get_slice(y=ys[0], normal=(0, 1, 0))
    x, _, z, inds = s.get_coords(normal=1, reshape=True)
    ds = xr.Dataset(
        coords={
            "t": reader.timesteps[ts_idx + 1:],
            "y": ys,
            #  "x": np.unique(x),
            #  "z": np.unique(z),
            "z": np.median(z, axis=1),
            "x": np.median(x, axis=0),
        }
    )
    return ds


def get_data(slice1, t, y):
    x, _, z, inds = slice1.get_coords(normal=1, reshape=True)
    ds = xr.Dataset(
        coords={
            "t": t,
            "y": y,
            "z": np.median(z, axis=1),
            "x": np.median(x, axis=0),
        }
    )
    for key in key_arrays:
        arr = slice1.get_array(key)
        arr = slice1.reshape(arr[inds], x.shape)
        ds[key] = (('z', 'x'), arr)
        ds[key] = ds[key].expand_dims(("t", "y"))

    return ds


reader.time = reader.timesteps[ts_idx]
ds = mk_data()
print(ds)
print("Consolidating data...")

for t, in reader:
    display = reader.show(key_arrays[0])
    for y in ys:
        print("t =", t, "y =", y, end=" ")
        s = reader.get_slice(y=y)
        # s.plot_contours("x_velocity")

        ds1 = get_data(s, t, y)
        print("ux_max =", float(ds1.x_velocity.max()))
        ds = ds.merge(ds1)
        # Quick exit
        #  1 / 0

        #  plt.pause(0.2)
    ds.to_netcdf(f'velocity_slices_for_div_check.nc', mode="a", engine="h5netcdf")

print(ds)


