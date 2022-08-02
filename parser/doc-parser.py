with open("french-docs.arff", "w", encoding="utf-8") as f:
  f.write(
    "@RELATION french\n\n"
    "@ATTRIBUTE text   string\n"
    "@ATTRIBUTE class  {CD,CI,DZ,FR,MA,SN}\n\n"
    "@DATA\n"
  )

for TLD in ["CD", "CI", "DZ", "FR", "MA", "SN"]:
  with open("FR-" + TLD + ".txt", "r", encoding="utf-8") as f:
    para = f.readlines()

  with open("french-docs.arff", "a", encoding="utf-8") as f:
    for line in para:
      line = line.replace("\n", " ").replace("\"", "\\\"").replace("<doc", "\"<doc").replace("</doc>", "</doc>\", " + TLD + "\n")
      if line.count(' ') > 1:
        f.write(line)
