#include <string>
#include <vector>

using namespace std;

string solution(int n) {
    string answer="";
    int a, b;
    
    while (n>0){
        a=n/3;
        b=n%3;
        if (b==2){
            answer="2"+answer;
            n=a;
        }
        else if (b==1){
            answer="1"+answer;
            n=a;
        }
        else{
            answer="4"+answer;
            n=a-1;
        }
    }
    
    return answer;
}