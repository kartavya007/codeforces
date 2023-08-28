#include<iostream>
#include<math.h>
using namespace std ;

int main()
{
    int temp , row = 0 , col = 0;
    for(int i = 0 ; i < 5 ; i++)
    {
        for(int j = 0 ; j < 5 ; j++)
        {
            cin>>temp ;
            if(temp)
            {
                row = i ;
                col = j ; 
            }
        }
    }
    int moves = abs(2 - row) + abs(2 - col) ;
    cout<<moves ;
    return 0 ; 
}
/*
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

*/