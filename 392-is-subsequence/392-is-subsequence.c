

bool isSubsequence(char * s, char * t){
    int t_index = 0;
    for(int i = 0; s[i] != '\0'; ++i) {
        //printf("searching for %c %d\n", s[i], t[t_index]);
        
        if (t[t_index] == '\0') {
            return false;
        }
        
        while(t[t_index] != '\0') {
            if(t[t_index++] == s[i]){
                //printf("found! %c\n", s[i]);
                break;
            } else if (t[t_index] == '\0') {
                return false;
            }
        }   
    }
    return true;
}