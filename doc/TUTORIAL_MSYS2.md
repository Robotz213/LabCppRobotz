# Tutorial: Instalação e Configuração do MSYS2 para Compilar Projetos C/C++

Este manual apresenta um passo a passo para instalar e configurar o MSYS2 no Windows, focando na preparação do ambiente para compilar projetos C/C++ com suporte a diferentes sistemas de build, como Make e Ninja.

## Sumário

- [Introdução](#introdução)
- [Pré-requisitos](#pré-requisitos)
- [Instalação do MSYS2](#instalação-do-msys2)
- [Atualização do MSYS2](#atualização-do-msys2)
- [Instalação das Ferramentas de Desenvolvimento](#instalação-das-ferramentas-de-desenvolvimento)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Comandos de Build: Make e Ninja](#comandos-de-build-make-e-ninja)
- [Referências](#referências)

---

## Introdução

O MSYS2 é um ambiente de desenvolvimento para Windows que fornece ferramentas Unix e um gerenciador de pacotes eficiente. Ele facilita a compilação de projetos C/C++ e oferece suporte a diferentes sistemas de build.

## Pré-requisitos

- Windows 10 ou superior (64 bits)
- Acesso à internet
- Permissão de administrador para instalação

## Instalação do MSYS2

1. Acesse o site oficial: [https://www.msys2.org/](https://www.msys2.org/)
2. Baixe o instalador adequado para seu sistema (x86_64).
3. Execute o instalador e siga as instruções, preferencialmente instalando em `C:\msys64`.

## Atualização do MSYS2

Abra o terminal MSYS2 (MSYS2 MSYS) e execute:

```sh
pacman -Syu
```

Se solicitado, feche o terminal e abra novamente, então execute:

```sh
pacman -Su
```

## Instalação das Ferramentas de Desenvolvimento

No terminal MSYS2, instale os pacotes essenciais:

```sh
pacman -S --needed base-devel mingw-w64-x86_64-toolchain
```

Para utilizar diferentes sistemas de build, instale também o CMake, Ninja e Make:

```sh
pacman -S mingw-w64-x86_64-cmake mingw-w64-x86_64-ninja mingw-w64-x86_64-make
```

> **Dica:** Sempre utilize o terminal `MSYS2 MinGW 64-bit` para compilar projetos C/C++.

## Configuração do Ambiente

- Certifique-se de que o `cmake`, `ninja`, `make`, `g++` e demais ferramentas estejam acessíveis:

```sh
which cmake
which ninja
which make
which g++
```

- Adicione o caminho do MSYS2 MinGW 64-bit ao `PATH` do sistema, se necessário.

## Comandos de Build: Make e Ninja

### Usando Make

1. Gere os arquivos de build com CMake:

```sh
cmake -G "Unix Makefiles" -B build
```

2. Compile o projeto:

```sh
cmake --build build
```

### Usando Ninja

1. Gere os arquivos de build com CMake:

```sh
cmake -G Ninja -B build
```

2. Compile o projeto:

```sh
cmake --build build
```

## Referências

- [MSYS2](https://www.msys2.org/)
- [CMake](https://cmake.org/)
- [Ninja](https://ninja-build.org/)
