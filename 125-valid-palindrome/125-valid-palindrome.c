

bool isPalindrome(char * s){
    int forward_index = 0;
    int backward_index = 0;
    
    while(s[backward_index] != '\0') {
        ++backward_index;
    }
    
    int string_size = backward_index;
    backward_index--;
    
    while(backward_index >= 0 && forward_index < string_size) {
        if(isalnum(s[forward_index]) == false) {
            ++forward_index;
            continue;
        } 
        if(isalnum(s[backward_index]) == false) {
            --backward_index;
            continue;
        }
        if(tolower(s[forward_index]) != tolower(s[backward_index])) {
            return false;
        }
        ++forward_index;
        --backward_index;
    }
    
    return true;
}