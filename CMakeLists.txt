cmake_minimum_required(VERSION 3.10)

project(rin-playground VERSION 1.0 LANGUAGES C)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if (NOT DEFINED BUNYAN_RIN_GENERATED_C)
    message(FATAL_ERROR "rin-playground must be built through bunyan.py in mode='rin'")
endif()
if (NOT DEFINED BUNYAN_RIN_COMPILER_DIR OR NOT DEFINED BUNYAN_RIN_STD_DIR)
    message(FATAL_ERROR "Bunyan could not resolve rin.exe on PATH")
endif()

add_executable(${PROJECT_NAME}
    ${BUNYAN_RIN_GENERATED_C}
    ${BUNYAN_RIN_GENERATED_H}
)

set_source_files_properties(${BUNYAN_RIN_GENERATED_C} PROPERTIES
    OBJECT_DEPENDS "${BUNYAN_RIN_ENTRY};${BUNYAN_RIN_GENERATED_H}"
)

target_include_directories(${PROJECT_NAME} PRIVATE
    ${BUNYAN_RIN_GEN_DIR}
    ${BUNYAN_RIN_COMPILER_DIR}
    ${BUNYAN_RIN_STD_DIR}
)
