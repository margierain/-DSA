// read Pset.md to understand the problem set solved for
// set = new Set(["quick", "brown", "the", "fox"])
// str = "thequickbrownfox";

function reconstruction_words (set, str) {
    res = []
    word = ""

    for (let char of str) {
        word += char
        if (set.has(word)) {
            res.push(word)
            word = ""
        }
    }

    return !res ? null: res;
};

console.log(reconstruction_words(new Set(["quick", "brown", "the", "fox"]), "thequickbrownfox"));