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
from agents.complexity_detector import ComplexityDetector
from agents.duplicate_code_detector import DuplicateCodeDetector
from agents.dead_code_detector import DeadCodeDetector
from agents.naming_detector import NamingDetector
from agents.documentation_detector import DocumentationDetector
from agents.test_detector import TestDetector

import time


class ReviewCoordinator:

    def __init__(self, project_files, extract_folder):

        self.project_files = project_files
        self.extract_folder = extract_folder

    def run(self):

        overall_start = time.perf_counter()

        # ---------------- Technology ----------------

        start = time.perf_counter()
        technology_detector = TechnologyDetector(self.project_files)
        technologies = technology_detector.detect()
        print(f"Technology Detector : {time.perf_counter() - start:.2f}s")

        # ---------------- Structure ----------------

        start = time.perf_counter()
        structure_detector = StructureDetector(self.extract_folder)
        structure = structure_detector.detect()
        print(f"Structure Detector : {time.perf_counter() - start:.2f}s")

        # ---------------- Quality ----------------

        start = time.perf_counter()
        quality_detector = CodeQualityDetector(self.project_files)
        quality = quality_detector.detect()
        print(f"Quality Detector : {time.perf_counter() - start:.2f}s")

        # ---------------- Security ----------------

        start = time.perf_counter()
        security_detector = SecurityDetector(self.project_files)
        security = security_detector.detect()
        print(f"Security Detector : {time.perf_counter() - start:.2f}s")

        # ---------------- Performance ----------------

        start = time.perf_counter()
        performance_detector = PerformanceDetector(self.project_files)
        performance = performance_detector.detect()
        print(f"Performance Detector : {time.perf_counter() - start:.2f}s")

        # ---------------- Complexity ----------------

        start = time.perf_counter()
        complexity_detector = ComplexityDetector(self.project_files)
        complexity = complexity_detector.detect()
        print(f"Complexity Detector : {time.perf_counter() - start:.2f}s")

        # ---------------- Duplicate ----------------

        start = time.perf_counter()
        duplicate_detector = DuplicateCodeDetector(self.project_files)
        duplicate_code = duplicate_detector.detect()
        print(f"Duplicate Detector : {time.perf_counter() - start:.2f}s")

        # ---------------- Dead Code ----------------

        start = time.perf_counter()
        dead_code_detector = DeadCodeDetector(self.project_files)
        dead_code = dead_code_detector.detect()
        print(f"Dead Code Detector : {time.perf_counter() - start:.2f}s")

        # ---------------- Naming ----------------

        start = time.perf_counter()
        naming_detector = NamingDetector(self.project_files)
        naming = naming_detector.detect()
        print(f"Naming Detector : {time.perf_counter() - start:.2f}s")

        # ---------------- Documentation ----------------

        start = time.perf_counter()
        documentation_detector = DocumentationDetector(self.project_files)
        documentation = documentation_detector.detect()
        print(f"Documentation Detector : {time.perf_counter() - start:.2f}s")

        # ---------------- Testing ----------------

        start = time.perf_counter()
        test_detector = TestDetector(self.project_files)
        tests = test_detector.detect()
        print(f"Test Detector : {time.perf_counter() - start:.2f}s")

        # ---------------- Architecture ----------------

        start = time.perf_counter()
        architecture_detector = ArchitectureDetector(self.extract_folder)
        architecture = architecture_detector.detect()
        print(f"Architecture Detector : {time.perf_counter() - start:.2f}s")

        # ---------------- Best Practices ----------------

        start = time.perf_counter()
        best_practices_detector = BestPracticesDetector(self.extract_folder)
        best_practices = best_practices_detector.detect()
        print(f"Best Practices Detector : {time.perf_counter() - start:.2f}s")

        # ---------------- Score ----------------

        start = time.perf_counter()

        score_calculator = ScoreCalculator()

        score = score_calculator.calculate(
            quality,
            security,
            performance,
            complexity,
            duplicate_code,
            dead_code,
            documentation,
            tests,
            naming,
            best_practices,
            architecture
        )

        print(f"Score Calculation : {time.perf_counter() - start:.2f}s")

        # ---------------- Chunking ----------------

        start = time.perf_counter()

        chunker = Chunker(self.project_files)
        chunks = chunker.create_chunks()

        print(f"Chunking : {time.perf_counter() - start:.2f}s")

        # ---------------- Embeddings ----------------

        embedding_service = EmbeddingService()

        start = time.perf_counter()

        embeddings = embedding_service.create_embeddings(chunks)

        print(f"Embeddings : {time.perf_counter() - start:.2f}s")

        # ---------------- Vector Store ----------------

        vector_store = VectorStore()

        start = time.perf_counter()

        vector_store.store(chunks, embeddings)

        print(f"Vector Store : {time.perf_counter() - start:.2f}s")

        query = "Review this project"

        query_embedding = embedding_service.create_query_embedding(query)

        start = time.perf_counter()

        results = vector_store.search(query_embedding)

        print(f"Vector Search : {time.perf_counter() - start:.2f}s")

        context = "\n\n".join(results["documents"][0])

        report = {
            "technologies": technologies,
            "structure": structure,
            "quality": quality,
            "security": security,
            "complexity": complexity,
            "duplicate_code": duplicate_code,
            "dead_code": dead_code,
            "documentation": documentation,
            "tests": tests,
            "naming": naming,
            "performance": performance,
            "architecture": architecture,
            "best_practices": best_practices,
            "score": score,
        }

        # ---------------- Prompt ----------------

        prompt_builder = PromptBuilder()

        start = time.perf_counter()

        prompt = prompt_builder.build(report, context)

        print(f"Prompt Build : {time.perf_counter() - start:.2f}s")

        # ---------------- Gemini ----------------

        llm = LLMService()

        start = time.perf_counter()

        ai_review = llm.review(prompt)

        print(f"Gemini Review : {time.perf_counter() - start:.2f}s")

        # ---------------- Parse ----------------

        parser = AIReviewParser()

        start = time.perf_counter()

        parsed_review = parser.parse(ai_review)

        print(f"AI Parser : {time.perf_counter() - start:.2f}s")

        report["ai_review"] = parsed_review

        # ---------------- PDF ----------------

        generator = ReportGenerator()

        start = time.perf_counter()

        generator.generate(
            report,
            "review_report.pdf"
        )

        print(f"PDF Generation : {time.perf_counter() - start:.2f}s")

        report["total_chunks"] = len(chunks)

        print("\n" + "=" * 60)
        print(f"TOTAL REVIEW TIME : {time.perf_counter() - overall_start:.2f}s")
        print("=" * 60)

        return report