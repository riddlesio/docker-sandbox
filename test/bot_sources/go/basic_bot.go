package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strings"
)

func main() {
	actions := [3]string{"rock", "paper", "scissors"}
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		words := strings.Split(line, " ")

		if words[0] != "action" {
			continue
		}

		choice := rand.Intn(3)
		fmt.Println(actions[choice])
	}
}
