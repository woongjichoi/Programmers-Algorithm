#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    vector<vector<int>> graph(n+1); // 안에 있는 벡터는 가변적으로 
    vector<int> qwer(n+1,0);
    for (auto v:edge){
        graph[v[0]].push_back(v[1]);
        graph[v[1]].push_back(v[0]);
    }
    queue<vector<int>> q; //queue<vector<int,int>> 이딴 거 없음 잠시 헷갈림
    int count=0;
    q.push({1,count});
    vector<int> visited(n+1, 0);
    visited[1]=1; 
    qwer[1]=1;
    while (!q.empty()){
        //여기에 if문에서 visited에 더 이상 0이 없으면 break하고 큐 사이즈 리턴하게 하려고 햇는데 
        //find가 안 먹어서
        //노드 갈 때마다 거리만 뽑아서 다른 벡터에 저장시킨 다음에
        //거기서 최댓값인 갯수 return하게 함 
        int tmp_node=(q.front())[0]; 
        int tmp_count=(q.front())[1]; 
        q.pop(); 
        for (auto t:graph[tmp_node]){
            if (visited[t]==0){
                q.push({t,tmp_count+1}); 
                visited[t]=1;
                qwer[t]=tmp_count+1;
            }
        }
    }
    
    // 가장 먼 노드 거리 찾기
    int maxx=qwer[1];
    for (auto c:qwer){
        if (c>maxx){
            maxx=c;
        }
    }
    
    // 가장 먼 노드 갯수 찾기 
    int answer=0;
    for (auto c:qwer){
        if (c==maxx){
            answer+=1;
        }
    }
    
    return answer;
}