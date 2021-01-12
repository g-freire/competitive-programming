//2:19:20
package main

import "fmt"

type node struct {
	next *node
	data string
}

type ssl struct {
	head *node
	len int
}

func(s *ssl) addHead(data string) error{
	node := &node{
		data: data,
	}
	if s.head == nil{
		s.head = node
	}else {
		node.next = s.head
		s.head = node
	}
	s.len += 1
	return nil
}

func(s *ssl) removeTail() error{
	if s.head == nil{
		fmt.Errorf("EMPTY SSL HEAD NODE")
	}
	var prev *node
	current := s.head
	for current.next != nil {
		prev = current
		current = current.next
	}
	if prev != nil {
		
	}


	s.len--
	return nil

}

func(s *ssl) traverse() error{
	if s.head == nil {
		fmt.Errorf("EMPTY SLL HEAD NODE")
	}else{
		current := s.head
		for current != nil {
			fmt.Print(current.data, "->")
			current = current.next
		}
		fmt.Print("\n")
	}
	return nil
}

func(s *ssl) size() error {
	fmt.Printf("Size: %d\n", s.len)
	return nil
}

func main() {
	fmt.Print("SINGLE LINKED LIST \n")
	s := &ssl{}
	//s.size()
	s.addHead("A")
	s.traverse()
	//s.size()
	s.addHead("B")
	s.traverse()
	//s.size()
	s.removeTail()
	s.traverse()

}