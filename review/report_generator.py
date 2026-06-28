from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors


class ReportGenerator:

    def generate(self, report, output_path):
        print("NEW REPORT GENERATOR RUNNING")

        doc = SimpleDocTemplate(output_path)

        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph(
                "AI Software Engineering Review",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph("<b>Overall Score</b>", styles["Heading2"])
        )

        elements.append(
            Paragraph(
                str(report["score"]["overall_score"]) + "/100",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph("<b>Project Structure</b>", styles["Heading2"])
        )

        for key, value in report["structure"].items():
            elements.append(
                Paragraph(f"{key}: {'Yes' if value else 'No'}", styles["BodyText"])
            )

        print(report["technologies"])

        tech = report["technologies"]

        elements.append(
            Paragraph("<b>Technology Stack</b>", styles["Heading2"])
        )

        elements.append(
            Paragraph(f"Frontend: {tech['frontend']}", styles["BodyText"])
        )

        elements.append(
             Paragraph(f"Backend: {tech['backend']}", styles["BodyText"])
        )

        elements.append(
            Paragraph(f"Database: {tech['database']}", styles["BodyText"])
        )

        elements.append(
            Paragraph("<b>Security Findings</b>", styles["Heading2"])
        )

        security_data = [
            ["Severity", "Issue", "File"]
        ]

        for issue in report["security"]:
            security_data.append([
                issue["severity"],
                issue["issue"],
                issue["file"]
        ])

        security_table = Table(security_data)

        security_table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.grey),
            ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),

            ("GRID", (0,0), (-1,-1), 1, colors.black),

            ("BACKGROUND", (0,1), (-1,-1), colors.beige),

            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

            ("BOTTOMPADDING", (0,0), (-1,0), 8),
        ]))

        elements.append(security_table)

        elements.append(
            Paragraph("<b>AI Review</b>", styles["Heading2"])
        )

        elements.append(
            Paragraph(
                report["ai_review"].replace("\n", "<br/>"),
                styles["BodyText"]
            )
        )

        doc.build(elements)