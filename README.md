# Tangram Pieces Matching Recognition

<div align="center">
  
  [![description](https://img.shields.io/badge/project-Team-1F1F1F?style=for-the-badge)](https://github.com/MUST-Quick-Fry/Tangram_Pieces_Matching_Recognition)
  &nbsp;
  [![stars](https://img.shields.io/github/stars/MUST-Quick-Fry/Tangram_Pieces_Matching_Recognition?style=for-the-badge&color=FDEE21)](https://github.com/MUST-Quick-Fry/Tangram_Pieces_Matching_Recognition/stargazers)
  &nbsp;
  [![forks](https://img.shields.io/github/forks/MUST-Quick-Fry/Tangram_Pieces_Matching_Recognition?style=for-the-badge&color=white)](https://github.com/MUST-Quick-Fry/Tangram_Pieces_Matching_Recognition/forks)
  &nbsp;
  [![contributors](https://img.shields.io/github/contributors/MUST-Quick-Fry/Tangram_Pieces_Matching_Recognition?style=for-the-badge&color=8BC0D0)](https://github.com/MUST-Quick-Fry/Tangram_Pieces_Matching_Recognition/graphs/contributors)
  
  <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" />
  &nbsp;
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  &nbsp;
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" />
  &nbsp;
  <img src="https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white" />
  &nbsp;
  <img src="https://img.shields.io/badge/Visual_Studio-5C2D91?style=for-the-badge&logo=visual%20studio&logoColor=white" />
</div>

<br>

The tangram is a dissection puzzle consisting of seven flat pieces, which are put together to form shapes. This programme implements 4 algorithms **DFS**, **BFS**, **A*** and **SA** to search the solution of all 13 convex polygons built from all the seven pieces.



## Table of Contents

- [Development Environment](#development-environment)
- [Install](#install)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)



## Development Environment

|Attribute|	Content|
|-----------|--------------------------------------|
|Programming Language|	**C++11** & **python** (3.9.0) |
|IDE | Visual Studio Code & PyCharm|
|Third-party libraries| PyQt 5.15.2 & pyqt5-tools 5.15.2.3.0.2|
|Supporting architecture| 32 & 64|
|Required DLL|`msvcp140d.dll` , `ucrtbased.dll` and `vcruntime140d.dll`|



## Install

```
git clone https://github.com/MUST-Quick-Fry/Tangram_Pieces_Matching_Recognition
```



## Usage

### Algorithm programme
For algorithm part, we use **C++11** because it has generic and functional features in addition to facilities for low-level memory manipulation.

Supporting ISO **C++11** language features and libraries., We tested compilation using **g++**(GNU C++ Compiler version 9.3.0), with commands as below :
```code
g++ −std=c++11 [CPPFILE] [−o EXE]
```
Besides, you can also use **CMake** with version 3.18.2 to build and run code, more details can be seen in `./Algorithm/CMakeLists.txt`.
### GUI programme
For GUI part, we use **Python** because high stability of libraries can easily encapsulate visual and interactive software.

Following template **PyInstaller** to create the execution, the command is used as below :
```code
pinstaller  [−F]  [−w]  [PYTHONMAINFILE]  [−p PYTHONPATH]  [−−hidden−import MODULENAME]  [−i .ico]
```
### Executable
There are software in encapsulation by source code in *Release* --- `./dist-x86` and `./dist-x64`.
We already download the required **DLL** files as listed in table, **DO NOT** remove or rename **DLL** files and the `Tangram.exe`.
> Please make sure your computer system architecture (64-bit  operating system or 32-bit operating system),
>  and then choose the corresponding directory



## Maintainers

![badge](https://img.shields.io/badge/maintenance-NO-EF2D5E) [@goodkillerchen](https://github.com/goodkillerchen), [@KennardWang](https://github.com/KennardWang), [@Tim-eyes](https://github.com/Tim-eyes)



## Contributing

Tasks completed by each person are documented below:

|Name|Task|
|--------|---------|
|Chen, Yuxuan (1809853J-I011-0011)|Construct programme algorithm part, implement DFS, BFS and A* algorithm, implement SAT for detecting collision|
|Wang, Yuyang (1809853Z-I011-0045)|Implement SA algorithm and GUI|
|He, Peilin (1809853U-I011-0078)|Report and README writing, presentation design , sub-implement GUI|

Feel free to [open an issue](https://github.com/MUST-Quick-Fry/Tangram_Pieces_Matching_Recognition/issues) or submit [PRs](https://github.com/MUST-Quick-Fry/Tangram_Pieces_Matching_Recognition/pulls).



## License

[![license](https://img.shields.io/github/license/MUST-Quick-Fry/Tangram_Pieces_Matching_Recognition)](LICENSE) © MUST-Quick-Fry ( 2021.5.17 )
