import os
from time import perf_counter
from pymech.dataset import open_mfdataset
from distributed import Client


tstart = perf_counter()
client = Client(scheduler_file=os.path.expanduser("~/scheduler.json"))
ds = open_mfdataset(
    "/var/scratch/data/2020-08-12/abl_grid-refine_4x32x4_V640.x1500.x640._2020-08-07_14-56-45/stsabl*",
    #  chunks=True,
    parallel=True
)

print(f"opening: took {perf_counter() - tstart} seconds")

# Timing with 100 statistics files gave
# chunks=False, parallel=False, Wall time: 47.4 s
# chunks=True, parallel=True, Wall time: 32.5 s
# chunks=False, parallel=True, Wall time: 18.5 s


import dask.array as da
import xarray as xr

tstart = perf_counter()
dsc = ds.chunk({"time": "auto"})
print(f"chunk: took {perf_counter() - tstart} seconds")

tstart = perf_counter()
ds.s01.mean()
print(f"mean: took {perf_counter() - tstart} seconds")

