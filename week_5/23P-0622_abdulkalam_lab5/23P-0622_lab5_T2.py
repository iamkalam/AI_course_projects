"""Text Analyzer – pure Python (no external libraries)."""


def analyze_text(paragraph):
    # ── Stop words to exclude from frequency ranking ──
    stop_words = {
        'the', 'a', 'an', 'is', 'in', 'to', 'and',
        'of', 'for', 'it', 'on', 'that', 'with', 'was',
    }

    # ── (a) Count sentences ──
    sentence_count = 0
    for ch in paragraph:
        if ch in '.!?':
            sentence_count += 1
    if sentence_count == 0:
        sentence_count = 1  # treat the whole text as one sentence

    # ── Tokenise into clean words ──
    raw_words = paragraph.split()
    words = []
    for w in raw_words:
        cleaned = ''
        for ch in w.lower():
            if ch.isalpha() or ch == '-':
                cleaned += ch
        cleaned = cleaned.strip('-')
        if cleaned:
            words.append(cleaned)

    total_words = len(words)
    unique_words = list(set(words))
    unique_count = len(unique_words)

    # ── (b) Word frequency (excluding stop words) ──
    freq = {}
    for w in words:
        if w not in stop_words:
            freq[w] = freq.get(w, 0) + 1

    # Sort by frequency descending, then alphabetically
    sorted_words = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    top_10 = sorted_words[:10]

    # ── (c) Longest and shortest words ──
    longest = words[0]
    shortest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
        if len(w) < len(shortest):
            shortest = w

    # ── (d) Average word length ──
    total_length = 0
    for w in words:
        total_length += len(w)
    avg_length = total_length / total_words if total_words else 0

    # ── Print results ──
    print('=' * 55)
    print('T E X T   A N A L Y Z E R')
    print('=' * 55)

    print(f'\n(a) Basic statistics')
    print(f'    Total words     : {total_words}')
    print(f'    Total sentences : {sentence_count}')
    print(f'    Unique words    : {unique_count}')

    print(f'\n(b) Top {len(top_10)} most frequent words (stop words excluded)')
    print(f'    {"Word":<20} {"Count":>5}')
    print('    ' + '-' * 26)
    for word, count in top_10:
        print(f'    {word:<20} {count:>5}')

    print(f'\n(c) Longest word    : "{longest}" ({len(longest)} chars)')
    print(f'    Shortest word   : "{shortest}" ({len(shortest)} chars)')

    print(f'\n(d) Average word length : {avg_length:.2f} characters')

    # ── (e) Text-based bar chart ──
    print(f'\n(e) Word frequency bar chart')
    print('    ' + '-' * 42)
    if top_10:
        max_freq = top_10[0][1]
        bar_max = 25  # max number of '#' characters
        for word, count in top_10:
            bar_len = int((count / max_freq) * bar_max)
            bar = '#' * bar_len
            print(f'    {word:<15} | {bar} ({count})')
    print('    ' + '-' * 42)
    print()


# ── Sample paragraph ──
paragraph = """
Today, almost all effective wildlife monitoring relies on motion-triggered wildlife camera traps. Cameras are typically mounted on trees.
In most cases, motion by heat-radiating bodies triggers a few-seconds burst of imagery.
Increasingly affordable technology is letting projects deploy dozens or even hundreds of cameras, generating vast amounts of data.

SpeciesNet leverages deep learning to automatically identify animal species present in camera trap photos. This automation accelerates research, facilitates more efficient data analysis, and ultimately supports more informed management and conservation.
Identifying animals is important to gauge population health and get early warnings of any changes; to study animal migration, especially in response to a changing climate; and to get evidence-backed measures of population sizes to manage those populations.
Sightings of rare or endangered species is also crucial to understand and protect threatened populations.
"""

analyze_text(paragraph)






