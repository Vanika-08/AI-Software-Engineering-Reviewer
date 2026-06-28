from agents.technology_detector import TechnologyDetector
from agents.structure_detector import StructureDetector
from agents.code_quality_detector import CodeQualityDetector
from agents.security_detector import SecurityDetector
from agents.architecture_detector import ArchitectureDetector
from agents.performance_detector import PerformanceDetector
from agents.best_practices_detector import BestPracticesDetector

class ReviewCoordinator:
    def __init__(self, project_files, extract_folder):

        self.project_files = project_files
        self.extract_folder = extract_folder
    
    def run(self):

        technology_detector = TechnologyDetector(self.project_files)
        technologies = technology_detector.detect()

        structure_detector = StructureDetector(self.extract_folder)
        structure = structure_detector.detect()

        quality_detector = CodeQualityDetector(self.project_files)
        quality = quality_detector.detect()

        security_detector = SecurityDetector(self.project_files)
        security = security_detector.detect()

        architecture_detector = ArchitectureDetector(self.extract_folder)
        architecture = architecture_detector.detect()

        performance_detector = PerformanceDetector(self.project_files)
        performance = performance_detector.detect()

        best_practices_detector = BestPracticesDetector(self.extract_folder)
        best_practices = best_practices_detector.detect()

        return {
            "technologies": technologies,
            "structure": structure,
            "quality": quality,
            "security": security,
            "architecture": architecture,
            "performance": performance,
            "best_practices": best_practices,
        }