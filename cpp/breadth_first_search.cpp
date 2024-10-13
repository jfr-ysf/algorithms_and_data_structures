#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

void breadthFirstPrint(unordered_map<string, vector<string>>& graph, string source) {
    queue<string> q;
    q.push(source);

    while (!q.empty()) {
        string current = q.front();
        q.pop();
        cout << current << " ";

        for (const string& neighbor : graph[current]) {
            q.push(neighbor);
        }
    }
}

int main() {
    unordered_map<string, vector<string>> graph = {
        {"a", {"c", "b"}},
        {"b", {"d"}},
        {"c", {"e"}},
        {"d", {"f"}},
        {"e", {}},
        {"f", {}}
    };

    breadthFirstPrint(graph, "a");  // Output: a c b e d f
    return 0;
}
