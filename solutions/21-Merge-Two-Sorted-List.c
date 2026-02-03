#include<stdio.h>
 
struct ListNode {
    int val;
    struct ListNode *next;
};
 
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode *head = malloc(sizeof(struct ListNode)), *arrow = head;
    head->next = NULL;
    while (list1 && list2){
        if (list1->val < list2->val){
            arrow->next = list1;
            list1 = list1->next;
            
        }
        else{
            arrow->next = list2;
            list2 = list2->next;
        }
        arrow = arrow->next;        
    }
    arrow->next = list1?list1:list2;
    
    return head->next;
}