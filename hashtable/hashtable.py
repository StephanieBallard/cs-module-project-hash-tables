class HashTableEntry: # class Node
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8 # this is the smallest our hash table can be
# table = [None] * 8

class HashTable: # linked list of hash table entries, get and put change from putting a single entry into your table to now needing to go through the linked list 
    
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity # capacity is the number of buckets that we have available in our hash table
        self.buckets = [None] * capacity # this is a property
        self.count = 0

        # Capacity is the amount of items in the hashtable
        # Buckets are the amount of indexes we have avail in the hashtable
        # we can have 4 buckets, but ten pieces of data to put into it. the 6 extra pieces of data will be stored via linked list

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.buckets)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        # Psuedo code
        # FNV_prime is the 64-bit FNV prime value: 1099511628211
        # FNV_offset_basis is the 64-bit FNV offset basis value: 14695981039346656037
        # algorithm fnv-1a is
        # hash := FNV_offset_basis
        # for each byte_of_data to be hashed do
        # hash := hash XOR byte_of_data
        # hash := hash × FNV_prime

        FNV_offset = 14695981039346656037
        FNV_prime = 1099511628211

        string_key = str(key).encode()
        hash = FNV_offset

        for i in string_key:
            hash *= FNV_prime
            hash ^= i
        
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        
    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # get the index for the key
        # search the linked list at the index for the key
        # if the key is found, overwrite the value stored there
        # else insert the key and value at the head of the list at that index

        # *** only increase the count of the size of the hash table if u are inserting in the put func

        # Your code here
        
        index = self.hash_index(key)
        cur = self.buckets[index]

        # does key exist? is it what we are looking for? if it's there overwrite it
        while cur is not None and cur.key != key:
            cur = cur.next

        if cur is not None:
            cur.value = value
        else:
            new_entry = HashTableEntry(key,value)
            new_entry.next = self.buckets[index]
            self.buckets[index] = new_entry
        
        self.count += 1
        
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
    
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        # get the index for the key
        # search the linked list for the key at that index
        # if found, delete it, return it
        # else return None

        # Your code here
        # Special case of empty head
        index = self.hash_index(key)
        cur = self.buckets[index]
        prev = None

        while cur is not None and cur.key != key:
            prev = cur
            cur = prev.next
        
        if cur is None:
            return None
        
        else:
            if prev is None:
                self.buckets[index] = cur.next
            else:
                prev.next = cur.next

        self.count -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

    # get the index for the key
    # search the linked list at that index for the key
    # if found, return the value
    # else return None

        # Your code here
        index = self.hash_index(key)
        cur = self.buckets[index]

        while cur is not None:
            if cur.key == key:
                return cur.value
            else:
                cur = cur.next

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [None] * self.capacity # [None] = an empty bucket, array of hash items that are in the linked list
        cur = None

        # loop through old buckets and reassign them to the new list because there will be different indexes now, the % needs to be redone
        for node in old_buckets:
            cur = node
            while cur is not None:
                self.put(cur.key, cur.value)
                cur = cur.next

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
