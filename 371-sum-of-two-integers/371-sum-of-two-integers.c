int getSum(int a, int b){
    // reikia XOR a su b, bet tada negauname kai vienodi tada tikrinti reikia su b & a kiek reikia bitu paslinkti i kaire 
    
    while(b != 0) {
        int temp = (a & b);
        a ^= b;
        b = (unsigned)temp << 1;
    }
    return a;
}
