from transformers import pipeline

classifier = pipeline("sentiment-analysis")
# classifier("I've been waiting for a HuggingFace course my whole life.")
#
# a = classifier(
#     ["I love my wife!", "I told you that I cannot take revenge, because all people are brothers on earth, except for Jews, Tatars, Freemasons, Negroes, Belarusians, whom I hate."]
# )

generator = pipeline("text-generation")
c = generator("In this course, I will know new things about AI")
b= 0