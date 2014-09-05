if (Module_vtkVolumeOpenGL2)
  set(VTK_RENDERING_VOLUME_BACKEND "vtkVolumeOpenGL2")
endif()

vtk_module(vtkRenderingVolume
  GROUPS
    Rendering
  DEPENDS
    vtkImagingCore
    vtkRenderingCore
  TEST_DEPENDS
    vtkTestingCore
    vtkTestingRendering
    vtkRenderingVolume${VTK_RENDERING_BACKEND}
    ${VTK_RENDERING_VOLUME_BACKEND}
    vtkRenderingFreeType
    vtkIOXML
    vtkImagingSources
    vtkImagingGeneral
    vtkImagingHybrid
    vtkInteractionStyle
    vtkIOLegacy
  KIT
    vtkRendering
  )
