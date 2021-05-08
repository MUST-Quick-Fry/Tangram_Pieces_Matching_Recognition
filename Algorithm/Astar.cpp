#include "tangram.h"
#include<iostream>
#include<vector>
using namespace std;
vector<Shape> ans1;
//vector<vector<Shape>> v;
int vis1[8][10];
int dx[8]={0,0,1,1,1,-1,-1,-1};
int dy[8]={1,-1,0,-1,1,0,-1,1};
int h_x(int kase){
    for(int i=0;i<8;i++){
        for(int j=0;j<9;j++){
            if(matrix[kase][i][j] && !vis1[i][j]){
                int cnt=0,flag=0,cnt1=0;
                for(int k=0;k<8;k++){
                    if(i+dx[k]>=0 && j+dy[k]>=0 && i+dx[k]<8 && j+dy[k]<9 ){
                        if(vis1[i+dx[k]][j+dy[k]]){
                            cnt++;
                            if(vis1[i+dx[k]][j+dy[k]]>7){
                                flag++;
                            }
                        }
                        else{
                            break;
                        }
                    }
                    else{
                        cnt1++;
                    }
                }
                if(cnt1+cnt==8 && cnt/3>=flag)
                    return 0x7f7f7f7f;
            }
        }
    }
    return 0;// if not return 0;
}
void Astar(int kase,int depth,int area){
    if(depth==7){
        for(auto &it:ans1){
            cout<<it<<' ';
        }
        //v.emplace_back(ans1);
        cout<<"\n";
        return;
    }
    if(area+h_x(kase)>16){
        return;
    }
    for(int i=0;i<8;i++)
        for(int j=0;j<9;j++){
            switch (depth) {
                case 0:
                    //initial_area(kase);
                    if (matrix[kase][i][j] == 2) {
                        Square s(Point(i, j));
                        if (check(kase, s)) {
                            vis1[i][j] = 7+depth+1;
                            for(auto &it:s.v){
                                vis1[(int)it.x][(int)it.y]=depth+1;
                            }
                            ans1.emplace_back(s);
                            Astar(kase, depth + 1,area+2);
                            ans1.pop_back();
                            for(auto &it:s.v){
                                vis1[(int)it.x][(int)it.y]=0;
                            }
                            vis1[i][j] = 0;
                        }
                    }
                    break;
                case 1:
                    if (matrix[kase][i][j] == 2 && !vis1[i][j]) {
                        for (int k = 0; k < 4; k++) {
                            BigTriangle bt(Point(i, j), k);
                            if (check(kase, bt) && not_overlap(bt,ans1)) {
                                vis1[i][j] = 7+depth+1;
                                ans1.emplace_back(bt);
                                for(auto &it:bt.v){
                                    vis1[(int)it.x][(int)it.y]=depth+1;
                                }
                                Astar(kase, depth + 1,area+4);
                                ans1.pop_back();
                                for(auto &it:bt.v){
                                    vis1[(int)it.x][(int)it.y]=0;
                                }
                                vis1[i][j] = 0;
                            }

                        }
                    }
                    break;
                case 2:
                    if (matrix[kase][i][j] == 2 && !vis1[i][j]) {
                        for (int k = 0; k < 4; k++) {
                            BigTriangle bt(Point(i, j), k);
                            if (check(kase, bt) && not_overlap(bt,ans1)) {
                                vis1[i][j] = 7+depth+1;
                                for(auto &it:bt.v){
                                    vis1[(int)it.x][(int)it.y]=depth+1;
                                }
                                ans1.emplace_back(bt);
                                //cout<<bt<<'\n';
                                Astar(kase, depth + 1,area+4);
                                ans1.pop_back();
                                for(auto &it:bt.v){
                                    vis1[(int)it.x][(int)it.y]=0;
                                }
                                vis1[i][j] = 0;
                            }

                        }
                    }
                    break;
                case 3:
                    if(matrix[kase][i][j]){
                        for(int k=0;k<4;k++){
                            Parallelogram p(Point(i,j),k);
                            if(check(kase,p) && not_overlap(p,ans1)){
                                vis1[i][j]=7+depth+1;
                                for(auto &it:p.v){
                                    vis1[(int)it.x][(int)it.y]=depth+1;
                                }
                                ans1.emplace_back(p);
                                Astar(kase,depth+1,area+2);
                                ans1.pop_back();
                                for(auto &it:p.v){
                                    vis1[(int)it.x][(int)it.y]=0;
                                }
                                vis1[i][j]=0;
                            }
                        }
                    }
                    break;
                case 4:
                    if(matrix[kase][i][j]){
                        for(int k=0;k<4;k++){
                            MidTriangle mt(Point(i,j),k);
                            if(check(kase,mt) && not_overlap(mt,ans1)){
                                vis1[i][j]=7+depth+1;
                                for(auto &it:mt.v){
                                    vis1[(int)it.x][(int)it.y]=depth+1;
                                }
                                ans1.emplace_back(mt);
                                Astar(kase,depth+1,area+2);
                                ans1.pop_back();
                                for(auto &it:mt.v){
                                    vis1[(int)it.x][(int)it.y]=0;
                                }
                                vis1[i][j]=0;
                            }
                        }
                    }
                    break;
                default:
                    if(matrix[kase][i][j]){
                        for(int k=0;k<4;k++){
                            SmallTriangle st(Point(i,j),k);
                            if(check(kase,st) && not_overlap(st,ans1)){
                                vis1[i][j]=7+depth+1;
                                for(auto &it:st.v){
                                    vis1[(int)it.x][(int)it.y]=depth+1;
                                }
                                ans1.emplace_back(st);
                                Astar(kase,depth+1,area+1);
                                ans1.pop_back();
                                for(auto &it:st.v){
                                    vis1[(int)it.x][(int)it.y]=0;
                                }
                                vis1[i][j]=0;
                            }
                        }
                    }
                    break;
            }
        }
}
