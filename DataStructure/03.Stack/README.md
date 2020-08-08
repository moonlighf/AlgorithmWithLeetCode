## 数据结构篇——栈的习题

- [x] 155. [最小栈(简单)](https://github.com/moonlighf/AlgorithmWithLeetCode/tree/master/DataStructure/03.Stack#01-最小栈) 
- [x] 150. [逆波兰表达式求值(中等)](https://github.com/moonlighf/AlgorithmWithLeetCode/tree/master/DataStructure/03.Stack#02-逆波兰表达式求值) 
- [x] 394. [字符串解码(中等)](https://github.com/moonlighf/AlgorithmWithLeetCode/tree/master/DataStructure/03.Stack#03-字符串解码) 
- [x] 394. [二叉树的中序遍历(中等)](https://github.com/moonlighf/AlgorithmWithLeetCode/tree/master/DataStructure/03.Stack#04-二叉树的中序遍历) 
  

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

### [03. 符串解码](https://leetcode-cn.com/problems/decode-string/)

#### **3.1 题目说明：**

>394. 字符串解码（难度：中等）
>
>给定一个经过编码的字符串，返回它解码后的字符串。
>
>编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
>
>你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
>
>此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
>
>示例 1：
>
>```
>输入：s = "3[a]2[bc]"
>输出："aaabcbc"
>```
>
>
>示例 2：
>
>```
>输入：s = "3[a2[c]]"
>输出："accaccacc"
>```
>
>
>示例 3：
>
>```
>输入：s = "2[abc]3[cd]ef"
>输出："abcabccdcdcdef"
>```
>
>示例 4：
>
>```
>输入：s = "abc3[cd]xyz"
>输出："abccdcdcdxyz"
>```

#### **3.2 解题思路：**
&#8195;对于这种需要按照某种顺序对一个序列进行操作的题目，可以逐一考虑需要用到的数据类型。这里考虑到后面入的元素需要优先操作，所以选择栈进行辅助操作。

&#8195;对于原字符串，可能存在四种可能，分别是`数字0-9`，`[`，`字母a-z`，`]`，所以只需要分别考虑这四种元素入栈时操作即可：

- 数字0-9：正常入栈
- [：正常入栈
- ]：pop出栈顶元素，直到遇到和其对应的`[`, 这之间的字母就是需要被复制的字母，然后往前pop出数字，即为复制的次数。然后将复制后的字母入栈即可
- 字母a-z：正常入栈

#### **3.3 题解代码（逐行解释版）：**

- [Python](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Python/394_decodeString.py)
- [Java](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Java/src/main/java/com/skymoon/DecodeString.java)
- [Scala](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Scala/src/main/scala/com/skymoon/solutionDecodeString394.scala )
- [Go](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Go/decodeStringSolution.go)

### [04. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)

#### **4.1 题目说明：**

> 给定一个二叉树，返回它的*中序* 遍历。 
>
>示例:
>
>```
>输入: [1,null,2,3]
>   1
>    \
>     2
>    /
>   3
>
>输出: [1,3,2]
>```
>
>
>进阶: 递归算法很简单，你可以通过迭代算法完成吗？

#### **4.2 解题思路：**

首先需要了解二叉树的中序遍历，这里顺便也复习下二叉树的其他几种遍历：

- 前序遍历： 访问根结点的操作发生在遍历其左右子树之前 
- 中序遍历： 访问根结点的操作发生在遍历其左右子树之中 
- 后序遍历： 访问根结点的操作发生在遍历其左右子树之后 
- 层序遍历： 从根节点开始，从上往下逐层遍历，同一层按从左往右逐个访问

同时，也顺便复习下二叉树本身的性质，这些性质可以再代码中灵活使用以达到减少复杂度的效果。

>经过前人的总结，二叉树具有以下几个性质：
>
>1. 二叉树中，第 i 层最多有 ` 2i-1 `个结点。
>2. 如果二叉树的深度为 K，那么此二叉树最多有 `2K-1` 个结点。
>3. 二叉树中，终端结点数（叶子结点数）为 `n0`，度为 2 的结点数为 `n2`，则 `n0=n2+1`。

#### **4.3 题解代码（逐行解释版）：**

- [Python](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Python/94_inorderTraversal.py)
- [Java](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Java/src/main/java/com/skymoon/InorderTraversal.java)
- [Scala](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Scala/src/main/scala/com/skymoon/solutionInorderTraversal94.scala)
- [Go](https://github.com/moonlighf/AlgorithmWithLeetCode/blob/master/DataStructure/03.Stack/Go/inorderTraversalSolution.go)