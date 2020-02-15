# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'VisItNek5000Reader'
ablnek5000 = VisItNek5000Reader(FileName='/home/avmo/src/exabl/data/abl_rot_15x24x10_V1pix1.x1.571_2020-02-09_17-38-37/abl.nek5000')
ablnek5000.Meshes = ['mesh']
ablnek5000.PointArrays = []

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on ablnek5000
ablnek5000.PointArrays = ['velocity_mag']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [689, 499]


# reset view to fit data
renderView1.ResetCamera()

# current camera placement for renderView1
renderView1.CameraPosition = [1.5430590649448526, 6.463304979594418, 4.555389168383411]
renderView1.CameraFocalPoint = [1.5707999467849734, 0.5, 0.7853999733924866]
renderView1.CameraViewUp = [0.018053943395482774, 0.5343398685402572, -0.8450768959190954]
renderView1.CameraParallelScale = 1.8259971497854517

# get the material library
# materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(Input=ablnek5000)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.1, 0.0]
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# show data in view
slice1Display = Show(slice1, renderView1)

# trace defaults for the display properties.
# slice1Display.Representation = 'Surface'
# slice1Display.ColorArrayName = [None, '']
# slice1Display.OSPRayScaleArray = 'velocity_mag'
# slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
# slice1Display.SelectOrientationVectors = 'None'
# slice1Display.ScaleFactor = 0.31415998935699463
# slice1Display.SelectScaleArray = 'None'
# slice1Display.GlyphType = 'Arrow'
# slice1Display.GlyphTableIndexArray = 'None'
# slice1Display.GaussianRadius = 0.01570799946784973
# slice1Display.SetScaleArray = ['POINTS', 'velocity_mag']
# slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
# slice1Display.OpacityArray = ['POINTS', 'velocity_mag']
# slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
# slice1Display.DataAxesGrid = 'GridAxesRepresentation'
# slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# slice1Display.ScaleTransferFunction.Points = [0.583583652973175, 0.0, 0.5, 0.0, 1.1641210317611694, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# slice1Display.OpacityTransferFunction.Points = [0.583583652973175, 0.0, 0.5, 0.0, 1.1641210317611694, 1.0, 0.5, 0.0]

# hide data in view
Hide(ablnek5000, renderView1)

# update the view to ensure updated data information
# renderView1.Update()

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'velocity_mag'))

# rescale color and/or opacity maps used to include current data range
# slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
# slice1Display.SetScalarBarVisibility(renderView1, True)

# get opacity transfer function/opacity map for 'velocity_mag'
# velocity_magPWF = GetOpacityTransferFunction('velocity_mag')
# velocity_magPWF.Points = [0.583583652973175, 0.0, 0.5, 0.0, 1.1641210317611694, 1.0, 0.5, 0.0]
# velocity_magPWF.ScalarRangeInitialized = 1

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

#### saving camera placements for all active views


#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).