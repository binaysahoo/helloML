package main

import (
	"fmt"
	"time"
)

func asyncTask(id int, result chan<- int) {
	// Perform some time-consuming task asynchronously
	time.Sleep(2 * time.Second)

	// Send the result through the channel
	result <- id * 2
}

func main() {
	// Create a channel to receive results
	resultChan := make(chan int)

	// Launch multiple goroutines to perform async tasks
	for i := 1; i <= 5; i++ {
		go asyncTask(i, resultChan)
	}

	// Wait for results from all goroutines
	for i := 1; i <= 5; i++ {
		result := <-resultChan
		fmt.Println("Result:", result)
	}
}

