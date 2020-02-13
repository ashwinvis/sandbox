# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
ablnek5000 = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1600, 766]

# get display properties
ablnek5000Display = GetDisplayProperties(ablnek5000, view=renderView1)

# change representation type
ablnek5000Display.SetRepresentationType('Points')

# change representation type
ablnek5000Display.SetRepresentationType('Volume')

# change representation type
ablnek5000Display.SetRepresentationType('Surface')

# create a new 'Slice'
slice1 = Slice(Input=ablnek5000)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [1.5707999467849731, 0.5, 0.7853999733924866]

# hide data in view
Hide(ablnek5000, renderView1)

# set active source
SetActiveSource(slice1)

# show data in view
slice1Display = Show(slice1, renderView1)

# get color transfer function/color map for 'x_velocity'
x_velocityLUT = GetColorTransferFunction('x_velocity')
x_velocityLUT.RGBPoints = [-0.20440159738063812, 0.231373, 0.298039, 0.752941, 0.604003019630909, 0.865003, 0.865003, 0.865003, 1.412407636642456, 0.705882, 0.0156863, 0.14902]
x_velocityLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'x_velocity']
slice1Display.LookupTable = x_velocityLUT
slice1Display.OSPRayScaleArray = 'x_velocity'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.15707999467849731
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.GaussianRadius = 0.007853999733924866
slice1Display.SetScaleArray = ['POINTS', 'x_velocity']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'x_velocity']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-0.003819699864834547, 0.0, 0.5, 0.0, 1.2901712656021118, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-0.003819699864834547, 0.0, 0.5, 0.0, 1.2901712656021118, 1.0, 0.5, 0.0]

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# get opacity transfer function/opacity map for 'x_velocity'
x_velocityPWF = GetOpacityTransferFunction('x_velocity')
x_velocityPWF.Points = [-0.20440159738063812, 0.0, 0.5, 0.0, 1.412407636642456, 1.0, 0.5, 0.0]
x_velocityPWF.ScalarRangeInitialized = 1

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.17132695034923556, 0.039455994487399705, -0.9844238419415902]

