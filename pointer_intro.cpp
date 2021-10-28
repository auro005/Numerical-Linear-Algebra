#include<iostream>
using namespace std;

int main()
{
    int n;
    int* ptr = &n;
    *ptr = 7;
    cout<<n<<endl;
}
