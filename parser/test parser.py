from nltk.tokenize import sent_tokenize

with open("french-test.arff", "w", encoding="utf-8") as f:
    f.write(
        "@RELATION french\n\n"
        "@ATTRIBUTE text   string\n"
        "@ATTRIBUTE class  {CD,CI,DZ,FR,MA,SN}\n\n"
        "@DATA\n"
    )

for TLD in ["CD", "CI", "DZ", "FR", "MA", "SN"]:
    count = 0

    with open("FR-" + TLD + ".txt", "r", encoding="utf-8") as f:
        para = f.readlines()

    with open("french-test.arff", "a", encoding="utf-8") as f:
        for sentence in para:
            tokenized = sent_tokenize(sentence, language="french")
            for line in tokenized:
                line = line.replace("\"", "\\\"").replace("<p>", "\"").replace("</p>", "\", " + TLD + "\n")
                if "<doc" not in line and "</doc>" not in line and line.count(' ') > 1:
                    if line[0] != "\"":
                        line = "\" " + line
                    if str("\", " + TLD) not in line:
                        line = line.strip() + "\", " + TLD + "\n"
                    if count % 100 == 0:
                        f.write(line)
                    count += 1
