#!/usr/bin/env python
import vtk
from vtk.test import Testing
from vtk.util.misc import vtkGetDataRoot
VTK_DATA_ROOT = vtkGetDataRoot()

ren1 = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.SetMultiSamples(0)
renWin.AddRenderer(ren1)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
# read data
reader = vtk.vtkMultiBlockPLOT3DReader()
reader.SetXYZFileName("" + str(VTK_DATA_ROOT) + "/Data/combxyz.bin")
reader.SetQFileName("" + str(VTK_DATA_ROOT) + "/Data/combq.bin")
reader.SetScalarFunctionNumber(110)
reader.Update()
output = reader.GetOutput().GetBlock(0)
# create outline
outlineF = vtk.vtkStructuredGridOutlineFilter()
outlineF.SetInputData(output)
outlineMapper = vtk.vtkPolyDataMapper()
outlineMapper.SetInputConnection(outlineF.GetOutputPort())
outline = vtk.vtkActor()
outline.SetMapper(outlineMapper)
outline.GetProperty().SetColor(0,0,0)
# create cursor
cursor = vtk.vtkCursor3D()
cursor.SetModelBounds(output.GetBounds())
cursor.SetFocalPoint(output.GetCenter())
cursor.AllOff()
cursor.AxesOn()
cursor.OutlineOn()
cursor.XShadowsOn()
cursor.YShadowsOn()
cursor.ZShadowsOn()
cursorMapper = vtk.vtkPolyDataMapper()
cursorMapper.SetInputConnection(cursor.GetOutputPort())
cursorActor = vtk.vtkActor()
cursorActor.SetMapper(cursorMapper)
cursorActor.GetProperty().SetColor(1,0,0)
# create probe
probe = vtk.vtkProbeFilter()
probe.SetInputData(cursor.GetFocus())
probe.SetSourceData(output)
# create a cone geometry for glyph
cone = vtk.vtkConeSource()
cone.SetResolution(16)
cone.SetRadius(0.25)
# create glyph
glyph = vtk.vtkGlyph3D()
glyph.SetInputConnection(probe.GetOutputPort())
glyph.SetSourceConnection(cone.GetOutputPort())
glyph.SetVectorModeToUseVector()
glyph.SetScaleModeToScaleByScalar()
glyph.SetScaleFactor(.0002)
glyphMapper = vtk.vtkPolyDataMapper()
glyphMapper.SetInputConnection(glyph.GetOutputPort())
glyphActor = vtk.vtkActor()
glyphActor.SetMapper(glyphMapper)
ren1.AddActor(outline)
ren1.AddActor(cursorActor)
ren1.AddActor(glyphActor)
ren1.SetBackground(1.0,1.0,1.0)
renWin.SetSize(200,200)
ren1.ResetCamera()
ren1.GetActiveCamera().Elevation(60)
ren1.ResetCameraClippingRange()
renWin.Render()
iren.Initialize()
# prevent the tk window from showing up then start the event loop
# --- end of script --