#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    vector<vector<bool>> graph(n+1, vector<bool>(n+1,false));
    int answer=0;
    
    for (auto result:results){
        graph[result[0]][result[1]]=true;
    }
    
    for (int i=1; i<n+1; i++){
        for (int j=1; j<n+1; j++){
            for (int k=1; k<n+1; k++){
                if (graph[j][i] && graph[i][k]){
                    graph[j][k]=true;
                }
                //if (graph[i][j] && graph[j][k]){
                    //graph[i][k]=true;
                //}
            }
        }
    }
    
    for (int i=1; i<n+1; i++){
        int count=0;
        for (int j=1; j<n+1; j++){
            if (graph[i][j]||graph[j][i]){
                count+=1;
            }
        }
        if (count==n-1){
            answer+=1;
        }
    }
    
    return answer;
}