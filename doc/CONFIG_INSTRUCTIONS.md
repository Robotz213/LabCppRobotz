## Instruções de Configuração

Para compilar o seu módulo, certifique-se de ter o CMake e o pybind11 instalados. Siga os passos abaixo:

1. Crie um diretório de build:

```
mkdir build
cd build
```

3. Execute o CMake para configurar o projeto:

```
cmake ..
```

4. Compile o projeto:

```
make
```

Caso não esteja no Linux, use o [build.py](./build.py) para facilitar!

### Instruções de Compilação (Apenas Windows):

```sh

python build.py --msvc # Caso queria compilar usando o MSVC do Visual Studio

# Ou

python build.py --msys2 # Caso queria compilar usando o MSYS2 (Requer instalação do MSYS2)

```
