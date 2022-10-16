/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    if(list1 == NULL) {
        return list2;
    } else if(list2 == NULL) {
        return list1;
    } else if (list1 == NULL && list2 == NULL) {
        return NULL;
    }
    
    struct ListNode* new_list = NULL;
    if(list1->val <= list2->val) {
        new_list = list1;
        list1 = list1->next;
    } else {
        new_list = list2;
        list2 = list2->next;
    }
    
    new_list->next = NULL;
    struct ListNode* new_head = new_list;
    
    while (true) {
        
        if(list1 == NULL) {
            //append to new head list 2;
            new_list->next = list2;
            break;
        } else if (list2 == NULL) {
            //append to new head list 1;
            new_list->next = list1;
            break;
        }        
        
        if(list1->val <= list2->val) {
            new_list->next = list1;
            list1 = list1->next;
        } else {
            new_list->next = list2;
            list2 = list2->next;
        }
        
        new_list = new_list->next;
    }
    
    return new_head;
}
