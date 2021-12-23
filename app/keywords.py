from typing import List

import yake

from app.data import Data
from app.nlp import get_tags


def get_keywords(text: str, max_ngram: int, n_keywords: int) -> List[str]:
    keywords = yake.KeywordExtractor(
        lan="en",
        n=max_ngram,
        dedupLim=0.3,
        top=n_keywords,
    ).extract_keywords(text)
    return [s[0].title() for s in keywords]


if __name__ == '__main__':
    db = Data()
    data = db.find({})[:5]
    for d in data:
        print(f"\nBox_id: {d['box_id']}")
        print(f"Old Tags: {get_tags(d['text'])}")
        print(f"New Tags: {d['tags']}")