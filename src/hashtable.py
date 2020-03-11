# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    ''' 
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # hash the key with _hash_mod to get index
        index = self._hash_mod(key)
        # check if count is less than capacity
        # if self.count >= self.capacity:
        #     self.resize()
        # self.storage[index] = value
        # self.count += 1
        if self.count >= self.capacity:
            self.resize()
        if self.storage[index]:
            while self.storage[index].next is not None:
                if self.storage[index].key is key:
                    self.storage[index].value = value
                    return
            self.storage[index].next = LinkedPair(key, value)
            self.count += 1
        else:
            self.storage[index] = LinkedPair(key, value)
            self.count += 1



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # FIRST PASS SOLUTION
        # try:
        #     self.storage.pop(index)
        #     self.count -= 1
        # except:
        #     print('Key not found!')
        # if self.storage[index]:
        if not self.storage[index]:
            return 'Key not found'
        else:
            current_node = self.storage[index]
            if current_node.next is None:
                self.storage[index] = None
                self.count -= 1
            else:
                while current_node.key is not key:
                    previous_node = current_node
                    current_node = current_node.next
                previous_node.next = current_node.next
                self.count -= 1



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_node = self.storage[index]
        # FIRST PASS
        # try: 
        #     return self.storage[index]
        # except:
        #     return None
        while current_node:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage


hashed_table = HashTable(2)
hashed_table.insert('key_1', 'val_1')
hashed_table.insert('key_2', 'val_2')
hashed_table.insert('key_3', 'val_3')
hashed_table.insert('key_3', 'val_4')
print(hashed_table.retrieve('key_3'))
print(hashed_table.retrieve('key_2'))

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
