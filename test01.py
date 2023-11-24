def analyze_sentence(sentence):
    words = sentence.split()

    word_count = {}
    duplicate_words = {}

    for word in words:
        # นับจำนวนคำ
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

        # เก็บข้อมูลคำที่ซ้ำ
        if word_count[word] > 1:
            duplicate_words[word] = word_count[word]

    total_words = len(words)
    total_duplicates = len(duplicate_words)

    print(f"ประโยคนี้ประกอบด้วยคำทั้งหมด {total_words} คำ")
    print(f"มีคำที่ซ้ำกันรวม {total_duplicates} คำ")

    if total_duplicates > 0:
        print("คำที่ซ้ำกันคือ:")
        for word, count in duplicate_words.items():
            print(f"คำ '{word}' ซ้ำ {count} ครั้ง")

print("++++++++++++++++++++++++++++++++++++++")
user_sentence = input("ป้อนประโยค (ภาษาอังกฤษ): ")
print("++++++++++++++++++++++++++++++++++++++")
analyze_sentence(user_sentence)
print("++++++++++++++++++++++++++++++++++++++")