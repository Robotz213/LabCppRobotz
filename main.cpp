#include <pybind11/pybind11.h>
#include <iostream>
namespace py = pybind11;

class SomeClass
{

    float multiplicador;

public:
    SomeClass(float multiplicador_) : multiplicador(multiplicador_) {};
    float multiplicar(float valor)
    {

        return multiplicador * valor;
    };
};

PYBIND11_MODULE(lab_robotz, handle)
{

    // Define a documentação do módulo Python
    handle.doc() = "Classe de multiplicação";

    // Expõe a classe SomeClass para Python como "PySomeCLass"
    py::class_<SomeClass>(
        handle, "PySomeClass")
        // Expõe o construtor que recebe um float
        .def(py::init<float>())
        // Expõe o método multiplicar como "multiply" em Python
        .def("multiply", &SomeClass::multiplicar);
}
