// 包，表明代码所在的模块（包）
package main

// 引入代码依赖
import (
	"fmt"
	"os"
)

// 程序主入口
func main() {
	if len(os.Args) > 1 {
		fmt.Println("Hello World", os.Args[1])
	} else {
		fmt.Println("Hello World")
	}
}
