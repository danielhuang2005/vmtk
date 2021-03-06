set(vtkvmtkITK_TARGET_LINK_LIBRARIES ${ITK_LIBRARIES})

if( ${VTK_VERSION_MAJOR} GREATER 5 )
  set( vtkvmtkITK_COMPONENTS
    vtkIOImage
    vtkImagingCore
    )
  if (VTK_WRAP_PYTHON AND VTK_VMTK_WRAP_PYTHON)
    list(APPEND vtkvmtkITK_COMPONENTS
      vtkWrappingPythonCore
      )
  endif(VTK_WRAP_PYTHON AND VTK_VMTK_WRAP_PYTHON)
  find_package( VTK 6.2 COMPONENTS ${vtkvmtkITK_COMPONENTS} REQUIRED )
  include( ${VTK_USE_FILE} )
  list( APPEND vtkvmtkITK_TARGET_LINK_LIBRARIES ${VTK_LIBRARIES} )
else( ${VTK_VERSION_MAJOR} GREATER 5 )
  list( APPEND vtkvmtkITK_TARGET_LINK_LIBRARIES
    vtkImaging
    )
endif( ${VTK_VERSION_MAJOR} GREATER 5 )

# --------------------------------------------------------------------------
# Sources

# include a test for endianness (used to be done by default)
INCLUDE (${CMAKE_ROOT}/Modules/TestBigEndian.cmake)
TEST_BIG_ENDIAN(CMAKE_WORDS_BIGENDIAN)

SET(vtkvmtkITK_SRCS
    vtkvmtkITKArchetypeImageSeriesReader.cxx
    vtkvmtkITKArchetypeImageSeriesScalarReader.cxx
    vtkvmtkITKImageWriter.cxx
    vtkvmtkITKImageToImageFilter.h
    vtkvmtkITKImageToImageFilter2DFF.h
    vtkvmtkITKImageToImageFilterFF.h
)

SET(VTK_VMTK_ITK_EXTRA_INCLUDES
  vtkvmtkITK.h
  vtkvmtkITKUtility.h
)

# --------------------------------------------------------------------------
# Build the library

vmtk_build_library(
  NAME vtkvmtkITK
  SRCS ${vtkvmtkITK_SRCS} ${VTK_VMTK_ITK_EXTRA_INCLUDES}
  TARGET_LINK_LIBRARIES ${vtkvmtkITK_TARGET_LINK_LIBRARIES}
  )
