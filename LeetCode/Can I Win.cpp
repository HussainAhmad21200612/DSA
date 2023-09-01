class Solution {
 public:
  bool canIWin(int maxChoosableInteger, int desiredTotal) {
		// sanity check
		if (desiredTotal<=maxChoosableInteger)
				return true;
		if (desiredTotal>(maxChoosableInteger*(maxChoosableInteger+1))/2)
				return false;

		unordered_map<int, bool> memo;
		return helper(desiredTotal, memo, 0, maxChoosableInteger);
}

bool helper (int desiredTotal, unordered_map<int, bool>& memo, int key, int& M) {
		if (desiredTotal<=0)
				return false;

		if (memo.find(key) != memo.end())
				return memo[key];

		for (int i=1; i<=M; i++) {
				if (!(key&1<<i) && !helper(desiredTotal-i, memo, key|1<<i, M)) {
						memo[key] = true;
						return memo[key];
				}
		}

		memo[key] = false;
		return memo[key];
}
};
