#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// iterative method
ListNode* reverseList(ListNode* head) {
    if (head == nullptr)
        return nullptr;
    if (head->next == nullptr)
        return head;
    
    ListNode* tempPrev = head;
    ListNode* temp = head->next;
    ListNode* tempNext = head->next->next;

    head->next = nullptr;
    while (temp->next != nullptr) {
        temp->next = tempPrev;
        tempPrev = temp;
        temp = tempNext;
        tempNext = tempNext->next;
    }
    head = temp;
    head->next = tempPrev;

    return head;

}


// recursion
ListNode* reverseList(ListNode* head) {
    if (head==nullptr || head->next==nullptr)
        return head;
    
    ListNode* rest = reverseList(head->next);   // rest는 head로 계속 고정
    ListNode* q = head->next;
    q->next = head;
    head->next = nullptr;

    return rest;
}