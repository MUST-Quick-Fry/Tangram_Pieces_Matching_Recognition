#include"tangram.h"
#include<iostream>
#include <queue>
#include<vector>
#include <cmath>
#include <stdlib.h>
#include <time.h> 
using namespace std;

vector<vector<Shape>> sa_res;

bool sa_evaluate(int kase, int posX, int posY, int depth){
    int cur = matrix[kase][posX][posY];
    if (cur == 0) { return false; }
    else {
        srand(time(0));
        
        double threshold = rand() % 99 / (double)99;         
        //cout << threshold << endl;

        if (exp((cur - 2.05) / (7 - depth)) > threshold) { return true; }
        else { return false; }
    }
}

void SA(int kase, const Shape& start) {
    queue<vector<Shape>> q;
    vector<Shape> v;
    
    v.emplace_back(start);
    q.emplace(v);
    while (!q.empty()) {
        auto top = q.front();
        q.pop();
        //cout << top.size();
        if (top.size() == 7) {
            for (auto& it : top) {
                cout << it << ' ';
            }
            cout << '\n';
            sa_res.emplace_back(top);
            continue;
        }
        for (int i = 0; i < 8; i++)
            for (int j = 0; j < 9; j++) {
                switch (top.size()) {
                case 1:
                    if (sa_evaluate(kase, i, j, (int)top.size())) {
                        for (int k = 0; k < 4; k++) {
                            BigTriangle bt(Point(i, j), k);
                            if (check(kase, bt) && not_overlap(bt, top)) {
                                top.emplace_back(bt);
                                q.emplace(top);
                                top.pop_back();
                            }

                        }
                    }
                    break;
                case 2:
                    if (sa_evaluate(kase, i, j, (int)top.size())) {
                        for (int k = 0; k < 4; k++) {
                            BigTriangle bt(Point(i, j), k);
                            if (check(kase, bt) && not_overlap(bt, top)) {
                                top.emplace_back(bt);
                                q.emplace(top);
                                top.pop_back();
                            }

                        }
                    }
                    break;
                case 3:
                    if (sa_evaluate(kase, i, j, (int)top.size())) {
                        for (int k = 0; k < 4; k++) {
                            Parallelogram p(Point(i, j), k);
                            if (check(kase, p) && not_overlap(p, top)) {
                                top.emplace_back(p);
                                q.emplace(top);
                                top.pop_back();
                            }
                        }
                    }
                    break;
                case 4:
                    if (sa_evaluate(kase, i, j, (int)top.size())) {
                        for (int k = 0; k < 4; k++) {
                            MidTriangle mt(Point(i, j), k);
                            if (check(kase, mt) && not_overlap(mt, top)) {
                                top.emplace_back(mt);
                                q.emplace(top);
                                top.pop_back();
                            }
                        }
                    }
                    break;
                default:
                    if (sa_evaluate(kase, i, j, (int)top.size())) {
                        for (int k = 0; k < 4; k++) {
                            SmallTriangle st(Point(i, j), k);
                            if (check(kase, st) && not_overlap(st, top)) {
                                top.emplace_back(st);
                                q.emplace(top);
                                top.pop_back();
                            }
                        }
                    }
                    break;
                }
            }
    }
}
void SA(int kase, int start) {
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 9; j++) {
            if (matrix[kase][i][j] == 2) {
                SA(kase, Square(Point(i, j)));
            }
        }
    }
}