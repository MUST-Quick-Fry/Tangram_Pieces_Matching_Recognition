#include"tangram.h"
#include<cmath>
#include<vector>
double Dot(Point A,Point B){
    return A.x*B.x+A.y*B.y;
}
double Length(Point A){
    return sqrt(Dot(A,A));
}
Point Normal(Point A){
    double L= Length(A);
    return {-A.y/L,A.x/L};
}
Point Project(const Shape &s,const Point &n){
    double min1= Dot(s.v[0],n);
    double max1=min1;
    for(int i=1;i<s.v.size();i++){
        double p= Dot(n,s.v[i]);
        if(p<min1)
            min1=p;
        else if(p>max1){
            max1=p;
        }
    }
    return {min1,max1};
}
bool not_overlap(const Shape &s1,const Shape &s2){
    for(auto it:s1.n){
        Point proj1=Project(s1,it);
        Point proj2=Project(s2,it);
        if(fabs(proj1.y-proj2.x)<=eps || fabs(proj1.x-proj2.y)<=eps)
            return true;
    }
    for(auto it:s2.n){
        Point proj1=Project(s1,it);
        Point proj2=Project(s2,it);
        if(proj1.y<=proj2.x || proj1.x>=proj2.y)
            return true;
    }
    return false;
}
bool not_overlap(const Shape &s, const vector<Shape>& ans){
    for(auto &it:ans){
        if(!not_overlap(it,s)){
            return false;
        }
    }
    return true;
}

bool check(int kase,const Shape &s){
    for(auto it:s.v){
        if(it.x<0 || it.y<0 || !matrix[kase][(int)it.x][(int)it.y]) {
            return false;
        }
    }
    return true;
}