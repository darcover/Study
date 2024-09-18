#include <iostream>

int main() 
{
    char char1 = 'A', char2 = 'Z';
    std::cout << "Сумма: " << char1 << " + " << char2 << " = " << (char)(char1 + char2) << "\n\n";

    short short1 = 10, short2 = 20;
    std::cout << "Сумма: " << short1 << " + " << short2 << " = " << (short1 + short2) << "\n\n";

    int int1 = 100, int2 = 200;
    std::cout << "Сумма: " << int1 << " + " << int2 << " = " << (int1 + int2) << "\n\n";

    long long1 = -2147483648, long2 = 2147483647;
    std::cout << "Сумма: " << long1 << " + " << long2 << " = " << (long1 + long2) << "\n\n";

    long long longLong1 = 1000000000, longLong2 = 2000000000;
    std::cout << "Сумма: " << longLong1 << " + " << longLong2 << " = " << (longLong1 + longLong2) << "\n\n";

    unsigned char uchar1 = 100, uchar2 = 150;
    std::cout << "Сумма: " << static_cast<int>(uchar1) << " + " << static_cast<int>(uchar2) << " = " << static_cast<int>(uchar1 + uchar2) << "\n\n";

    unsigned short ushort1 = 1000, ushort2 = 2000;
    std::cout << "Сумма: " << ushort1 << " + " << ushort2 << " = " << (ushort1 + ushort2) << "\n\n";

    unsigned int uint1 = 10000, uint2 = 20000;
    std::cout << "Сумма: " << uint1 << " + " << uint2 << " = " << (uint1 + uint2) << "\n\n";

    unsigned long ulong1 = 100000, ulong2 = 200000;
    std::cout << "Сумма: " << ulong1 << " + " << ulong2 << " = " << (ulong1 + ulong2) << "\n\n";

    unsigned long long ullong1 = 9223372036854775807, ullong2 = 9223372036854775807;
    std::cout << "Сумма: " << ullong1 << " + " << ullong2 << " = " << (ullong1 + ullong2) << "\n\n";

    float float1 = 5.5f, float2 = 2.2f;
    std::cout << "Сумма: " << float1 << " + " << float2 << " = " << (float1 + float2) << "\n\n";

    double double1 = 100.25, double2 = 200.75;
    std::cout << "Сумма: " << double1 << " + " << double2 << " = " << (double1 + double2) << "\n\n";

    long double longDouble1 = 1000.25L, longDouble2 = 2000.75L;
    std::cout << "Сумма: " << longDouble1 << " + " << longDouble2 << " = " << (longDouble1 + longDouble2) << "\n\n";

    bool bool1 = true, bool2 = false;
    std::cout << "Сумма: " << bool1 << " && " << bool2 << " = " << (bool)(bool1 * bool2) << "\n";

    return 0;
}