# show data in view
slice1Display = Show(slice1, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# hide data in view
Hide(ablnek5000, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# update the view to ensure updated data information
renderView1.Update()

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.Play()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

animationScene1.Play()

animationScene1.Play()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

animationScene1.Play()

animationScene1.Play()

animationScene1.Play()

# get color legend/bar for x_velocityLUT in view renderView1
x_velocityLUTColorBar = GetScalarBar(x_velocityLUT, renderView1)
x_velocityLUTColorBar.Title = 'x_velocity'
x_velocityLUTColorBar.ComponentTitle = ''

# change scalar bar placement
x_velocityLUTColorBar.WindowLocation = 'AnyLocation'
x_velocityLUTColorBar.Position = [0.91875, 0.4373368146214099]
x_velocityLUTColorBar.ScalarBarLength = 0.33000000000000024

# change scalar bar placement
x_velocityLUTColorBar.Position = [0.91875, 0.23107049608355093]
x_velocityLUTColorBar.ScalarBarLength = 0.5362663185378592

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
x_velocityLUT.ApplyPreset('Inferno (matplotlib)', True)

# rescale color and/or opacity maps used to exactly fit the current data range
slice1Display.RescaleTransferFunctionToDataRange(False, True)

animationScene1.Play()

animationScene1.Play()

animationScene1.Play()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToFirst()

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

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

# create a new 'Slice'
slice2 = Slice(Input=slice1)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [1.5707999467849731, 0.5, 0.7853999733924866]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.5707999467849731, 0.5, 0.6749051990182937]

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [1.5707999467849731, 0.01, 0.7853999733924866]
slice2.SliceType.Normal = [0.0, 1.0, 0.0]

# show data in view
slice2Display = Show(slice2, renderView1)

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = ['POINTS', 'x_velocity']
slice2Display.LookupTable = x_velocityLUT
slice2Display.OSPRayScaleArray = 'x_velocity'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'None'
slice2Display.ScaleFactor = 0.31415998935699463
slice2Display.SelectScaleArray = 'None'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'None'
slice2Display.GaussianRadius = 0.01570799946784973
slice2Display.SetScaleArray = ['POINTS', 'x_velocity']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'x_velocity']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [0.4729827344417572, 0.0, 0.5, 0.0, 0.6250284314155579, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [0.4729827344417572, 0.0, 0.5, 0.0, 0.6250284314155579, 1.0, 0.5, 0.0]

# hide data in view
Hide(slice1, renderView1)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(slice1)

# show data in view
slice1Display = Show(slice1, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(slice2, renderView1)

# set active source
SetActiveSource(slice2)

# show data in view
slice2Display = Show(slice2, renderView1)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(ablnek5000)

# show data in view
ablnek5000Display = Show(ablnek5000, renderView1)

# show color bar/color legend
ablnek5000Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(ablnek5000, renderView1)

# show data in view
ablnek5000Display = Show(ablnek5000, renderView1)

# show color bar/color legend
ablnek5000Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on ablnek5000
ablnek5000.PointArrays = ['x_velocity', 'y_velocity']

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
x_velocityLUT.RescaleTransferFunction(-0.020675310865044594, 1.1528749465942383)

# Rescale transfer function
x_velocityPWF.RescaleTransferFunction(-0.020675310865044594, 1.1528749465942383)

# set active source
SetActiveSource(slice2)

# hide data in view
Hide(ablnek5000, renderView1)

# set scalar coloring
ColorBy(slice2Display, ('POINTS', 'y_velocity'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(x_velocityLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'y_velocity'
y_velocityLUT = GetColorTransferFunction('y_velocity')
y_velocityLUT.RGBPoints = [-0.00884238164871931, 0.231373, 0.298039, 0.752941, 0.005726418923586607, 0.865003, 0.865003, 0.865003, 0.020295219495892525, 0.705882, 0.0156863, 0.14902]
y_velocityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'y_velocity'
y_velocityPWF = GetOpacityTransferFunction('y_velocity')
y_velocityPWF.Points = [-0.00884238164871931, 0.0, 0.5, 0.0, 0.020295219495892525, 1.0, 0.5, 0.0]
y_velocityPWF.ScalarRangeInitialized = 1

# hide data in view
Hide(slice1, renderView1)

# set active source
SetActiveSource(slice1)

# show data in view
slice1Display = Show(slice1, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(slice2)

# rescale color and/or opacity maps used to exactly fit the current data range
slice2Display.RescaleTransferFunctionToDataRange(False, True)

# get color legend/bar for y_velocityLUT in view renderView1
y_velocityLUTColorBar = GetScalarBar(y_velocityLUT, renderView1)
y_velocityLUTColorBar.Title = 'y_velocity'
y_velocityLUTColorBar.ComponentTitle = ''

# change scalar bar placement
y_velocityLUTColorBar.WindowLocation = 'AnyLocation'
y_velocityLUTColorBar.Position = [0.773125, 0.33812010443864227]
y_velocityLUTColorBar.ScalarBarLength = 0.3300000000000006

# set active source
SetActiveSource(ablnek5000)

# Properties modified on ablnek5000
ablnek5000.PointArrays = ['velocity_mag', 'x_velocity', 'y_velocity', 'z_velocity']

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(slice2)

# set scalar coloring
ColorBy(slice2Display, ('POINTS', 'velocity_mag'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(y_velocityLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'velocity_mag'
velocity_magLUT = GetColorTransferFunction('velocity_mag')
velocity_magLUT.RGBPoints = [0.4753826856613159, 0.231373, 0.298039, 0.752941, 0.5517241358757019, 0.865003, 0.865003, 0.865003, 0.6280655860900879, 0.705882, 0.0156863, 0.14902]
velocity_magLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'velocity_mag'
velocity_magPWF = GetOpacityTransferFunction('velocity_mag')
velocity_magPWF.Points = [0.4753826856613159, 0.0, 0.5, 0.0, 0.6280655860900879, 1.0, 0.5, 0.0]
velocity_magPWF.ScalarRangeInitialized = 1

# set active source
SetActiveSource(slice1)

# hide data in view
Hide(slice2, renderView1)

# show data in view
slice1Display = Show(slice1, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# destroy slice2
Delete(slice2)
del slice2

# set active source
SetActiveSource(ablnek5000)

# create a new 'Slice'
slice2 = Slice(Input=ablnek5000)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [1.5707999467849731, 0.5, 0.7853999733924866]

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [1.5707999467849731, 0.01, 0.7853999733924866]
slice2.SliceType.Normal = [0.0, 1.0, 0.0]

# show data in view
slice2Display = Show(slice2, renderView1)

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = ['POINTS', 'x_velocity']
slice2Display.LookupTable = x_velocityLUT
slice2Display.OSPRayScaleArray = 'velocity_mag'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'None'
slice2Display.ScaleFactor = 0.31415998935699463
slice2Display.SelectScaleArray = 'None'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'None'
slice2Display.GaussianRadius = 0.01570799946784973
slice2Display.SetScaleArray = ['POINTS', 'velocity_mag']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'velocity_mag']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [0.28490254282951355, 0.0, 0.5, 0.0, 0.9582680463790894, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [0.28490254282951355, 0.0, 0.5, 0.0, 0.9582680463790894, 1.0, 0.5, 0.0]

# hide data in view
Hide(ablnek5000, renderView1)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(slice2Display, ('POINTS', 'y_velocity'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(x_velocityLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(slice2Display, ('POINTS', 'velocity_mag'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(y_velocityLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
velocity_magLUT.ApplyPreset('Inferno (matplotlib)', True)

animationScene1.Play()

animationScene1.Play()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
velocity_magLUT.ApplyPreset('Viridis (matplotlib)', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
velocity_magLUT.ApplyPreset('Viridis (matplotlib)', True)

animationScene1.Play()

# Properties modified on renderView1
renderView1.EnableRayTracing = 1

# Properties modified on renderView1
renderView1.EnableRayTracing = 0

animationScene1.Play()

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 1

# set active source
SetActiveSource(slice1)

animationScene1.Play()

# change scalar bar placement
x_velocityLUTColorBar.Position = [0.91875, 0.48172323759791125]
x_velocityLUTColorBar.ScalarBarLength = 0.2856135770234989

# get color legend/bar for velocity_magLUT in view renderView1
velocity_magLUTColorBar = GetScalarBar(velocity_magLUT, renderView1)
velocity_magLUTColorBar.Title = 'velocity_mag'
velocity_magLUTColorBar.ComponentTitle = ''

# change scalar bar placement
velocity_magLUTColorBar.WindowLocation = 'AnyLocation'
velocity_magLUTColorBar.Position = [0.84875, 0.0757180156657963]
velocity_magLUTColorBar.ScalarBarLength = 0.33000000000000007

# change scalar bar placement
x_velocityLUTColorBar.Position = [0.8475, 0.6344647519582245]

# change scalar bar placement
x_velocityLUTColorBar.Position = [0.8475, 0.5639686684073106]
x_velocityLUTColorBar.ScalarBarLength = 0.35610966057441273

# change scalar bar placement
velocity_magLUTColorBar.ScalarBarLength = 0.3378328981723212

# set active source
SetActiveSource(slice2)

# set active source
SetActiveSource(slice1)

# set active source
SetActiveSource(slice2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice2.SliceType)

# set active source
SetActiveSource(slice1)

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'velocity_mag'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(x_velocityLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

animationScene1.Play()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
velocity_magLUT.ApplyPreset('Inferno (matplotlib)', True)

animationScene1.Play()

# change scalar bar placement
velocity_magLUTColorBar.Position = [0.84, 0.3746736292428198]
velocity_magLUTColorBar.ScalarBarLength = 0.3378328981723211

# change scalar bar placement
velocity_magLUTColorBar.Position = [0.845, 0.4686684073107049]
velocity_magLUTColorBar.ScalarBarLength = 0.3378328981723211

# change scalar bar placement
velocity_magLUTColorBar.Position = [0.845, 0.17232375979112263]
velocity_magLUTColorBar.ScalarBarLength = 0.6341775456919034

# change scalar bar placement
velocity_magLUTColorBar.Position = [0.86125, 0.17101827676240194]

# set active source
SetActiveSource(slice2)

# change representation type
slice2Display.SetRepresentationType('Feature Edges')

# change representation type
slice2Display.SetRepresentationType('Outline')

# change representation type
slice2Display.SetRepresentationType('Surface')

animationScene1.Play()

animationScene1.Play()

animationScene1.Play()

# current camera placement for renderView1
renderView1.CameraPosition = [-0.9822951325919982, 1.1848495978723956, 4.047228935416691]
renderView1.CameraFocalPoint = [1.5708000063896128, 0.5000000111758728, 0.6749051990182976]
renderView1.CameraViewUp = [0.12697982346876804, 0.9864182330446559, -0.10418826204952002]
renderView1.CameraParallelScale = 2.377237893433979

# save screenshot
SaveScreenshot('/home/avmo/test.png', renderView1, ImageResolution=[1600, 766])

# current camera placement for renderView1
renderView1.CameraPosition = [-0.9822951325919982, 1.1848495978723956, 4.047228935416691]
renderView1.CameraFocalPoint = [1.5708000063896128, 0.5000000111758728, 0.6749051990182976]
renderView1.CameraViewUp = [0.12697982346876804, 0.9864182330446559, -0.10418826204952002]
renderView1.CameraParallelScale = 2.377237893433979

# save screenshot
SaveScreenshot('/home/avmo/test.png', renderView1, ImageResolution=[1600, 766],
    OverrideColorPalette='WhiteBackground',
    TransparentBackground=1)

# change scalar bar placement
velocity_magLUTColorBar.Position = [0.91375, 0.2271540469973889]

# reset view to fit data bounds
renderView1.ResetCamera(0.0, 3.1415998935699463, 0.009999999776482582, 0.009999999776482582, 0.0, 1.5707999467849731)

# reset view to fit data bounds
renderView1.ResetCamera(0.0, 3.1415998935699463, 0.009999999776482582, 0.009999999776482582, 0.0, 1.5707999467849731)

# reset view to fit data
renderView1.ResetCamera()

# change scalar bar placement
velocity_magLUTColorBar.Position = [0.8818749999999999, 0.19321148825065254]

# current camera placement for renderView1
renderView1.CameraPosition = [-1.4110599240121353, 1.6635431993724699, 5.237588577663701]
renderView1.CameraFocalPoint = [-0.1661870127047389, 1.0957315238271137, 3.4956697250953246]
renderView1.CameraViewUp = [0.23385199703785217, 0.9521072365061712, -0.1969899836895019]
renderView1.CameraViewAngle = 20.475
renderView1.CameraParallelScale = 1.8259971497854517

# save screenshot
SaveScreenshot('/home/avmo/test.png', renderView1, ImageResolution=[1600, 766],
    OverrideColorPalette='WhiteBackground',
    TransparentBackground=1)