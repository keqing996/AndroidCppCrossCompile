import logging
import subprocess

'''
All user configuration para
'''

# cmake.exe path
cmake_path: str = 'D:/Programmes/CMake/bin/cmake.exe'
# ndk base path
ndk_home: str = 'D:/Programmes/Android/ndk/android-ndk-r23c/'
# android target sdk version
system_version: str = '31'
# build abi
build_abi: str = 'arm64-v8a'
# build type
build_type: str = 'Debug'
# print cmake build detail
do_verbose_output: bool = False

'''
All needed configuration
'''

# ndk cmake tool chain path
ndk_cmake_toolchain: str = ndk_home + 'build/cmake/android.toolchain.cmake'
# ndk make.exe path
make_exe: str = ndk_home + 'prebuilt/windows-x86_64/bin/make.exe'
# ndk clang c compiler path
c_compiler: str = ndk_home + 'toolchains/llvm/prebuilt/windows-x86_64/bin/clang.exe'
# ndk clang c++ compiler path
cpp_compiler: str = ndk_home + 'toolchains/llvm/prebuilt/windows-x86_64/bin/clang++.exe'

'''
Cmake macro args
'''

# CMAKE_BUILD_TYPE - debug or release or somethine
arg_define_build_type: str = '-DCMAKE_BUILD_TYPE={}'.format(build_type)
# CMAKE_MAKE_PROGRAM - where ndk make.exe located
arg_define_make_exe: str = '-DCMAKE_MAKE_PROGRAM="{}"'.format(make_exe)
# CMAKE_C_COMPILER - where c compiler located
arg_define_c_compiler: str = '-DCMAKE_C_COMPILER="{}"'.format(c_compiler)
# CMAKE_CXX_COMPILER - where c++ compiler located
arg_define_cpp_compiler: str = '-DCMAKE_CXX_COMPILER="{}"'.format(cpp_compiler)
# CMAKE_ANDROID_NDK - where android ndk located
arg_define_ndk: str = '-DCMAKE_ANDROID_NDK="{}"'.format(ndk_home)
# CMAKE_TOOLCHAIN_FILE - where android ndk cmake toolchain located
arg_define_toolchain: str = '-DCMAKE_TOOLCHAIN_FILE="{}"'.format(ndk_cmake_toolchain)
# ANDROID_ABI - what target abi is
arg_define_abi: str = '-DANDROID_ABI="{}"'.format(build_abi)
# ANDROID_PLATFORM - what android sdk version is
arg_define_android_plat: str = '-DANDROID_PLATFORM={}'.format(system_version)
# DCMAKE_VERBOSE_MAKEFILE:BOOL - output build detail
arg_define_verbose_output: str = '-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON'

'''
Other generate cmake args
'''
# build system
arg_generator: str = '-G "MinGW Makefiles"'
# source path
arg_source_path: str = '-S "./"'
# build output dir
arg_build_dir: str = '-B "./build/"'


def run(args_list: list[str]) -> None:
    args: str = ' '.join(args_list)

    sub_proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_data, stderr_data = sub_proc.communicate()
    stdout_data = stdout_data.decode('utf-8')
    stderr_data = stderr_data.decode('utf-8')

    if stdout_data:
        logging.debug(stdout_data)
    if stderr_data:
        logging.warning(stderr_data)

    pass


def cmake_generate() -> None:
    args_list: list[str] = [cmake_path,
                            arg_define_build_type,
                            arg_define_make_exe,
                            arg_define_c_compiler,
                            arg_define_cpp_compiler,
                            arg_define_ndk,
                            arg_define_toolchain,
                            arg_define_abi,
                            arg_define_android_plat,
                            arg_generator,
                            arg_source_path,
                            arg_build_dir]

    if do_verbose_output:
        args_list.append(arg_define_verbose_output)

    run(args_list)
    pass
    

def cmake_build() -> None:
    args_list: list[str] = [cmake_path, '--build "./build/"', '--target all']
    run(args_list)
    pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    cmake_generate()
    cmake_build()
