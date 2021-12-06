letter_scores = {
    ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T') : 1,
    ('D', 'G') : 2,
    ('B', 'C', 'M', 'P') : 3,
    ('F', 'H', 'V', 'W', 'Y') : 4,
    ('K') : 5,
    ('J, X') : 8,
    ('Q', 'Z') : 10
}

def score(word):
    total_score = 0
    for char in word.upper():
        total_score += next(value for key, value in letter_scores.items() if char in key)

    return total_score