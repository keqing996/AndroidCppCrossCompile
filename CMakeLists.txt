cmake_minimum_required(VERSION 3.26)

project(AndroidCpp)

file(GLOB_RECURSE SrcFiles src/*.cpp)

add_executable(hello_world ${SrcFiles})

# header path, CMAKE_ANDROID_NDK is defined in CMakePresets.json, points to ndk path
target_include_directories(hello_world PRIVATE
        "${CMAKE_ANDROID_NDK}/toolchains/llvm/prebuilt/windows-x86_64/sysroot/usr/include/")

# link log library
target_link_libraries(hello_world PRIVATE
        liblog.so
)