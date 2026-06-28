class Chunker:

    def __init__(self, project_files, chunk_size=4000):
        self.project_files = project_files
        self.chunk_size = chunk_size

    def create_chunks(self):

        chunks = []

        current_chunk = ""

        for project_file in self.project_files:

            file_text = (
                f"\n\nFILE: {project_file['path']}\n"
                f"{project_file['content']}\n"
            )

            if len(current_chunk) + len(file_text) > self.chunk_size:

                chunks.append(current_chunk)
                current_chunk = ""

            current_chunk += file_text

        if current_chunk:
            chunks.append(current_chunk)

        return chunks