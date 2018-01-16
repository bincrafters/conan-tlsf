project(conan-tlsf)
cmake_minimum_required(VERSION 2.8.11)

## Conan Setup #################################################################
include(conanbuildinfo.cmake)
conan_basic_setup()

## General settings ############################################################
set(TLSF_VERSION_MAJOR 3)
set(TLSF_VERSION_MINOR 1)

set(WINDOWS_EXPORT_ALL_SYMBOLS TRUE)

## Build tlsf library #########################################################
set(TLSF_TARGET tlsf)
set(TLSF_SOURCE_FILES ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/tlsf.c
                      ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/tlsf.h)

add_library(${TLSF_TARGET} ${TLSF_SOURCE_FILES})
target_link_libraries(${TLSF_TARGET} ${CONAN_LIBS})
#target_include_directories(${TLSF_TARGET} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/include)
set_property(TARGET ${TLSF_TARGET} PROPERTY C_STANDARD 99)

# Install ######################################################################
install(TARGETS ${TLSF_TARGET}
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)
        
install(DIRECTORY source_subfolder/
        DESTINATION include
        FILES_MATCHING PATTERN "*.h"
  )
