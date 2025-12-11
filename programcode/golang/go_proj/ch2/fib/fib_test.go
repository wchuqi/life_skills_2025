package fib_test

import (
	"testing"
)

// 全局变量
var ALL_A int

func Test_Fib_Generate(t *testing.T) {
	ALL_A = 100
	t.Log("全局变量：", ALL_A)
	// var a int = 1
	// var b int = 1
	var (
		a int = 1
		b int = 1 // 或者 b := 1，go具有类型推断能力
	)
	t.Log(a)
	for i := 0; i < 6; i++ {
		t.Log("", b)
		tmp := a
		a = b
		b = tmp + a
	}
}

func Test_change_1(t *testing.T) {
	a := 1
	b := 2
	t.Log(a, b)
	a, b = b, a
	t.Log(a, b)
}
