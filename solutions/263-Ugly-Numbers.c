bool isUgly(int n) {
    int arr[3] = {2,3,5};
    if (n<1){
        return false;
    }
    for(int i = 0; i<3;i++){
        while(n%arr[i]==0){
            n/=arr[i];
        }
    }
    return n == 1;