#include <iostream>
// #include <math.h>
using namespace std;

// class Solution {
// public:
//     int getSum(int a, int b) {
//         // use of bitwise operators (this works faster than arithmetic operators).

//         // 1. convert int to binary string
//         // size of an integer is assumed to be 32 bits
//         char a_str[10]; 
//         char b_str[10];
//         for (int i=0; i<10; i++) {
//             // right shift operator
//             int atemp = a >> 9-i;
//             int btemp = b >> 9-i;
//             if (atemp & 1)
//                 a_str[i]='1';
//             else 
//                 a_str[i]='0';

//             if (btemp & 1)
//                 b_str[i]='1';
//             else 
//                 b_str[i]='0';            
//         }
//         for (int i=0; i<10; i++)
//             cout << a_str[i];

//         // 2. carry out binary summation
//         int carryin=0;
//         char sum_str[10];
//         for (int i=9; i>=0; i--) {
//             if (carryin==0) {
//                 if (a_str[i]=='0' && b_str[i]=='0') {
//                     sum_str[i]='0';
//                     carryin=0;
//                 }
//                 else if (a_str[i]=='0' && b_str[i]=='1' || a_str[i]=='1' && b_str[i]=='0') {
//                     sum_str[i]='1';
//                     carryin=0;
//                 }
//                 else if (a_str[i]=='1' && b_str[i]=='1') {
//                     sum_str[i]='0';
//                     carryin=1;
//                 }
//             }
//             else {
//                 if (a_str[i]=='0' && b_str[i]=='0') {
//                     sum_str[i]='1';
//                     carryin=0;
//                 }
//                 else if (a_str[i]=='0' && b_str[i]=='1' || a_str[i]=='1' && b_str[i]=='0') {
//                     sum_str[i]='0';
//                     carryin=1;
//                 }
//                 else if (a_str[i]=='1' && b_str[i]=='1') {
//                     sum_str[i]='1';
//                     carryin=1;
//                 }
//             }
//         }

//         // 3. convert binary string to int
//         int ans=0;
//         int base=1;

//         // if the result is negative
//         if (sum_str[0]=='1') {
//             for (int i=0; i<10; i++) {
//                 if (sum_str[i]=='0') {
//                     sum_str[i]=='1';
//                 }
//                 else {
//                     sum_str[i]=='0';
//                 }
//             }
//         }

//         for (int i=9; i>=0; i--) {
//             if (sum_str[i]=='1')
//                 ans += base;
//             base *= 2;
//         }
//         return ans;
//     }
// };


class Solution {
public:
    int getSum(int a, int b) {
        while (b != 0) {
            unsigned carry = a&b;   // carry should be unsigned to deal with negative numbers
            a = a^b;    
            b = carry << 1;
        }
        return a;
    }
};

