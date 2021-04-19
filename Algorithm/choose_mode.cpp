#include"tangram.h"
void choose_mode(int kase,int way){//first parameter 1-13, second parameter 1-4
    /*for(int i=0;i<8;i++) {
        for (int j = 0; j < 9; j++) {
            cout << matrix[kase][i][j] << ' ';
        }
        cout<<'\n';
    }*/
    switch (way) {
        case 1:
            dfs(kase,0);
            break;
        case 2:
            bfs(kase,0);
            break;
        case 3:
            ida(kase,0,0);
            break;
        default:
            break;
    }
}