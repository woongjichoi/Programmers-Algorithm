#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> numbers, int target) {
    queue<vector<int>> plus_start;
    queue<vector<int>> minus_start;
    int count=0;
    int answer=0;
    
    plus_start.push({numbers[0],count});
    minus_start.push({-1*numbers[0],count}); 
    while (!plus_start.empty()){
        int n=(plus_start.front())[0]; 
        int now_count=(plus_start.front())[1]; 
        if (now_count==numbers.size()-1){
            break;
        }
        plus_start.pop(); 
        plus_start.push({n+numbers[now_count+1],now_count+1}); 
        plus_start.push({n-numbers[now_count+1],now_count+1});
    }
    
    // 큐는 auto로 순회 불가능
    while (!plus_start.empty()){
        int p=(plus_start.front())[0];
        if (p==target){
            answer+=1;
        }
        plus_start.pop();
    }
    
    while (!minus_start.empty()){
        int n=(minus_start.front())[0]; 
        int now_count=(minus_start.front())[1]; 
        if (now_count==numbers.size()-1){
            break;
        }
        minus_start.pop(); 
        minus_start.push({n+numbers[now_count+1],now_count+1}); 
        minus_start.push({n-numbers[now_count+1],now_count+1}); 
    }
    
    while (!minus_start.empty()){
        int p=(minus_start.front())[0];
        if (p==target){
            answer+=1;
        }
        minus_start.pop();
    }
    
    return answer;
}