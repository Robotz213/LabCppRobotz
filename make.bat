cd C:\Github\LabCppRobotz
cmake -G "Visual Studio 17 2022" -A x64 -S . -B build ^
  -DPYBIND11_FINDPYTHON=ON ^
  -DPython3_EXECUTABLE=C:/Python313/python.exe ^
  -DCMAKE_CXX_STANDARD=17

cmake --build build --config Release --target lab_robotz
