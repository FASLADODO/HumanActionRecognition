import logging


class FeatureExtractor:

    def __init__(self, extractionStrategy):
        if extractionStrategy is not None:
            self.extract = extractionStrategy


    def extract(self):
        logging.error("The default extract() method was called. This should never happen.")


def siftExtraction(videoPath):
    logging.error("siftExtraction: This function is not implemented yet.")


def surfExtraction(videoPath):
    logging.error("surfExtraction: This function is not implemented yet.")
