#include <iostream>
#include <vector>
#include <queue>

class Solution {
public:
    vector<vector<int>> nearest(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        queue<pair<int, int>> q;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j]) {
                    q.push({i, j});
                    grid[i][j] = 0;
                } else {
                    grid[i][j] = INT_MAX;
                }
            }
        }

        vector<int> row = {-1, 1, 0, 0};
        vector<int> col = {0, 0, -1, 1};

        while (!q.empty()) {
            pair<int, int> top = q.front();
            q.pop();
            int x = top.first;
            int y = top.second;
            int time = grid[x][y];

            for (int i = 0; i < 4; ++i) {
                int newx = x + row[i];
                int newy = y + col[i];

                if (newx >= 0 && newx < n && newy >= 0 && newy < m && grid[newx][newy] == INT_MAX) {
                    grid[newx][newy] = time + 1;
                    q.push({newx, newy});
                }
            }
        }

        return grid;
}

};
