class DetectorPipeline:

    def __init__(self):
        self.detectors = []

    def register(self, name, detector):
        self.detectors.append((name, detector))

    def run(self):

        results = {}

        for name, detector in self.detectors:
            results[name] = detector.detect()

        return results