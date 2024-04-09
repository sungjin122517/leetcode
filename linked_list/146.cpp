#include <iostream>
#include <unordered_map>

using namespace std;

/*
use doubly linked list for adding new key-value
why? To keep the order of put time.
When accessing/adding a key-value pair, it moves the corresponding node to the front of the linked list, making it the most recently used item.
*/



class LRUCache {
public:
    class Node {
        public:
            int key;
            int value;
            Node* next;
            Node* prev;

            Node(int key, int value) {
                this->key = key;
                this->value = value;
            }
    };

    int capacity;
    unordered_map<int, Node*> map;
    Node* head = new Node(-1, -1);
    Node* tail = new Node(-1, -1);

    LRUCache(int capacity) {
        this->capacity = capacity;
        head->next = tail;
        tail->prev = head;
    }

    void addNode(Node* newNode) {
        Node* temp = head->next;
        newNode->next = temp;
        newNode->prev = head;
        head->next = newNode;
        temp->prev = newNode;
    }

    void deleteNode(Node* node) {
        Node* back = node->prev;
        Node* front = node->next;

        back->next = front;
        front->prev = back; 
    }
    
    int get(int key) {
        if (map.find(key) != map.end()) {
            Node* resNode = map[key];
            int ans = resNode->value;
            map.erase(key); // 위치와 주소가 바뀌어서?
            deleteNode(resNode);
            addNode(resNode);
            map[key] = head->next;

            return ans;      
        }
        return -1;

    }
    
    void put(int key, int value) {
        // key already exists
        if (map.find(key) != map.end()) {
            Node* curr = map[key];
            map.erase(key);
            deleteNode(curr);
        }

        // if max capacity
        if (map.size() == capacity) {
            // Node* delNode = tail->prev;
            map.erase(tail->prev->key);
            deleteNode(tail->prev);
        }

        // Node* newNode = ;
        addNode(new Node(key, value));
        map[key] = head->next;
    }
};