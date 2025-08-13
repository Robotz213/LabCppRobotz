import argparse
import subprocess
import sys


def build_msvc():
    cmd = [
        "cmake",
        "-G",
        "Visual Studio 17 2022",
        "-A",
        "x64",
        "-S",
        ".",
        "-B",
        "build",
        "-DPYBIND11_FINDPYTHON=ON",
        f"-DPython3_EXECUTABLE={sys.executable}",
        "-DCMAKE_CXX_STANDARD=17",
    ]
    try:
        subprocess.check_call(cmd)
        subprocess.check_call(
            [
                "cmake",
                "--build",
                "build",
                "--config",
                "Release",
                "--target",
                "lab_robotz",
            ]
        )
    except subprocess.CalledProcessError as e:
        print(f"Error during build: {e}")
        sys.exit(e.returncode)


def build_msys2():
    cmd = [
        "cmake",
        "-G",
        "Ninja",
        "-S",
        ".",
        "-B",
        "build",
        "-DPYBIND11_FINDPYTHON=ON",
        f"-DPython3_EXECUTABLE={sys.executable}",
        "-DCMAKE_CXX_STANDARD=17",
    ]
    subprocess.check_call(cmd)
    subprocess.check_call(
        ["cmake", "--build", "build", "--config", "Release", "--target", "lab_robotz"]
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build lab_robotz with MSVC or MSYS2")
    parser.add_argument(
        "--msvc", action="store_true", help="Build with MSVC (Visual Studio)"
    )
    parser.add_argument(
        "--msys2", action="store_true", help="Build with MSYS2 (Ninja/MinGW)"
    )
    args = parser.parse_args()

    if args.msvc:
        build_msvc()
    elif args.msys2:
        build_msys2()
    else:
        print("Escolha --msvc ou --msys2")
        sys.exit(1)
