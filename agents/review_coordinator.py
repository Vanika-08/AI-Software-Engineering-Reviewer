from agents.technology_detector import TechnologyDetector
from agents.structure_detector import StructureDetector
from agents.code_quality_detector import CodeQualityDetector
from agents.security_detector import SecurityDetector
from agents.architecture_detector import ArchitectureDetector
from agents.performance_detector import PerformanceDetector
from agents.best_practices_detector import BestPracticesDetector
from agents.score_calculator import ScoreCalculator
from agents.chunker import Chunker
from review.prompt_builder import PromptBuilder
from services.llm_service import LLMService
from services.embedding_service import EmbeddingService
from services.vector_store import VectorStore
from review.report_generator import ReportGenerator
from review.ai_review_parser import AIReviewParser

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

        print("Quality Issues:", len(quality))
        print("Security Issues:", len(security))
        print("Performance Issues:", len(performance))
        print("Architecture:", architecture)
        print("Best Practices:", best_practices)

        score_calculator = ScoreCalculator()

        score = score_calculator.calculate(
            quality,
            security,
            performance,
            best_practices,
            architecture
        )

        chunker = Chunker(self.project_files)
        chunks = chunker.create_chunks()

        context = chunks[0]

        embedding_service = EmbeddingService()

        embeddings = embedding_service.create_embeddings(chunks)

        vector_store = VectorStore()

        vector_store.store(chunks, embeddings)

        query = "Review this project"

        query_embedding = embedding_service.create_query_embedding(query)

        results = vector_store.search(query_embedding)

        context = "\n\n".join(results["documents"][0])

        report = {
            "technologies": technologies,
            "structure": structure,
            "quality": quality,
            "security": security,
            "performance": performance,
            "architecture": architecture,
            "best_practices": best_practices,
            "score": score
        }

        prompt_builder = PromptBuilder()

        prompt = prompt_builder.build(report, context)

        llm = LLMService()
        ai_review = llm.review(prompt)

        print("========== RAW AI REVIEW ==========")
        print(ai_review)

        parser = AIReviewParser()

        parsed_review = parser.parse(ai_review)

        print("========== PARSED REVIEW ==========")
        print(parsed_review)

        report["ai_review"] = parsed_review

        print("CALLING REPORT GENERATOR")

        generator = ReportGenerator()

        generator.generate(
            report,
            "review_report.pdf"
        )

        print("PDF GENERATED")

        report["total_chunks"] = len(chunks)

        return report