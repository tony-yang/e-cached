// Core engine of the cache db
package ecached

import (
  "fmt"
)

type ecached struct {
  cache map[string]string
}

func New() ecached {
  fmt.Println("Creating a new ecached object")
  c := ecached {make(map[string]string)}
  return c
}

// Create a new key value pair to the cache or updating the value
// of an existing key
func (c ecached) Set(k string, v string) {
  c.cache[k] = v
}

// Get the value from the cache by key
func (c ecached) Get(k string) string {
  return c.cache[k]
}
