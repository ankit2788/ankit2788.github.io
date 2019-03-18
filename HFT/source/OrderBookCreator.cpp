#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

int main()
{

    string TBTpath = "/Users/ankitgupta/Data/TBTData/SBIN_20180404_RawTicks.csv";
    string line;
    ifstream TBT(TBTpath);

    if (!TBT)
    {
        cout<<"TBT file not present in desired location"        <<endl;
        exit(1);
    }

    int totalTicks = 0 ;
    while (getline(TBT, line))
    {
        totalTicks += 1;
        cout<<totalTicks<<endl;
    }
    
    cout<<"Total Ticks ="<<totalTicks << endl;

    return 0;
}


