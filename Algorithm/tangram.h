//
// Created by ccyyxx on 4/15/21.
//
#ifndef TANGRAM_TANGRAM_H
#define TANGRAM_TANGRAM_H
#include<iostream>
#include <cmath>
#include <vector>
#define double long double
using namespace std;
constexpr double eps=1e-10;
class Point{
public:
    Point(double x,double y):x(x),y(y){}

    Point() = default;
    double x;
    double y;
    Point operator + (const Point &p) const{
        return Point(this->x+p.x,this->y+p.y);
    }
    Point operator - (const Point &p) const{
        return Point(this->x-p.x,this->y-p.y);
    }
    friend ostream& operator << (ostream &out, const Point &p){
        out << p.y << p.x;
        return out;
    }
};
double Dot(Point A,Point B);
double Length(Point A);
Point Normal(Point A);
class Shape{
public:
    Shape(Point Mass_point): Mass_point(Mass_point){};
    Point Mass_point;
    vector<Point> v;
    vector<Point> n;
    friend ostream& operator << (ostream &out, const Shape &s){
        for(auto it:s.v){
            out<<it;
        }
        return out;
    }
};
Point Project(const Shape &s,const Point &n);
class BigTriangle: public Shape{
public:
    BigTriangle(Point Mass_point,int pos): Shape(Mass_point){
        switch (pos) {
            case 0:
                v.emplace_back(Mass_point.x-1,Mass_point.y);
                v.emplace_back(Mass_point.x+1,Mass_point.y-2);
                v.emplace_back(Mass_point.x+1,Mass_point.y+2);
                break;
            case 1:
                v.emplace_back(Mass_point.x,Mass_point.y+1);
                v.emplace_back(Mass_point.x-2,Mass_point.y-1);
                v.emplace_back(Mass_point.x+2,Mass_point.y-1);
                break;
            case 2:
                v.emplace_back(Mass_point.x+1,Mass_point.y);
                v.emplace_back(Mass_point.x-1,Mass_point.y+2);
                v.emplace_back(Mass_point.x-1,Mass_point.y-2);
                break;
            case 3:
                v.emplace_back(Mass_point.x,Mass_point.y-1);
                v.emplace_back(Mass_point.x+2,Mass_point.y+1);
                v.emplace_back(Mass_point.x-2,Mass_point.y+1);
                break;
            default:
                break;
        }
        for(int i=0;i<3;i++){
            n.emplace_back(Normal(v[(i+1)%3]-v[i]));
        }
    }
};
class MidTriangle: public Shape{
public:
    MidTriangle(Point Mass_point,int pos): Shape(Mass_point){
        v.emplace_back(Mass_point);
        switch (pos) {
            case 0:
                v.emplace_back(Mass_point.x,Mass_point.y+2);
                v.emplace_back(Mass_point.x-2,Mass_point.y);
                break;
            case 1:
                v.emplace_back(Mass_point.x+2,Mass_point.y);
                v.emplace_back(Mass_point.x,Mass_point.y+2);
                break;
            case 2:
                v.emplace_back(Mass_point.x,Mass_point.y-2);
                v.emplace_back(Mass_point.x+2,Mass_point.y);
                break;
            case 3:
                v.emplace_back(Mass_point.x-2,Mass_point.y);
                v.emplace_back(Mass_point.x,Mass_point.y-2);
                break;
            default:
                break;
        }
        for(int i=0;i<3;i++){
            n.emplace_back(Normal(v[(i+1)%3]-v[i]));
        }
    }
};
class SmallTriangle: public Shape{
public:
    SmallTriangle(Point Mass_point,int pos): Shape(Mass_point){
        v.emplace_back(Mass_point);
        switch (pos) {
            case 0:
                v.emplace_back(Mass_point.x+1,Mass_point.y-1);
                v.emplace_back(Mass_point.x+1,Mass_point.y+1);
                break;
            case 1:
                v.emplace_back(Mass_point.x-1,Mass_point.y-1);
                v.emplace_back(Mass_point.x+1,Mass_point.y-1);
                break;
            case 2:
                v.emplace_back(Mass_point.x-1,Mass_point.y+1);
                v.emplace_back(Mass_point.x-1,Mass_point.y-1);
                break;
            case 3:
                v.emplace_back(Mass_point.x+1,Mass_point.y+1);
                v.emplace_back(Mass_point.x-1,Mass_point.y+1);
                break;
            default:
                break;
        }
        for(int i=0;i<3;i++){
            n.emplace_back(Normal(v[(i+1)%3]-v[i]));
        }
    }
};
class Square: public Shape{
public:
    explicit Square(Point Mass_point):Shape(Mass_point){
        v.emplace_back(Mass_point.x-1,Mass_point.y);
        v.emplace_back(Mass_point.x,Mass_point.y-1);
        v.emplace_back(Mass_point.x+1,Mass_point.y);
        v.emplace_back(Mass_point.x,Mass_point.y+1);
        for(int i=0;i<4;i++){
            n.emplace_back(Normal(v[(i+1)%4]-v[i]));
        }
    }
};
class Parallelogram: public Shape{
public:
    Parallelogram(Point Mass_point,int pos):Shape(Mass_point){
        v.emplace_back(Mass_point);
        switch (pos) {
            case 0:
                v.emplace_back(Mass_point.x+1,Mass_point.y-1);
                v.emplace_back(Mass_point.x+1,Mass_point.y+1);
                v.emplace_back(Mass_point.x,Mass_point.y+2);
                break;
            case 1:
                v.emplace_back(Mass_point.x-1,Mass_point.y-1);
                v.emplace_back(Mass_point.x-1,Mass_point.y+1);
                v.emplace_back(Mass_point.x,Mass_point.y+2);
                break;
            case 2:
                v.emplace_back(Mass_point.x-1,Mass_point.y-1);
                v.emplace_back(Mass_point.x+1,Mass_point.y-1);
                v.emplace_back(Mass_point.x+2,Mass_point.y);
                break;
            case 3:
                v.emplace_back(Mass_point.x+2,Mass_point.y);
                v.emplace_back(Mass_point.x+1,Mass_point.y+1);
                v.emplace_back(Mass_point.x-1,Mass_point.y+1);
                break;
            default:
                break;
        }
        for(int i=0;i<4;i++){
            n.emplace_back(Normal(v[(i+1)%4]-v[i]));
        }
    }
};
static int matrix[13][8][9]=
        {
                {
                        0,  0,  0,  0,  1,  0,  0,  0,  0,
                        0,  0,  0,  1,  2,  1,  0,  0,  0,
                        0,  0,  1,  2,  2,  2,  1,  0,  0,
                        0,  1,  2,  2,  2,  2,  2,  1,  0,
                        1,  1,  1,  1,  1,  1,  1,  1,  1,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                },//case1
                {
                        1,  1,  1,  1,  1,  0,  0,  0,  0,
                        1,  2,  2,  2,  1,  0,  0,  0,  0,
                        1,  2,  2,  2,  1,  0,  0,  0,  0,
                        1,  2,  2,  2,  1,  0,  0,  0,  0,
                        1,  1,  1,  1,  1,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                },//case2
                {
                        0,  0,  0,  0,  1,  0,  0,  0,  0,
                        0,  0,  0,  1,  2,  1,  0,  0,  0,
                        0,  0,  1,  2,  2,  2,  1,  0,  0,
                        0,  1,  2,  2,  2,  1,  0,  0,  0,
                        1,  2,  2,  2,  1,  0,  0,  0,  0,
                        0,  1,  2,  1,  0,  0,  0,  0,  0,
                        0,  0,  1,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                },//case3
                {
                        0,  0,  0,  0,  1,  1,  1,  1,  1,
                        0,  0,  0,  1,  2,  2,  2,  1,  0,
                        0,  0,  1,  2,  2,  2,  1,  0,  0,
                        0,  1,  2,  2,  2,  1,  0,  0,  0,
                        1,  1,  1,  1,  1,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                },//case4
                {
                        0,  0,  1,  1,  1,  1,  1,  0,  0,
                        0,  1,  2,  2,  2,  1,  0,  0,  0,
                        1,  2,  2,  2,  1,  0,  0,  0,  0,
                        1,  2,  2,  1,  0,  0,  0,  0,  0,
                        1,  2,  1,  0,  0,  0,  0,  0,  0,
                        1,  1,  0,  0,  0,  0,  0,  0,  0,
                        1,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                },//case5
                {
                        0,  0,  0,  1,  0,  0,  0,  0,  0,
                        0,  0,  1,  2,  1,  0,  0,  0,  0,
                        0,  1,  2,  2,  2,  1,  0,  0,  0,
                        1,  2,  2,  2,  1,  0,  0,  0,  0,
                        1,  2,  2,  1,  0,  0,  0,  0,  0,
                        1,  2,  1,  0,  0,  0,  0,  0,  0,
                        1,  1,  0,  0,  0,  0,  0,  0,  0,
                        1,  0,  0,  0,  0,  0,  0,  0,  0,
                },//case6
                {
                        1,  1,  1,  0,  0,  0,  0,  0,  0,
                        1,  2,  2,  1,  0,  0,  0,  0,  0,
                        1,  2,  2,  2,  1,  0,  0,  0,  0,
                        1,  2,  2,  2,  2,  1,  0,  0,  0,
                        1,  1,  1,  1,  1,  1,  1,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                },//case7
                {
                        0,  0,  0,  1,  1,  1,  1,  1,  0,
                        0,  0,  1,  2,  2,  2,  2,  1,  0,
                        0,  1,  2,  2,  2,  2,  2,  1,  0,
                        1,  1,  1,  1,  1,  1,  1,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                },//case8
                {
                        1,  1,  1,  1,  1,  0,  0,  0,  0,
                        1,  2,  2,  2,  2,  1,  0,  0,  0,
                        1,  2,  2,  2,  1,  0,  0,  0,  0,
                        1,  2,  2,  1,  0,  0,  0,  0,  0,
                        1,  2,  1,  0,  0,  0,  0,  0,  0,
                        0,  1,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                },//case9
                {
                        0,  0,  1,  1,  1,  0,  0,  0,  0,
                        0,  1,  2,  2,  2,  1,  0,  0,  0,
                        1,  2,  2,  2,  2,  2,  1,  0,  0,
                        0,  1,  2,  2,  2,  1,  0,  0,  0,
                        0,  0,  1,  1,  1,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                },//case10
                {
                        0,  0,  1,  1,  1,  1,  1,  0,  0,
                        0,  1,  2,  2,  2,  2,  2,  1,  0,
                        1,  2,  2,  2,  2,  2,  1,  0,  0,
                        0,  1,  1,  1,  1,  1,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                },//case11
                {
                        0,  1,  1,  1,  0,  0,  0,  0,  0,
                        1,  2,  2,  2,  1,  0,  0,  0,  0,
                        1,  2,  2,  2,  2,  1,  0,  0,  0,
                        1,  2,  2,  2,  1,  0,  0,  0,  0,
                        0,  1,  2,  1,  0,  0,  0,  0,  0,
                        0,  0,  1,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                },//case12
                {
                        0,  0,  0,  1,  1,  1,  0,  0,  0,
                        0,  0,  1,  2,  2,  1,  0,  0,  0,
                        0,  1,  2,  2,  2,  1,  0,  0,  0,
                        1,  2,  2,  2,  1,  0,  0,  0,  0,
                        1,  2,  2,  1,  0,  0,  0,  0,  0,
                        1,  1,  1,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                        0,  0,  0,  0,  0,  0,  0,  0,  0,
                },//case13
        };
void choose_mode(int kase,int way);
void dfs(int kase,int depth);
void bfs(int kase,int start);
void Astar(int kase,int depth,int maxed);
void SA(int kase, int start);
bool not_overlap(const Shape &s1,const Shape &s2);
bool not_overlap(const Shape &s, const vector<Shape>& ans);
bool check(int kase,const Shape &s);

bool sa_evaluate(int kase, int posX, int posY, int depth);
#endif //TANGRAM_TANGRAM_H
