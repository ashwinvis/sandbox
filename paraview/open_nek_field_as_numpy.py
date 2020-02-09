# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`
from vtk.numpy_interface import dataset_adapter as dsa
from vtk.util.numpy_support import vtk_to_numpy
import numpy as np
from vtktools import vtkio
# from vtk.numpy_interface import algorithms as algs
# from paraview.servermanager import *
# import the simple module from the paraview
from paraview.simple import *
# disable automatic camera reset on 'Show'
# paraview.simple._DisableFirstRenderCameraReset()

# create a new 'VisItNek5000Reader'
ablnek5000 = pv.VisItNek5000Reader(
    FileName='/run/media/avmo/seagate/runs/abl_irrot_15x24x10_V1pix1.x1.571_2020-02-05_12-02-28/abl.nek5000')
ablnek5000.Meshes = ['mesh']
ablnek5000.PointArrays = []

# get animation scene
animationScene1 = pv.GetAnimationScene()

# get the time-keeper
timeKeeper1 = pv.GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on ablnek5000
ablnek5000.PointArrays = ['pressure', 'velocity_mag',
                          'x_velocity', 'y_velocity', 'z_velocity']

# get active view
renderView1 = pv.GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1080, 766]

# show data in view
ablnek5000Display = pv.Show(ablnek5000, renderView1)

# trace defaults for the display properties.
ablnek5000Display.Representation = 'Surface'
ablnek5000Display.ColorArrayName = [None, '']
ablnek5000Display.OSPRayScaleArray = 'pressure'
ablnek5000Display.OSPRayScaleFunction = 'PiecewiseFunction'
ablnek5000Display.SelectOrientationVectors = 'None'
ablnek5000Display.ScaleFactor = 0.31415998935699463
ablnek5000Display.SelectScaleArray = 'None'
ablnek5000Display.GlyphType = 'Arrow'
ablnek5000Display.GlyphTableIndexArray = 'None'
ablnek5000Display.GaussianRadius = 0.01570799946784973
ablnek5000Display.SetScaleArray = ['POINTS', 'pressure']
ablnek5000Display.ScaleTransferFunction = 'PiecewiseFunction'
ablnek5000Display.OpacityArray = ['POINTS', 'pressure']
ablnek5000Display.OpacityTransferFunction = 'PiecewiseFunction'
ablnek5000Display.DataAxesGrid = 'GridAxesRepresentation'
ablnek5000Display.PolarAxes = 'PolarAxesRepresentation'
ablnek5000Display.ScalarOpacityUnitDistance = 0.03404065311696019
ablnek5000Display.ExtractedBlockIndex = 2

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ablnek5000Display.ScaleTransferFunction.Points = [
    -0.18865761160850525, 0.0, 0.5, 0.0, 0.12637193500995636, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ablnek5000Display.OpacityTransferFunction.Points = [
    -0.18865761160850525, 0.0, 0.5, 0.0, 0.12637193500995636, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = pv.GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
pv.ColorBy(ablnek5000Display, ('POINTS', 'x_velocity'))

# rescale color and/or opacity maps used to include current data range
ablnek5000Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
ablnek5000Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'x_velocity'
x_velocityLUT = pv.GetColorTransferFunction('x_velocity')

# get opacity transfer function/opacity map for 'x_velocity'
x_velocityPWF = pv.GetOpacityTransferFunction('x_velocity')

# set scalar coloring
pv.ColorBy(ablnek5000Display, ('POINTS', 'y_velocity'))

# Hide the scalar bar for this color map if no visible data is colored by it.
pv.HideScalarBarIfNotNeeded(x_velocityLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
ablnek5000Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
ablnek5000Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'y_velocity'
y_velocityLUT = pv.GetColorTransferFunction('y_velocity')

# get opacity transfer function/opacity map for 'y_velocity'
y_velocityPWF = pv.GetOpacityTransferFunction('y_velocity')

# set scalar coloring
pv.ColorBy(ablnek5000Display, ('POINTS', 'z_velocity'))

# Hide the scalar bar for this color map if no visible data is colored by it.
pv.HideScalarBarIfNotNeeded(y_velocityLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
ablnek5000Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
ablnek5000Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'z_velocity'
z_velocityLUT = pv.GetColorTransferFunction('z_velocity')

# get opacity transfer function/opacity map for 'z_velocity'
z_velocityPWF = pv.GetOpacityTransferFunction('z_velocity')

# set scalar coloring
pv.ColorBy(ablnek5000Display, ('CELLS', 'vtkCompositeIndex'))

# Hide the scalar bar for this color map if no visible data is colored by it.
pv.HideScalarBarIfNotNeeded(z_velocityLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
ablnek5000Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
ablnek5000Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkCompositeIndex'
vtkCompositeIndexLUT = pv.GetColorTransferFunction('vtkCompositeIndex')

# get opacity transfer function/opacity map for 'vtkCompositeIndex'
vtkCompositeIndexPWF = pv.GetOpacityTransferFunction('vtkCompositeIndex')

# set scalar coloring
pv.ColorBy(ablnek5000Display, ('POINTS', 'velocity_mag'))

# Hide the scalar bar for this color map if no visible data is colored by it.
pv.HideScalarBarIfNotNeeded(vtkCompositeIndexLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
ablnek5000Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
ablnek5000Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'velocity_mag'
velocity_magLUT = pv.GetColorTransferFunction('velocity_mag')

# get opacity transfer function/opacity map for 'velocity_mag'
velocity_magPWF = pv.GetOpacityTransferFunction('velocity_mag')

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

# Properties modified on animationScene1
animationScene1.AnimationTime = 25.26755267805

# Properties modified on timeKeeper1
timeKeeper1.Time = 25.26755267805

# saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [1.5707999467849731, 0.5, 6.616070405485035]
renderView1.CameraFocalPoint = [1.5707999467849731, 0.5, 0.7853999733924866]
renderView1.CameraParallelScale = 1.8259971497854517

# uncomment the following to render all views
pv.RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
