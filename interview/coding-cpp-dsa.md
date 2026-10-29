# C++ and data-structure problems

These problems test C++ fluency and the structures trading systems use. Solve each in C++, state the complexity, and say what the worst case is. Compile your solution with `-Wall -Wextra -Werror` before you trust it.

Difficulty: 🟢 warm-up · 🟡 standard · 🔴 hard

---

### 1. Reverse a singly linked list 🟢

Reverse a singly linked list in place. State the time and space complexity.

<details><summary>Solution</summary>

```cpp
struct Node {
    int value;
    Node* next;
};

Node* reverse(Node* head) {
    Node* prev = nullptr;
    while (head != nullptr) {
        Node* next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }
    return prev;
}
```

Time O(n), space O(1). Test the empty list, a single node, and a list of two.
</details>

---

### 2. Top k of a stream 🟡

Given a stream of n integers, return the k largest. Give the complexity, and say what changes if the stream does not fit in memory.

<details><summary>Solution</summary>

Keep a min-heap of size k. For each value, push it if the heap is smaller than k, or replace the top if the value is larger.

```cpp
#include <cstddef>
#include <functional>
#include <queue>
#include <vector>

std::vector<int> topK(const std::vector<int>& values, std::size_t k) {
    std::priority_queue<int, std::vector<int>, std::greater<int>> heap;
    for (int v : values) {
        if (heap.size() < k) {
            heap.push(v);
        } else if (v > heap.top()) {
            heap.pop();
            heap.push(v);
        }
    }
    std::vector<int> result;
    while (!heap.empty()) {
        result.push_back(heap.top());
        heap.pop();
    }
    return result;
}
```

Time O(n log k), space O(k). A max-heap of everything would be O(n) space, which fails for a stream.
</details>

---

### 3. Merge two sorted sequences 🟢

Merge two sorted vectors into one sorted vector in O(n + m) time.

<details><summary>Solution</summary>

```cpp
#include <vector>

std::vector<int> merge(const std::vector<int>& a, const std::vector<int>& b) {
    std::vector<int> out;
    out.reserve(a.size() + b.size());
    std::size_t i = 0, j = 0;
    while (i < a.size() && j < b.size()) {
        out.push_back(a[i] <= b[j] ? a[i++] : b[j++]);
    }
    out.insert(out.end(), a.begin() + i, a.end());
    out.insert(out.end(), b.begin() + j, b.end());
    return out;
}
```

Time O(n + m). The `reserve` call avoids reallocations, which matters when this runs on a hot path.
</details>

---

### 4. Detect a cycle in a linked list 🟡

Given a linked list, decide whether it contains a cycle, using O(1) extra space.

<details><summary>Solution</summary>

Floyd's tortoise and hare: move one pointer by one step and another by two. If they meet, there is a cycle.

```cpp
bool hasCycle(const Node* head) {
    const Node* slow = head;
    const Node* fast = head;
    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            return true;
        }
    }
    return false;
}
```

Time O(n), space O(1). The pointers meet within n steps once inside the cycle, because the fast pointer closes the gap by one each step.
</details>

---

### 5. LRU cache 🟡

Design a cache with get and put in O(1) average time that evicts the least recently used entry when full.

<details><summary>Solution</summary>

Combine a doubly linked list (most recent at the front) with a hash map from key to list iterator.

```cpp
#include <list>
#include <unordered_map>
#include <utility>

class LRUCache {
public:
    explicit LRUCache(std::size_t capacity) : capacity_(capacity) {}

    bool get(int key, int& value) {
        auto it = index_.find(key);
        if (it == index_.end()) {
            return false;
        }
        order_.splice(order_.begin(), order_, it->second);
        value = it->second->second;
        return true;
    }

    void put(int key, int value) {
        auto it = index_.find(key);
        if (it != index_.end()) {
            it->second->second = value;
            order_.splice(order_.begin(), order_, it->second);
            return;
        }
        if (order_.size() == capacity_) {
            index_.erase(order_.back().first);
            order_.pop_back();
        }
        order_.emplace_front(key, value);
        index_[key] = order_.begin();
    }

private:
    std::size_t capacity_;
    std::list<std::pair<int, int>> order_;
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> index_;
};
```

`splice` moves a node without invalidating iterators, so the map's stored iterators stay valid. Average O(1) per operation.
</details>

---

### 6. Order book price levels 🔴

Describe how you would store the bid side of a limit order book so that adding an order, cancelling an order, and reading the best bid are all fast. State the complexity of each, and say which you would choose for a liquid stock with a narrow price range.

<details><summary>Solution</summary>

- **Price levels:** a sorted map from price to a queue of orders. Adding a new level is O(log L) for L levels; reading the best bid is O(1) with a cached pointer.
- **Orders:** a hash map from order ID to its node in the queue, so a cancel finds the node in O(1) and removes it from its queue in O(1) with a doubly linked list.
- **Narrow range:** a flat array indexed by tick, with a cached best-bid index, gives O(1) for add and cancel and a cheap scan for the best bid. It is also cache-friendly.

For a liquid stock with a narrow range, the flat array usually wins in practice. The answer that shows judgement names the trade-off: the array needs a known price range, and a stock that gaps outside it needs a fallback.

See [Project 10](../projects/10-limit-order-book-simulator/) for the implementation.
</details>

---

### 7. Thread-safe counter versus atomic 🟡

Explain why `std::atomic<int>::fetch_add` is not the same as `int++` with a mutex around it, and which you would choose for a counter of processed messages.

<details><summary>Solution</summary>

Both are safe for concurrent increments. The atomic is a single hardware operation, usually much cheaper than a mutex, which may involve a system call when there is contention. A mutex also blocks other threads while it is held.

For a counter, use `std::atomic<std::uint64_t>` with `fetch_add(1, std::memory_order_relaxed)`. Relaxed ordering is enough because nothing else depends on the order of the increments. If the count is published with other data, use `release` on the publish and `acquire` on the read.
</details>
