#include <iostream>
#include <unordered_set>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// 1. hashing approach
bool hasCycle(ListNode *head) {
    // if (head == nullptr || head->next == nullptr)
    //     return false;
    unordered_set<ListNode*> set;

    while (head != nullptr) {
        // return true if head is found in the set (indicates there is a loop)
        if (set.find(head) != set.end())
            return true;
        
        set.insert(head);
        head = head->next;
    }
    return false;
}