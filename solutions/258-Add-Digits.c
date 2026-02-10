int addDigits(int num) {
    bool flag = true;
    int sum = 0;
    while(flag){
        if (num){
            sum += num%10;
            num /=10;
            if(num == 0 && sum > 9){
                num = sum;
                sum = 0;
            }
        }
        
        else if(sum<=9){
            flag = false;
        }
    }
    return sum;
}
