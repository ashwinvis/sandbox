# trace generated using paraview version 5.7.0
#
from vtk.numpy_interface import dataset_adapter as dsa
from vtk.util.numpy_support import vtk_to_numpy
import numpy as np
from vtktools import vtkio
# from vtk.numpy_interface import algorithms as algs
# from paraview.servermanager import *
# import the simple module from the paraview
import paraview.simple as pv
# disable automatic camera reset on 'Show'
pv._DisableFirstRenderCameraReset()



class NekReader:
    """Create a new enhanced 'VisItNek5000Reader'."""
    def __init__(
        self,
        filename,
        arrays=('pressure', 'velocity_mag',
                'x_velocity', 'y_velocity', 'z_velocity')
    ):
        self.nek5000 = nek5000 = pv.VisItNek5000Reader(FileName=filename)
        nek5000.Meshes=['mesh']
        nek5000.PointArrays=[]

        # get animation scene
        self.animationScene1=pv.GetAnimationScene()

        # get the time-keeper
        self.timeKeeper1=pv.GetTimeKeeper()

        # update animation scene based on data timesteps
        self.animationScene1.UpdateAnimationUsingDataTimeSteps()

        # Properties modified on ablnek5000
        nek5000.PointArrays=arrays

    def __iter__(self):
        return self

    def __next__(self):
        self.animationScene1.GoToNext()
        # return self.get_data

    @property
    def time(self):
        return self.timeKeeper1.Time




if __name__ == "__main__":
    reader = NekReader(
        # filename='/run/media/avmo/seagate/runs/abl_irrot_15x24x10_V1pix1.x1.571_2020-02-05_12-02-28/abl.nek5000'
        filename='/home/avmo/src/exabl/data/abl_irrot_15x24x10_V1pix1.x1.571_2020-02-05_12-02-28/abl.nek5000'
    )
    print(reader.time)
    next(reader)
    print(reader.time)
    for _ in reader:
        print(reader.time)
        pass