import difflib

def calculate_similarity(text1, text2):
    similarity = difflib.SequenceMatcher(None, text1, text2).ratio()
    return similarity

def check_plagiarism(text1, text2, threshold=0.8):
    similarity = calculate_similarity(text1, text2)
    if similarity >= threshold:
        return True, similarity
    else:
        return False, similarity

if __name__ == "__main__":
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")

    is_plagiarized, similarity = check_plagiarism(text1, text2)

    if is_plagiarized:
        print(f"Plagiarism detected! Similarity: {similarity:.2%}")
    else:
        print(f"No plagiarism detected. Similarity: {similarity:.2%}")
