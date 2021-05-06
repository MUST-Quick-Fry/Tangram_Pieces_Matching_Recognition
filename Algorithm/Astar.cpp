#include "tangram.h"
#include<iostream>
#include<vector>
using namespace std;
vector<Shape> ans1;
//vector<vector<Shape>> v;
int vis[8][10];
int h_x(){
    return 0;
}
void Astar(int kase,int depth,int maxed){
    if(depth+h_x()>7){
        return;
    }
    if(depth==7){
        for(auto &it:ans1){
            cout<<it;
        }
        //v.emplace_back(ans1);
        cout<<"\n";
    }
    for(int i=0;i<8;i++)
        for(int j=0;j<9;j++){
            switch (depth) {
                case 0:
                    initial_area(kase);
                    if (matrix[kase][i][j] == 2) {
                        Square s(Point(i, j));
                        if (check(kase, s)) {
                            vis[i][j] = depth+1;
                            ans1.emplace_back(s);
                            dfs(kase, depth + 1);
                            ans1.pop_back();
                            vis[i][j] = 0;
                        }
                    }
                    break;
                case 1:
                    if (matrix[kase][i][j] == 2 && !vis[i][j]) {
                        for (int k = 0; k < 4; k++) {
                            BigTriangle bt(Point(i, j), k);
                            if (check(kase, bt) && not_overlap(bt,ans1)) {
                                vis[i][j] = depth+1;
                                ans1.emplace_back(bt);
                                //cout<<bt<<'\n';
                                dfs(kase, depth + 1);
                                ans1.pop_back();
                                vis[i][j] = 0;
                            }

                        }
                    }
                    break;
                case 2:
                    if (matrix[kase][i][j] == 2 && !vis[i][j]) {
                        for (int k = 0; k < 4; k++) {
                            BigTriangle bt(Point(i, j), k);
                            if (check(kase, bt) && not_overlap(bt,ans1)) {
                                vis[i][j] = depth+1;
                                ans1.emplace_back(bt);
                                //cout<<bt<<'\n';
                                dfs(kase, depth + 1);
                                ans1.pop_back();
                                vis[i][j] = 0;
                            }

                        }
                    }
                    break;
                case 3:
                    if(matrix[kase][i][j]){
                        for(int k=0;k<4;k++){
                            Parallelogram p(Point(i,j),k);
                            if(check(kase,p) && not_overlap(p,ans1)){
                                vis[i][j]=depth+1;
                                ans1.emplace_back(p);
                                dfs(kase,depth+1);
                                ans1.pop_back();
                                vis[i][j]=0;
                            }
                        }
                    }
                    break;
                case 4:
                    if(matrix[kase][i][j]){
                        for(int k=0;k<4;k++){
                            MidTriangle mt(Point(i,j),k);
                            if(check(kase,mt) && not_overlap(mt,ans1)){
                                vis[i][j]=depth+1;
                                ans1.emplace_back(mt);
                                dfs(kase,depth+1);
                                ans1.pop_back();
                                vis[i][j]=0;
                            }
                        }
                    }
                    break;
                default:
                    if(matrix[kase][i][j]){
                        for(int k=0;k<4;k++){
                            SmallTriangle st(Point(i,j),k);
                            if(check(kase,st) && not_overlap(st,ans1)){
                                vis[i][j]=depth+1;
                                ans1.emplace_back(st);
                                dfs(kase,depth+1);
                                ans1.pop_back();
                                vis[i][j]=0;
                            }
                        }
                    }
                    break;
            }
        }
}
