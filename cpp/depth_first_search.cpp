#include <iostream>
#include <stack>
#include <unordered_map>
#include <vector>

using namespace std;

void depthFirstPrint(unordered_map<char, vector<char>>& graph, char source) {
    stack<char> s;
    s.push(source);

    while (!s.empty()) {
        char current = s.top();
        s.pop();
        cout << current << " ";

        // Push neighbors onto the stack
        for (char neighbor : graph[current]) {
            s.push(neighbor);
        }
    }
}

int main() {
    unordered_map<char, vector<char>> graph;
    graph['a'] = {'b', 'c'};
    graph['b'] = {'d'};
    graph['c'] = {'e'};
    graph['d'] = {'f'};
    graph['e'] = {};
    graph['f'] = {};

    depthFirstPrint(graph, 'a');  // Output: a b d f c e

    return 0;
}
