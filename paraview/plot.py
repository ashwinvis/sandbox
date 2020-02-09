# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'VisItNek5000Reader'
ablnek5000 = VisItNek5000Reader(FileName='/run/media/avmo/seagate/runs/abl_irrot_15x24x10_V1pix1.x1.571_2020-02-05_12-02-28/abl.nek5000')
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
# renderView1.ViewSize = [1600, 499]

# show data in view
ablnek5000Display = Show(ablnek5000, renderView1)

# trace defaults for the display properties.
ablnek5000Display.Representation = 'Surface'
ablnek5000Display.ColorArrayName = [None, '']
ablnek5000Display.OSPRayScaleArray = 'velocity_mag'
ablnek5000Display.OSPRayScaleFunction = 'PiecewiseFunction'
ablnek5000Display.SelectOrientationVectors = 'None'
ablnek5000Display.ScaleFactor = 0.31415998935699463
ablnek5000Display.SelectScaleArray = 'None'
ablnek5000Display.GlyphType = 'Arrow'
ablnek5000Display.GlyphTableIndexArray = 'None'
ablnek5000Display.GaussianRadius = 0.01570799946784973
ablnek5000Display.SetScaleArray = ['POINTS', 'velocity_mag']
ablnek5000Display.ScaleTransferFunction = 'PiecewiseFunction'
ablnek5000Display.OpacityArray = ['POINTS', 'velocity_mag']
ablnek5000Display.OpacityTransferFunction = 'PiecewiseFunction'
ablnek5000Display.DataAxesGrid = 'GridAxesRepresentation'
ablnek5000Display.PolarAxes = 'PolarAxesRepresentation'
ablnek5000Display.ScalarOpacityUnitDistance = 0.03404065311696019
ablnek5000Display.ExtractedBlockIndex = 2

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ablnek5000Display.ScaleTransferFunction.Points = [0.0010371223324909806, 0.0, 0.5, 0.0, 1.412827968597412, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ablnek5000Display.OpacityTransferFunction.Points = [0.0010371223324909806, 0.0, 0.5, 0.0, 1.412827968597412, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(ablnek5000Display, ('POINTS', 'velocity_mag'))

# rescale color and/or opacity maps used to include current data range
ablnek5000Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
ablnek5000Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'velocity_mag'
velocity_magLUT = GetColorTransferFunction('velocity_mag')
velocity_magLUT.RGBPoints = [0.0010371223324909806, 0.231373, 0.298039, 0.752941, 0.7069325454649515, 0.865003, 0.865003, 0.865003, 1.412827968597412, 0.705882, 0.0156863, 0.14902]
velocity_magLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'velocity_mag'
velocity_magPWF = GetOpacityTransferFunction('velocity_mag')
velocity_magPWF.Points = [0.0010371223324909806, 0.0, 0.5, 0.0, 1.412827968597412, 1.0, 0.5, 0.0]
velocity_magPWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
velocity_magLUT.ApplyPreset('Inferno (matplotlib)', True)

# get color legend/bar for velocity_magLUT in view renderView1
velocity_magLUTColorBar = GetScalarBar(velocity_magLUT, renderView1)
velocity_magLUTColorBar.Title = 'velocity_mag'
velocity_magLUTColorBar.ComponentTitle = ''

# change scalar bar placement
velocity_magLUTColorBar.WindowLocation = 'AnyLocation'
velocity_magLUTColorBar.Position = [0.9087500000000001, 0.5390781563126252]
velocity_magLUTColorBar.ScalarBarLength = 0.3300000000000002

# change scalar bar placement
velocity_magLUTColorBar.Position = [0.9087500000000001, 0.13827655310621242]
velocity_magLUTColorBar.ScalarBarLength = 0.7308016032064131

# Rescale transfer function
velocity_magLUT.RescaleTransferFunction(0.0010371223324909806, 1.0)

# Rescale transfer function
velocity_magPWF.RescaleTransferFunction(0.0010371223324909806, 1.0)

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

# rescale color and/or opacity maps used to exactly fit the current data range
ablnek5000Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
velocity_magLUT.RescaleTransferFunction(0.003677219618111849, 1.1)

# Rescale transfer function
velocity_magPWF.RescaleTransferFunction(0.003677219618111849, 1.1)

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

# current camera placement for renderView1
renderView1.CameraPosition = [1.5707999467849731, 0.5, 4.076661427044123]
renderView1.CameraFocalPoint = [1.5707999467849731, 0.5, 0.7853999733924866]
renderView1.CameraParallelScale = 1.8259971497854517

# save animation
SaveAnimation('/home/avmo/anim.avi', renderView1, ImageResolution=[1600, 496],
    FrameWindow=[0, 35])

# current camera placement for renderView1
renderView1.CameraPosition = [1.5707999467849731, 0.5, 4.076661427044123]
renderView1.CameraFocalPoint = [1.5707999467849731, 0.5, 0.7853999733924866]
renderView1.CameraParallelScale = 1.8259971497854517

# save screenshot
SaveScreenshot('/home/avmo/test.png', renderView1, ImageResolution=[1600, 499],
    OverrideColorPalette='WhiteBackground')

# create a new 'Contour'
contour1 = Contour(Input=ablnek5000)
contour1.ContourBy = ['POINTS', 'velocity_mag']
contour1.Isosurfaces = [0.5744097200222313]
contour1.PointMergeMethod = 'Uniform Binning'

# set active source
SetActiveSource(contour1)

# show data in view
contour1Display = Show(contour1, renderView1)

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'velocity_mag']
contour1Display.LookupTable = velocity_magLUT
contour1Display.OSPRayScaleArray = 'velocity_mag'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 0.31415998935699463
contour1Display.SelectScaleArray = 'velocity_mag'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'velocity_mag'
contour1Display.GaussianRadius = 0.01570799946784973
contour1Display.SetScaleArray = ['POINTS', 'velocity_mag']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'velocity_mag']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [0.5744097232818604, 0.0, 0.5, 0.0, 0.5745317935943604, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [0.5744097232818604, 0.0, 0.5, 0.0, 0.5745317935943604, 1.0, 0.5, 0.0]

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(contour1)

# Properties modified on contour1
contour1.Isosurfaces = [0.5744097200222313, 0.6, 0.7]

# show data in view
contour1Display = Show(contour1, renderView1)

# hide data in view
Hide(ablnek5000, renderView1)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

# Properties modified on contour1
contour1.Isosurfaces = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on contour1
contour1.Isosurfaces = [0.5, 0.6, 0.7, 0.8, 1.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on contour1
contour1.Isosurfaces = [0.5, 0.6, 0.7, 0.8]

# update the view to ensure updated data information
renderView1.Update()

# rescale color and/or opacity maps used to exactly fit the current data range
contour1Display.RescaleTransferFunctionToDataRange(False, True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
velocity_magLUT.ApplyPreset('Blue - Green - Orange', True)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-1.6875604765529497, 0.038918879069371595, 0.7316086373133374]
renderView1.CameraFocalPoint = [1.5707999467849698, 0.5000000000000017, 0.7853999733924854]
renderView1.CameraViewUp = [-0.13953088246781328, 0.9897150358084863, -0.031548070184405475]
renderView1.CameraParallelScale = 1.8259971497854517

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).