### 题目：8. 字符串转换整数 (atoi)

#### 难度：中等

#### 题目描述：
实现一个 `myAtoi(string s)` 函数，将字符串转换为 32 位有符号整数。转换规则如下：
1. **空格**：丢弃前导空格。
2. **符号**：检查下一个字符是否为 `'-'` 或 `'+'`，若无则假定为正。
3. **转换**：读取数字字符，直到遇到非数字字符或字符串结束。若无数字则返回 `0`。
4. **舍入**：若整数超出 `[−2³¹, 2³¹ − 1]` 范围，则截断为边界值。

---

#### 示例：

**示例 1**：
- 输入：`s = "42"`
- 输出：`42`

**示例 2**：
- 输入：`s = " -042"`
- 输出：`-42`

**示例 3**：
- 输入：`s = "1337c0d3"`
- 输出：`1337`

**示例 4**：
- 输入：`s = "0-1"`
- 输出：`0`

**示例 5**：
- 输入：`s = "words and 987"`
- 输出：`0`

---

#### 提示：
- `0 <= s.length <= 200`
- `s` 由英文字母、数字、`' '`、`'+'`、`'-'` 和 `'.'` 组成。

---

#### 解题思路：
1. **有限状态机（FSM）**：
   - 定义状态：`start`、`signed`、`in_number`、`end`。
   - 根据当前字符类型（空格、符号、数字、其他）切换状态。
   - 时间复杂度：`O(n)`，空间复杂度：`O(1)`。

2. **直接遍历法**：
   - 遍历字符串，按规则处理前导空格、符号和数字。
   - 在数字转换过程中检查溢出。
   - 时间复杂度：`O(n)`，空间复杂度：`O(1)`。

---

#### 伪代码（直接遍历法）：
```
function myAtoi(s):
    i = 0
    sign = 1
    num = 0
    n = len(s)
    # 跳过前导空格
    while i < n and s[i] == ' ':
        i += 1
    # 处理符号
    if i < n and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1
    # 转换数字
    while i < n and s[i].isdigit():
        digit = int(s[i])
        # 检查溢出
        if num > (2³¹ - 1 - digit) // 10:
            return 2³¹ - 1 if sign == 1 else -2³¹
        num = num * 10 + digit
        i += 1
    return sign * num
```

---

#### 注意事项：
- 前导空格不影响符号和数字的识别。
- 符号只能出现在数字之前，且只能有一个。
- 数字转换时需实时检查是否溢出。

---

#### 代码实现（Python，直接遍历法）：
```python
def myAtoi(s: str) -> int:
    i = 0
    sign = 1
    num = 0
    n = len(s)
    # 跳过前导空格
    while i < n and s[i] == ' ':
        i += 1
    # 处理符号
    if i < n and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1
    # 转换数字
    while i < n and s[i].isdigit():
        digit = int(s[i])
        # 检查溢出
        if num > (2**31 - 1 - digit) // 10:
            return 2**31 - 1 if sign == 1 else -2**31
        num = num * 10 + digit
        i += 1
    return sign * num
```

---

#### 复杂度分析：
- **时间复杂度**：`O(n)`，遍历字符串一次。
- **空间复杂度**：`O(1)`，仅使用常数空间。

---

#### 其他解法（有限状态机）：
```python
class StateMachine:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.num = 0
        self.transition_table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }
    
    def get_state(self, c):
        if c.isspace():
            return 0
        elif c == '+' or c == '-':
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3
    
    def process(self, c):
        self.state = self.transition_table[self.state][self.get_state(c)]
        if self.state == 'signed':
            self.sign = -1 if c == '-' else 1
        elif self.state == 'in_number':
            digit = int(c)
            if self.num > (2**31 - 1 - digit) // 10:
                self.num = 2**31 if self.sign == -1 else 2**31 - 1
                self.state = 'end'
            else:
                self.num = self.num * 10 + digit

def myAtoi(s: str) -> int:
    sm = StateMachine()
    for c in s:
        sm.process(c)
    return sm.sign * sm.num
```