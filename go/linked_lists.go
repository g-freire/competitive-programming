//package main
//
//import "fmt"
//
//// SINGLE LINKED LIST
//// first approach using simple node - https://golangbyexample.com/singly-linked-list-in-golang/
//// seccond approach using node with prev - https://www.golangprograms.com/golang-program-for-implementation-of-linked-list.html
//
//type LinkedList interface{
//	Count()
//	Traverse()
//	AddHead()
//	AddTail()
//	RemoveHead()
//	RemoveTail()
//	GetItem()
//	SetItem()
//	Reverse()
//}
//
//type node struct {
//	name string
//	next *node
//}
//
//type singleList struct {
//	len  int
//	head *node
//}
//
//func initList() *singleList {
//	return &singleList{}
//}
//
//// METHODS
//func (s *singleList) Size() int {
//	return s.len
//}
//
//func (s *singleList) Traverse() error{
//	if s.head == nil {
//		fmt.Errorf("Cannot traverse empty LL")
//	}else{
//		current := s.head
//		for current != nil{
//			fmt.Print(current.name, " -> ")
//			current = current.next
//		}
//	}
//	return nil
//}
//
//func (s *singleList) AddHead(name string) {
//	node := &node{
//		name: name,
//	}
//	if s.head == nil {
//		s.head = node
//	}else{
//		node.next = s.head
//		s.head = node
//	}
//	s.len++
//	return
//}
//
//func (s *singleList) AddTail(name string){
//	node := &node{
//		name: name,
//	}
//	if s.head == nil {
//		s.head = node
//	} else{
//		// traverse until next is nil
//		current := s.head
//		for current.next != nil{
//			current = current.next
//		}
//		current.next = node
//	}
//	s.len++
//	return
//}
//
//func cantHaveTwoMainSamePackage() {
//	singleList := initList()
//
//	//ADD HEAD METHOD
//	fmt.Printf("Size: %d\n", singleList.Size())
//	fmt.Printf("AddHead: A\n")
//	singleList.AddHead("A")
//	fmt.Printf("AddHead: B\n")
//	singleList.AddHead("B")
//	fmt.Printf("Size: %d\n", singleList.Size())
//
//
//	//ADD TAIL METHOD
//	fmt.Printf("AddTail: C\n")
//	singleList.AddTail("C")
//	err := singleList.Traverse()
//	if err != nil {
//		fmt.Println(err.Error())
//	}
//	//
//	//fmt.Printf("RemoveFront\n")
//	//err = singleList.RemoveFront()
//	//if err != nil {
//	//	fmt.Printf("RemoveFront Error: %s\n", err.Error())
//	//}
//	//
//	//fmt.Printf("RemoveBack\n")
//	//err = singleList.RemoveBack()
//	//if err != nil {
//	//	fmt.Printf("RemoveBack Error: %s\n", err.Error())
//	//}
//	//
//	//fmt.Printf("RemoveBack\n")
//	//err = singleList.RemoveBack()
//	//if err != nil {
//	//	fmt.Printf("RemoveBack Error: %s\n", err.Error())
//	//}
//	//
//	//fmt.Printf("RemoveBack\n")
//	//err = singleList.RemoveBack()
//	//if err != nil {
//	//	fmt.Printf("RemoveBack Error: %s\n", err.Error())
//	//}
//	//
//	//err = singleList.Traverse()
//	//if err != nil {
//	//	fmt.Println(err.Error())
//	//}
//	//
//	//fmt.Printf("Size: %d\n", singleList.Size())
//}