using namespace std;

// 유클리드 호제법
int gcd(int a, int b){
    int mod = a%b;
    
    while (mod>0){
        a = b;
        b = mod;
        mod = a%b;
    }
    
    return b;
}

long long solution(int w,int h) {
    long long answer = (long long)w*(long long)h;
    answer -= gcd(w, h)*((w/gcd(w,h))+(h/gcd(w,h))-1);
    return answer;
}