//package main
//
//import "fmt"
//
//// SINGLE LINKED LIST
//
//type ssl struct {
//	head *node
//	len int
//}
//type node struct{
//	next *node
//	data string
//}
//
//func (ssl *ssl) addHead(data string) error{
//	node := &node{
//		data: data,
//	}
//	if ssl.head == nil{
//		fmt.Errorf("sll head is empty")
//		ssl.head = node
//	}else{
//		node.next = ssl.head
//		ssl.head = node
//	}
//	return nil
//}
//
//func(s *ssl) traverse() error{
//	if s.head == nil{
//		fmt.Errorf("empty ssl")
//	}else{
//		currentNode := s.head
//		for currentNode != nil {
//			fmt.Print(currentNode.data, "->")
//			currentNode = currentNode.next
//		}
//		fmt.Print("\n")
//
//	}
//	return nil
//}
//
//func main() {
//	ssl := &ssl{}
//	ssl.addHead("A")
//    ssl.traverse()
//	ssl.addHead("B")
//	ssl.traverse()
//	return
//
//}