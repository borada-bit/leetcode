/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    if (head == NULL) {
        return false;
    }
    
    struct ListNode *fast = head;
    struct ListNode *slow = head;
    bool cycle = false;
    
    while(fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        
        if (fast == slow) {
            cycle = true;
            break;
        }
    }
    
    return cycle;
}