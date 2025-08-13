cmake_minimum_required(VERSION 3.15)
project(lab_robotz LANGUAGES CXX)

# Define padrão de compilação
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Faz o pybind11 usar o FindPython moderno
set(PYBIND11_FINDPYTHON ON)

# Define explicitamente o Python (substitua pelo caminho que quer usar por padrão)
set(Python3_EXECUTABLE "C:/Python313/python.exe" CACHE FILEPATH "Path to Python executable")

# Acha Python e pybind11
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

# Cria o módulo
pybind11_add_module(lab_robotz main.cpp)
