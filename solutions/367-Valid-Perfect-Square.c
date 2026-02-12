bool isPerfectSquare(int num) {
    if(num == 1){
        return true;
    }
    int low = 2,high = num;
    long int mid;
    while(low<=high){
        mid = low+(high-low)/2;
        if (mid*mid == num){
            return true;
        }
        else if (mid * mid > num){
            high = mid-1;
        }
        else if (mid * mid < num){
            low = mid+1;
        }  
    }
    return false;   
}