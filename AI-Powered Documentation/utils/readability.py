# Import the textstat library, which provides functions to compute readability scores
import textstat

# Define a function that computes readability metrics for the given text
def compute_readability_metrics(text):
    return {
        # Flesch Reading Ease: higher scores mean easier to read (0-100 scale)
        "flesch_reading_ease": textstat.flesch_reading_ease(text),

        # Gunning Fog Index: estimates years of formal education needed to understand the text
        "gunning_fog_index": textstat.gunning_fog(text),

        # Automated Readability Index: similar to Gunning Fog, gives a grade-level score
        "automated_readability_index": textstat.automated_readability_index(text)
    }
