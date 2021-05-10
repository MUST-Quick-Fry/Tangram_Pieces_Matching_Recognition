# Tangram Pieces Matching Recognition
Project of CO105 Fundamentals of Artificial Intelligence
# Authors
    CHEN YUXUAN 1809853J-I011-0011  
    HE PEILIN 1809853U-I011-0078  
    WANG YUYANG 1809853Z-I011-0045  
# Team cooperation
Tasks completed by each person are documented below:

|Name|	Task|
|--------|---------|
|CHEN YUXUAN	|Construct programme algorithm part, implement DFS, BFS and A* algorithm, implement SAT for detecting collision|
|WANG YUYANG	|Implement SA algorithm and GUI|
|HE PEILIN	|Report and README writing, presentation design , sub-implement GUI|
# Introduction
The tangram is a dissection puzzle consisting of seven flat pieces, which are put together to form shapes.
This programme implements 4 algorithms **DFS**, **BFS**, **A*** and **SA** to search the solution of all 13 convex polygons built from all the seven pieces. 

# Environment
The detailed information of programming environment are listed in table :
|Attribute|	Content|
|-----------|--------------------------------------|
|Programming Language|	**C++11** & **python** (3.9.0) |
|IDE | Visual Studio Code & PyCharm|
|Third-party libraries| PyQt 5.15.2 & pyqt5-tools 5.15.2.3.0.2|
|Supporting architecture| 32 & 64|

|Required DLL|`msvcp140d.dll` , `ucrtbased.dll` and `vcruntime140d.dll`|

# How to compile and execute

## Algorithm programme
For algorithm part, we use **C++11** because it has generic and functional features in addition to facilities for low-level memory manipulation.

Supporting ISO **C++11** language features and libraries., We tested compilation using **g++**(GNU C++ Compiler version 9.3.0), with commands as below :
```code
g++ −std=c++11 [CPPFILE] [−o EXE]
```
Besides, you can also use **CMake** with version 3.18.2 to build and run code, more details can be seen in `./Algorithm/CMakeLists.txt`.
## GUI programme
For GUI part, we use **Python** because high stability of libraries can easily encapsulate visual and interactive software.

Following template **PyInstaller** to create the execution, the command is used as below :
```code
pinstaller  [−F]  [−w]  [PYTHONMAINFILE]  [−p PYTHONPATH]  [−−hidden−import MODULENAME]  [−i .ico]
```
# Usage
There are software in encapsulation by source code in *Release* --- `./dist-x86` and `./dist-x64`.
We already download the required **DLL** files as listed in table, **DO NOT** remove or rename **DLL** files and the `Tangram.exe`.
> Please make sure your computer system architecture (64-bit  operating system or 32-bit operating system),
>  and then choose the corresponding directory


