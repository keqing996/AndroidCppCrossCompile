import logging
import subprocess

# All user configuration para
cmake_path: str = 'D:/Programmes/CMake/bin/cmake.exe'
ndk_base_path: str = 'D:/Programmes/Android/ndk/android-ndk-r23c/'
system_version: str = '33'
build_abi: str = 'arm64-v8a'
build_type: str = 'Debug'

# All needed configuration
ndk_cmake_toolchain: str = ndk_base_path + 'build/cmake/android.toolchain.cmake'
make_exe: str = ndk_base_path + 'prebuilt/windows-x86_64/bin/make.exe'
c_compiler: str = ndk_base_path + 'toolchains/llvm/prebuilt/windows-x86_64/bin/clang.exe'
cpp_compiler: str = ndk_base_path + 'toolchains/llvm/prebuilt/windows-x86_64/bin/clang++.exe'

# All cmake macro args
arg_define_build_type: str = '-DCMAKE_BUILD_TYPE={}'.format(build_type)
arg_define_make_exe: str = '-DCMAKE_MAKE_PROGRAM="{}"'.format(make_exe)
arg_define_c_compiler: str = '-DCMAKE_C_COMPILER="{}"'.format(c_compiler)
arg_define_cpp_compiler: str = '-DCMAKE_CXX_COMPILER="{}"'.format(cpp_compiler)
arg_define_ndk: str = '-DCMAKE_ANDROID_NDK="{}"'.format(ndk_base_path)
arg_define_toolchain: str = '-DCMAKE_TOOLCHAIN_FILE="{}"'.format(ndk_cmake_toolchain)
arg_define_toolchain_ver: str = '-DCMAKE_SYSTEM_NAME="clang"'
arg_define_system: str = '-DCMAKE_SYSTEM_NAME="Android"'
arg_define_abi:str = '-DANDROID_ABI="{}"'.format(build_abi)
arg_define_system_ver:str = '-DCMAKE_SYSTEM_VERSION={}'.format(system_version)

# Other generate cmake args
arg_generator: str = '-G "MinGW Makefiles"'
arg_source_path: str = '-S "./"'
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
    args_list: list[str] = []
    args_list.append(cmake_path)
    args_list.append(arg_define_build_type)
    args_list.append(arg_define_make_exe)
    args_list.append(arg_define_c_compiler)
    args_list.append(arg_define_cpp_compiler)
    args_list.append(arg_define_ndk)
    args_list.append(arg_define_toolchain)
    args_list.append(arg_define_toolchain_ver)
    args_list.append(arg_define_system)
    args_list.append(arg_define_abi)
    args_list.append(arg_define_system_ver)
    args_list.append(arg_generator)
    args_list.append(arg_source_path)
    args_list.append(arg_build_dir)
    run(args_list)
    pass
    

def cmake_build() -> None:
    args_list: list[str] = []
    args_list.append(cmake_path)
    args_list.append('--build "./build/"')
    args_list.append('--target all')
    run(args_list)
    pass

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    cmake_generate()
    cmake_build()
