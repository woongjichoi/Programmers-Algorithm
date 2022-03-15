// 풀이 방식은 쉽게 떠올렸는데 벡터 초기화랑 인덱스 처리에서 헤맴

#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> triangle) {
    // 합을 저장할 triangle이랑 똑같은 사이즈의 배열
    // ex. [[0],[0,0],[0,0,0],[0,0,0,0],[0,0,0,0,0]] 만들고 싶었는데
    // 벡터 대신 문제에서 준 최대 삼각형의 높이 기준으로 배열 씀 
    int dp[500][500];  
    int n=triangle.size();
    
    dp[0][0]=triangle[0][0];
    
    // 마지막 원소 가리킬 때 -1 쓰지 말기 
    for (int i=1; i<n; i++){
        for (int j=0; j<=i; j++){
            if (j==0){
                dp[i][j]=dp[i-1][0]+triangle[i][j];
            }
            else if (j==i){
                dp[i][j]=dp[i-1][i-1]+triangle[i][j];
            }
            else{
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+triangle[i][j];
            }
        }
    }
    
    // C++은 max(배열) 없음
    int answer=0;
    for (int i=0; i<n; i++){
        if (dp[n-1][i]>answer){
            answer=dp[n-1][i];
        }
    }
    
    return answer;
}