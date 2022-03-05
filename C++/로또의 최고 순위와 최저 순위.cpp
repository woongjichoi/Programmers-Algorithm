#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int high_number, low_number=0;
    int high_score, low_score;
    
    for (auto lotto:lottos){
        if (*find(win_nums.begin(), win_nums.end(), lotto)==lotto){
            low_number+=1;
        }
    }
    
    if (low_number<2){
        low_score=6;
    }
    else{
        low_score=7-low_number;
    }
    
    high_number=count(lottos.begin(), lottos.end(), 0)+low_number;
    
    if (high_number<2){
        high_score=6;
    }
    else{
        high_score=7-high_number;
    }
    
    answer.push_back(high_score);
    answer.push_back(low_score);
    
    return answer;
}