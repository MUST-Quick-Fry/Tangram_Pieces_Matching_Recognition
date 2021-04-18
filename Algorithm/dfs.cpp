#include<iostream>
#include<vector>
#include "tangram.h"
using namespace std;
vector<Shape> ans;
vector<vector<Shape>> v;
int vis[8][10];



void dfs(int kase,int depth){
    //cout<<depth<<'\n';
//    if(not_overlap(SmallTriangle(Point(3,1),0),Square(Point(3,2)))){
//        cout<<"true";
//    }
//    else{
//        cout<<"false";
//    }
    if(depth==7){
        for(auto &it:ans){
            cout<<it;
        }
        cout<<'\n';
    }
    for(int i=0;i<8;i++)
        for(int j=0;j<9;j++){
            switch (depth) {
                case 0:
                    if (matrix[kase][i][j] == 2) {
                        Square s(Point(i, j));
                        if (check(kase, s)) {
                            vis[i][j] = depth+1;
                            ans.emplace_back(s);
                            dfs(kase, depth + 1);
                            ans.pop_back();
                            vis[i][j] = 0;
                        }
                    }
                    break;
                case 1:
                    if (matrix[kase][i][j] == 2 && !vis[i][j]) {
                        for (int k = 0; k < 4; k++) {
                            BigTriangle bt(Point(i, j), k);
                            if (check(kase, bt) && not_overlap(bt,ans)) {
                                vis[i][j] = depth+1;
                                ans.emplace_back(bt);
                                //cout<<bt<<'\n';
                                dfs(kase, depth + 1);
                                ans.pop_back();
                                vis[i][j] = 0;
                            }

                        }
                    }
                    break;
                case 2:
                    if (matrix[kase][i][j] == 2 && !vis[i][j]) {
                        for (int k = 0; k < 4; k++) {
                            BigTriangle bt(Point(i, j), k);
                            if (check(kase, bt) && not_overlap(bt,ans)) {
                                vis[i][j] = depth+1;
                                ans.emplace_back(bt);
                                //cout<<bt<<'\n';
                                dfs(kase, depth + 1);
                                ans.pop_back();
                                vis[i][j] = 0;
                            }

                        }
                    }
                    break;
                case 3:
                    if(matrix[kase][i][j]){
                        for(int k=0;k<4;k++){
                            Parallelogram p(Point(i,j),k);
                            if(check(kase,p) && not_overlap(p,ans)){
                                vis[i][j]=depth+1;
                                ans.emplace_back(p);
                                dfs(kase,depth+1);
                                ans.pop_back();
                                vis[i][j]=0;
                            }
                        }
                    }
                    break;
                case 4:
                    if(matrix[kase][i][j]){
                        for(int k=0;k<4;k++){
                            MidTriangle mt(Point(i,j),k);
                            if(check(kase,mt) && not_overlap(mt,ans)){
                                vis[i][j]=depth+1;
                                ans.emplace_back(mt);
                                dfs(kase,depth+1);
                                ans.pop_back();
                                vis[i][j]=0;
                            }
                        }
                    }
                    break;
                default:
                    if(matrix[kase][i][j]){
                        for(int k=0;k<4;k++){
                            SmallTriangle st(Point(i,j),k);
                            if(check(kase,st) && not_overlap(st,ans)){
                                vis[i][j]=depth+1;
                                ans.emplace_back(st);
                                dfs(kase,depth+1);
                                ans.pop_back();
                                vis[i][j]=0;
                            }
                        }
                    }
                    break;
            }
        }
}