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
                Paragraph(
                    f"{key}: {'Yes' if value else 'No'}",
                    styles["BodyText"]
                )
            )

        tech = report["technologies"]

        elements.append(
            Paragraph("<b>Technology Stack</b>", styles["Heading2"])
        )

        elements.append(
            Paragraph(
                f"Frontend: {tech['frontend']}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"Backend: {tech['backend']}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"Database: {tech['database']}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph("<b>Security Findings</b>", styles["Heading2"])
        )

        if report["security"]:

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
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
            ]))

            elements.append(security_table)

        else:

            elements.append(
                Paragraph(
                    "No security issues found.",
                    styles["BodyText"]
                )
            )

        elements.append(
            Paragraph(
                "<b>Complexity Findings</b>",
                styles["Heading2"]
            )
        )

        if report["complexity"]:

            complexity_data = [
                ["Issue", "IF", "Loops", "Returns", "File"]
            ]

            for issue in report["complexity"]:

                complexity_data.append([
                    issue["issue"],
                    str(issue["if_count"]),
                    str(issue["loop_count"]),
                    str(issue["return_count"]),
                    issue["file"]
                ])

            complexity_table = Table(complexity_data)

            complexity_table.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
                ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
                ("GRID", (0,0), (-1,-1), 1, colors.black),
                ("BACKGROUND", (0,1), (-1,-1), colors.beige),
                ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0,0), (-1,0), 8),
            ]))

            elements.append(complexity_table)

        else:
            elements.append(
                Paragraph(
                    "No complexity issues found.",
                    styles["BodyText"]
                )
            )
        
        elements.append(
            Paragraph(
                "<b>Duplicate Code Findings</b>",
                styles["Heading2"]
            )
        )

        if report["duplicate_code"]:

            duplicate_data = [
                ["Similarity", "File 1", "File 2"]
            ]

            for item in report["duplicate_code"]:

                duplicate_data.append([
                    f'{item["similarity"]}%',
                    item["file1"],
                    item["file2"]
                ])

            duplicate_table = Table(duplicate_data)

            duplicate_table.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (-1,0), colors.darkgreen),
                ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
                ("GRID", (0,0), (-1,-1), 1, colors.black),
                ("BACKGROUND", (0,1), (-1,-1), colors.beige),
                ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0,0), (-1,0), 8),
            ]))

            elements.append(duplicate_table)

        else:
            elements.append(
                Paragraph(
                "No duplicate code detected.",
                styles["BodyText"]
                )
            )
        
        elements.append(
            Paragraph(
                "<b>Dead Code Findings</b>",
                styles["Heading2"]
            )
        )

        if report["dead_code"]:

            dead_data = [
                ["Issue", "File"]
            ]

            for item in report["dead_code"]:

                dead_data.append([
                    item["issue"],
                    item["file"]
                ])

            dead_table = Table(dead_data)

            dead_table.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (-1,0), colors.orange),
                ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
                ("GRID", (0,0), (-1,-1), 1, colors.black),
                ("BACKGROUND", (0,1), (-1,-1), colors.beige),
                ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0,0), (-1,0), 8),
            ]))

            elements.append(dead_table)

        else:
            elements.append(
                Paragraph(
                    "No dead code detected.",
                    styles["BodyText"]
                )
            )
        
        elements.append(
            Paragraph(
                "<b>Naming Convention Findings</b>",
                styles["Heading2"]
            )
        )

        if report["naming"]:

            naming_data = [["Issue", "Name", "File"]]

            for item in report["naming"]:
                naming_data.append([
                    item["issue"],
                    item["name"],
                    item["file"]
                ])

            naming_table = Table(naming_data)

            naming_table.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (-1,0), colors.darkcyan),
                ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
                ("GRID", (0,0), (-1,-1), 1, colors.black),
                ("BACKGROUND", (0,1), (-1,-1), colors.beige),
                ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0,0), (-1,0), 8),
            ]))

            elements.append(naming_table)

        else:

            elements.append(
                Paragraph(
                    "No naming convention issues found.",
                    styles["BodyText"]
                )
         )
        
        elements.append(
            Paragraph("<b>AI Review</b>", styles["Heading2"])
        )

        for heading, content in report.get("ai_review", {}).items():

            elements.append(
                Paragraph(
                    f"<b>{heading}</b>",
                    styles["Heading3"]
                )
            )

            elements.append(
                Paragraph(
                    content.replace("\n", "<br/>"),
                    styles["BodyText"]
                )
            )

        doc.build(elements)