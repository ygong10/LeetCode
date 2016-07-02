/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next){
            return head;
        }
        if (!head->next->next){
            ListNode *new_head = head->next;
            new_head->next = head;
            head->next = NULL;
            return new_head;
        }
        ListNode *first, *second, *temp;
        first = head;
        second = first->next;
        first->next = NULL;
        first = second;
        second = second->next;
        first->next = head;
        while (second){
            temp = second->next;
            second->next = first;
            first = second;
            second = temp;
        }
        return first;
    }
};