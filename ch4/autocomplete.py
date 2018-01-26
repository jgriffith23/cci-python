"""Implement an autocomplete with a trie"""


class TrieNode():
    def __init__(self, letter, prefixes=None):
        self.letter = letter

        if prefixes is None:
            self.prefixes = {}
        else:
            self.prefixes = prefixes

    def __repr__(self):
        return f"<TrieNode letter: {self.letter}>"

    def add(self, word):
        """Add a new word to the trie."""

        if word[0] not in self.prefixes:
            letters = list(word[-1::-1])
            curr_node = TrieNode(letters.pop())
            self.prefixes[word[0]] = curr_node

            while letters:
                next_node = TrieNode(letters.pop())
                curr_node.prefixes[next_node.letter] = next_node
                curr_node = next_node

            curr_node.prefixes["*"] = None

        elif len(word) > 1:
            self.prefixes[word[0]].add(word[1:])

    def find(self, word):
        """Search for a word in the trie."""

        if "*" in self.prefixes and len(word) == 0:
            return True

        if word[0] not in self.prefixes:
            return False

        start = self.prefixes[word[0]]

        return start.find(word[1:])

    def get_ending_node(self, word):
        """Find the last node of a prefix in the trie."""

        if len(word) > 0:
            if word[0] not in self.prefixes:
                return None

            start = self.prefixes[word[0]]

            return start.get_ending_node(word[1:])

        return self

    def get_words(self, prefix):
        """Get all words from this node that could match the input letters."""

        if prefix[0] not in self.prefixes.keys():
            return []

        words = set([])
        curr_word = list(prefix[:-1])
        to_visit = [self.get_ending_node(prefix)]

        while to_visit:
            curr_node = to_visit.pop()

            if curr_node is None:
                continue

            curr_word.append(curr_node.letter)
            to_visit.extend(list(curr_node.prefixes.values()))

            if "*" in curr_node.prefixes:
                words.add("".join(curr_word))

                if list(curr_node.prefixes.keys()) == ["*"]:
                    curr_word.pop()

        return sorted(words)

    def delete(self, word):
        pass


def autocomplete(trie):
    """Run a REPL and let users ask for available words."""

    having_fun = True

    while having_fun:
        print("\nType part of a word.")
        prefix = input("> ").lower()

        possibilities = trie.get_words(prefix)[:5]
        print("Maybe you meant:")
        for word in possibilities:
            print("-", word)

        print("Do you want to keep typing?")
        answer = input("(y or n) > ").lower()
        if answer == "n":
            break
        elif answer != "y":
            print("I don't understand that answer.")

    print("Hope you liked the autocomplete!\n")


if __name__ == "__main__":
    start = TrieNode("start")
    with open("/usr/share/dict/words") as words:
        word_list = [next(words).rstrip() for w in range(1000)]
        for word in word_list:
            print(word)
            start.add(word.lower())

    # end = TrieNode("*")
    # a2 = TrieNode("a", prefixes={"*": None})
    # y1 = TrieNode("y", prefixes={"*": None})
    # y2 = TrieNode("y", prefixes={"*": None})
    # n = TrieNode("n", prefixes={"y": y2, "*": None, "a": a2})
    # a1 = TrieNode("a", prefixes={"n": n, "*": None})
    # m = TrieNode("m", prefixes={"a": a1, "y": y1})

    # start = TrieNode("start", prefixes={"m": m})

    autocomplete(start)
