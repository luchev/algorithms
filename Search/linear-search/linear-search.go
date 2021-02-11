package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func linearSearch(haystack []int, needle int) int {
	for index, value := range haystack {
		if value == needle {
			return index
		}
	}
	return -1
}

func parseInts(input string) []int {
	fields := strings.Fields(input)
	ints := make([]int, len(fields))
	for index, value := range fields {
		ints[index], _ = strconv.Atoi(value)
	}
	return ints
}

func test() {
	reader := bufio.NewReader(os.Stdin)
	reader.ReadLine()
	numbersLine, _ := reader.ReadString('\n')
	numbers := parseInts(numbersLine)
	queriesLine, _ := reader.ReadString('\n')
	queries := parseInts(queriesLine)
	for _, query := range queries {
		fmt.Print(linearSearch(numbers, query), " ")
	}
}

func main() {
	test()
}
