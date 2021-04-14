/* *****************************************************
 * @File Name   : test
 * @Author      : SkyMoon
 * @Email       : skymoon9406@gmail.com
 * @Create Date : 2021/4/1
 * @Description :
 * *****************************************************/
package main

import (
	"fmt"
)


func main() {
	trie := Constructor()
	trie.Insert("apple")
	fmt.Println(trie.Search("apple"))
	fmt.Println(trie.Search("app"))
	fmt.Println(trie.StartsWith("app"))
	trie.Insert("app")
	fmt.Println(trie.Search("app"))
}

type Trie struct {
	isEnd bool
	children [26] * Trie
}


/** Initialize your data structure here. */
func Constructor() Trie {
	return Trie{}
}


/** Inserts a word into the trie. */
func (this *Trie) Insert(word string)  {
	node := this
	// 遍历字符串数组，然后插入到前缀树中
	for _, chr := range word{
		// 获取当前字符的ascii码差值，用于在Trie的children中索引
		chr -= 'a'
		// 如果该字符已经在前缀树之中就跳过，否则，添加到Trie中
		if node.children[chr] == nil {
			node.children[chr] = &Trie{}
		}
		// 前缀树也进入下一层
		node = node.children[chr]
	}
	// 遍历结束后最后一个节点的isEnd置为true
	node.isEnd = true
}

func (this *Trie) SearchPrefix(prefix string) *Trie {
	node := this
	// 查找是否以某个字符串开始，就是根据该字符串的每个字符来查找是否在前缀树中
	for _, chr := range prefix{
		chr -= 'a'
		// 如果该字符已经在前缀树之中就跳过，否则，添加到Trie中
		if node.children[chr] == nil {
			return nil
		}
		// 前缀树也进入下一层
		node = node.children[chr]
	}
	// 如果遍历结束都没有发现不在的字符串的话，就返回最终的节点，该节点记录了是isEnd
	return node
}


/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
	// 查找就是根据该字符串的每个字符来查找是否在前缀树中，且节点为最终节点
	node := this.SearchPrefix(word)
	return  node != nil && node.isEnd
}


/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
	node := this.SearchPrefix(prefix)
	return node != nil
}
