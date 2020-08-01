## 数据结构篇——栈的习题

- [x] 155. 最小栈
- [x] 150. 逆波兰表达式求值

### [01. 最小栈]( https://leetcode-cn.com/problems/min-stack/ )

#### **1.1 题目说明：**

>155.  最小栈（难度：简单）
>
>设计一个支持 push ，pop ，top 操作，**并能在常数时间内检索到最小元素的栈。**
>
>- push(x) —— 将元素 x 推入栈中。
>- pop() —— 删除栈顶的元素。
>- top() —— 获取栈顶元素。
>- getMin() —— 检索栈中的最小元素。
>
>**示例：**
>
>```
>输入：
>["MinStack","push","push","push","getMin","pop","top","getMin"]
>[[],[-2],[0],[-3],[],[],[],[]]
>
>输出：
>[null,null,null,null,-3,null,0,-2]
>
>解释：
>MinStack minStack = new MinStack();
>minStack.push(-2);
>minStack.push(0);
>minStack.push(-3);
>minStack.getMin();   --> 返回 -3
>minStack.pop();
>minStack.top();      --> 返回 0.
>minStack.getMin();   --> 返回 -2
>```

#### **1.2 解题思路：**

&#8195;根据栈的特性，即只能**在O（1）的时间复杂度内操作栈顶元素**，所以为了保证用常数时间检索到栈内的最小元素，则必须让**最小元素位于栈顶**，所以此处只能用**空间换时间**，用**两个栈实现，一个最小栈始终保证最小值在顶部** 

#### **1.3 题解代码（逐行解释版）：**

- [Python](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Python/155_MinStack.py )
- [Java](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Java/src/main/java/com/skymoon/MinStack.java)
- [Scala](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Scala/src/main/scala/com/skymoon/solutionMinStack155.scala)
- [Go](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Go/minStackSolution.go)

### [02. 逆波兰表达式求值]( https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/ )

#### **2.1 题目说明：**

>150. 逆波兰表达式求值（难度：中等）
>
>根据 逆波兰表示法，求表达式的值。
>
>有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
>
>**说明：**
>
>- 整数除法只保留整数部分。
>- 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
>
>**示例：**
>
>```
># 示例 1：
>输入: ["2", "1", "+", "3", "*"]
>输出: 9
>解释: 该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
>
># 示例 2：
>输入: ["4", "13", "5", "/", "+"]
>输出: 6
>解释: 该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
>
># 示例 3：
>输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
>输出: 22
>解释: 
>该算式转化为常见的中缀算术表达式为：
>  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
>= ((10 * (6 / (12 * -11))) + 17) + 5
>= ((10 * (6 / -132)) + 17) + 5
>= ((10 * 0) + 17) + 5
>= (0 + 17) + 5
>= 17 + 5
>= 22
>
>```

#### **2.2 解题思路：**

&#8195;首先，得先理解什么是**逆波兰表达式**。

> **逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。**
>
> - 平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
> - 该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。
>
> **逆波兰表达式主要有以下两个优点：**
>
> - 去掉括号后表达式无歧义，上式即便写成 1 2 + 3 4 + * 也可以依据次序计算出正确结果。
> - 适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中

&#8195;其实，引用中的优点已经说明了本题的解法。由于逆波兰表达式是一种后缀表达式，**其运算符主要负责其前面相邻的数字的运算规则**，所以只需要在**遇到运算符的时候对它之前离它最近的数字进行运算**即可。很明显，这非常适合利用栈进行运算。所以，大致思路即为：**遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中**

#### **2.3 题解代码（逐行解释版）：**

- [Python](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Python/150_evalRPN.py)
- [Java](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Java/src/main/java/com/skymoon/EvalRpn.java)
- [Scala](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Scala/src/main/scala/com/skymoon/solutionEvalRPN150.scala)
- [Go](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Go/evalRPNSolution.go)

