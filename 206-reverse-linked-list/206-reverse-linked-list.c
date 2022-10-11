/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    if (head == NULL) {
        return NULL;
    }
    
    struct ListNode *curr = head->next;
    head->next = NULL;
    struct ListNode *prev = head;
    struct ListNode *temp = head;
    
    while(curr != NULL) {
        temp = prev;
        prev = curr; 
        
        curr = curr->next;
        prev->next = temp;
    }
    
    return prev;
}