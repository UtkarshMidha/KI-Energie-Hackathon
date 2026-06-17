import json
from pathlib import Path


class KnowledgeLoader:

    def __init__(self, kb_root="knowledge_base"):
        self.kb_root = Path(kb_root)

    def load_all(self):

        kb = {}

        for folder in self.kb_root.iterdir():

            if not folder.is_dir():
                continue

            kb[folder.name] = {}

            for file in folder.iterdir():

                if file.suffix == ".json":

                    with open(file, encoding="utf-8") as f:
                        kb[folder.name][file.stem] = json.load(f)

                elif file.suffix == ".md":

                    kb[folder.name][file.stem] = file.read_text(
                        encoding="utf-8"
                    )

        return kb