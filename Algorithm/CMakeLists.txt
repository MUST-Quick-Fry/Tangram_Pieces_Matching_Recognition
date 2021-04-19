cmake_minimum_required(VERSION 3.18.2)
project(Tangram)

set(CMAKE_CXX_STANDARD 14)

add_executable(Tangram main.cpp tangram.h dfs.cpp bfs.cpp IDA.cpp choose_mode.cpp collision_detect.cpp)