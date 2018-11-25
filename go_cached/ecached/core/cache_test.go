package ecached

import (
  "testing"
)

func TestSetGetKey(t *testing.T) {
  entries := []struct {
    key string
    val string
  } {
    {"test-key", "15"},
  }

  c := New()
  for _, entry := range entries {
    c.Set(entry.key, entry.val)
    actual := c.Get(entry.key)
    if actual != entry.val {
      t.Errorf("The cache stored incorrect value: key = %s value = %s expected value = %s", entry.key, actual, entry.val)
    }
  }
}
