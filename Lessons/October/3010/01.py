from transformers import pipeline

classifier = pipeline("sentiment-analysis")
# classifier("I've been waiting for a HuggingFace course my whole life.")
#
# a = classifier(
#     ["I love my wife!", "I told you that I cannot take revenge, because all people are brothers on earth, except for Jews, Tatars, Freemasons, Negroes, Belarusians, whom I hate."]
# )
#
# generator = pipeline("text-generation")
# c = generator("In this course, I will know new things about AI")
# generator = pipeline("text-generation", model="distilgpt2")
# d = generator(
#     "In this course, we will teach you how to make new things with AI",
#     max_length=30,
#     num_return_sequences=2,
# )


ner = pipeline("ner", aggregation_strategy="average", model="dslim/distilbert-NER")
# ner = pipeline("ner", aggregation_strategy="simple", model="dslim/distilbert-NER")
e = ner(["My name is Nik and I work at Infobus in Prague.","My name is Sam and I work at Dodo in Prague."])
print(e)
b= 0
text = "My name is Nik and I work at Infobus in Prague."

entities = [
    {"entity_group": "PER", "score": 0.99, "start": 11, "end": 14},
    {"entity_group": "ORG", "score": 0.62, "start": 29, "end": 36},
    {"entity_group": "LOC", "score": 0.98, "start": 40, "end": 46},
]

def extract_words(text, entities):
    words = []
    for entity in entities:
        words.append(text[entity["start"]:entity["end"]])
    return words

def filter_by_score(entities, min_score):
    filtered_entities = []
    for entity in entities:
        if entity["score"] >= min_score:
            filtered_entities.append(entity)
    return filtered_entities

def  group_by_type(text, entities):
