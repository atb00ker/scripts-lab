#include <iostream>
using namespace std;

// HCF/GCD for 2 Numbers
int gcd2(int a, int b) {
    if (a == 0)
        return b;
    return gcd2(b%a,a);
}

// LCM for 2 Numbers
int lcm2(int a, int b) {
    return (a*b)/gcd2(a,b);
}

// HCF/GCD for 3 Numbers
int gcd3(int a, int b, int c) {
    int r = gcd2(a,b);
    return gcd2(r,c);
}

// LCM for 3 Numbers
int lcm3(int a, int b, int c) {
    // a×b×c*HCF(a,b,c)/HCF(a,b)×HCF(b,c)×HCF(c,a)=LCM(a,b,c)
    return (a*b*c*gcd3(a,b,c))/(gcd2(a,b)*gcd2(b,c)*gcd2(c,a));
}


int main() {
    int a, b, c, n;
    cout<<"Enter how many numbers you have? (2 or 3): ";
    cin>>n;
    switch(n) {
        case 2:
            cout<<"Enter first number: ";
            cin>>a;
            cout<<"Enter second number: ";
            cin>>b;
            cout<<"GCD: "<<gcd2(a,b)<<endl;
            cout<<"LCM: "<<lcm2(a,b)<<endl;
            break;
        case 3:
            cout<<"Enter first number: ";
            cin>>a;
            cout<<"Enter second number: ";
            cin>>b;
            cout<<"Enter third number: ";
            cin>>c;
            cout<<"GCD: "<<gcd3(a,b,c)<<endl;
            cout<<"LCM: "<<lcm3(a,b,c)<<endl;
            break;
        default:
            cout<<"Incorrect Value!"<<endl;
    }
	return 0;

}
