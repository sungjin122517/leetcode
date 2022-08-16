struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
//     if (!list1 && !list2) { return nullptr; }
//     if (!list1) { return list2; }
//     if (!list2) { return list1; }

//     ListNode* curr1 = list1;
//     ListNode* curr2 = list2;

//     if (curr2->val >= curr1->val) {
//         while (curr2 != nullptr) {
//             ListNode* temp1 = curr1;
//             ListNode* temp2 = curr2;
//             if (curr2->val >= curr1->val && curr2->val <= curr1->next->val) {   // curr1->next might be nullptr, which causes error.
//                 curr2 = curr2->next;
//                 curr1 = curr1->next;
//                 temp1->next = temp2;
//                 while (curr2->val < curr1->val) {
//                     temp2 = temp2->next;
//                     curr2 = curr2->next;
//                 }
//                 temp2->next = curr1;
//             }
//             else {
//                 curr1 = curr1->next;
//             }
//         }
//         return list1;
//     }
//     while (curr1 != nullptr) {
//         ListNode* temp1 = curr1;
//         ListNode* temp2 = curr2;
//         if (curr1->val >= curr2->val && curr1->val <= curr2->next->val) {
//             curr1 = curr1->next;
//             curr2 = curr2->next;
//             temp2->next = temp1;
//             while (curr1->val < curr2->val) {
//                 temp1 = temp1->next;
//                 curr1 = curr1->next;
//             }
//             temp1->next = curr2;
//         }
//         else {
//             curr2 = curr2->next;
//         }
        
//     }
//     return list2;
// }

ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    if (!list1 && !list2) { return nullptr; }
    if (!list1) { return list2; }
    if (!list2) { return list1; }

    // temporary node to hang the result on
    ListNode dummy;

    // tail points to the last result node
    ListNode* tail = &dummy;
    tail->next = nullptr;

    while (1) {
        ListNode* temp1 = list1;
        ListNode* temp2 = list2;
        if (list1 == nullptr) {
            tail->next = list2;
            break;
        }
        else if (list2 == nullptr) {
            tail->next = list1;
            break;
        }

        if (list1->val <= list2->val) {
            list1 = list1->next;
            tail->next = temp1;
            temp1->next = nullptr;
        }
        else {
            list2 = list2->next;
            tail->next = temp2;
            temp2->next = nullptr;
        }
        tail = tail->next;
    }

    return (dummy.next);
}


// Recursion
ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    ListNode* result = nullptr;

    if (list1 == nullptr)
        return list2;
    else if (list2 == nullptr)
        return list1;

    if (list1->val <= list2->val) {
        result = list1;
        result->next = mergeTwoLists(list1->next, list2);
    }
    else {
        result = list2;
        result->next = mergeTwoLists(list1, list2->next);
    }

    return result;
}
