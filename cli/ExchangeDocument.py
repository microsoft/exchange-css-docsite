from datetime import date
import enum
import os
import shutil
import yaml

DESCRIPTION = "Article description that will be displayed on landing pages and in most search results"

KB_ID = ["KB12345","KB12346"]

CASE_ID = ["12345", "12346"]

class Language(enum.Enum):
    ZH = "zh"
    EN = "en"

class ExchangeDocument(object):
    """The class for Exchange support document"""

    def __init__(self,
                 category: str,  # TODO: enum for category
                 language: Language = Language.EN,
                 file_name: str = "template-doc", # TODO: generate file_name from title?
                 title: str = "Template Document",
                 author: str = "",
                ):
        self.category = category
        self.file_path = self._generate_file_path(category, file_name)
        self.template_file_path = self._generate_template_file_path(language)
        self.title = title
        self.author = author

    @classmethod
    def _generate_file_path(cls, category: str, file_name: str) -> os.PathLike:
        """Generate the file path to the new document.

        Args:
            category (str): the name of the category
            file_name (str): the file name of the new document

        Returns:
            os.PathLike: the absolute path to the new document
        """
        file_name += ".md"
        category_path = category.lower().replace(' ', '-')
        return os.path.join(os.getcwd(), "docs", category_path, file_name)

    @classmethod
    def _generate_template_file_path(cls, language: Language) -> os.PathLike:
        """Generate the file path to the Markdown template to be used.

        Args:
            language (Language): the language for the new document.

        Returns:
            os.PathLike: the absolute path to the template
        """
        template_file_name = "template.{lang}.md".format(lang = language.value)
        return os.path.join(os.getcwd(), "md-templates", template_file_name)

    def _copy_template_to_directory(self) -> None:
        """Copy the template file into destination directory with new file name."""
        shutil.copyfile(self.template_file_path, self.file_path)
        
    def _generate_md_metadata(self) -> str:
        """Generate the metadate for Markdown file, wrapped with `---` and ended linebreak"""
        metadata = {
            "title": self.title,
            "author": self.author,
            "description": DESCRIPTION,
            "kbIDs": KB_ID,
            "caseIDs": CASE_ID,
            "date": date.today().isoformat()
        }
        
        return yaml.dump(metadata, explicit_start=True, sort_keys=False)+"---\n\n"

    def _write_metadata_to_doc(self):
        """Write the fields to the metadata of the new Markdown document"""
        metadata_str = self._generate_md_metadata()
        with open(self.file_path, 'r') as old_file:
            old_data = old_file.read()

        with open(self.file_path, 'w') as new_file:
            new_file.write(metadata_str+old_data)
            
    def _update_mkdocs_yml(self):
        """Add the path of the new document relative to `docs/` to `mkdocs.yml`"""
        with open(os.path.join(os.getcwd(), 'mkdocs.yml'), 'r') as read_stream:
            mkdocs_config = yaml.safe_load(read_stream)
            
        relative_file_path = os.path.relpath(self.file_path, start=os.getcwd()+'/docs/')
        
        navs = mkdocs_config["nav"]
          
        for nav in navs:
            try:
                nav[self.category].append(relative_file_path)
                nav[self.category].remove('empty.md')
            except:
                pass

        with open(os.path.join(os.getcwd(), 'mkdocs.yml'), 'w') as write_stream:
            yaml.dump(mkdocs_config, write_stream, sort_keys=False)
        
    def create(self):
        """Create a new Exchange support document"""
        self._copy_template_to_directory()
        self._write_metadata_to_doc()
        self._update_mkdocs_yml()
            
if __name__ == '__main__':
    doc = ExchangeDocument("Distribution Lists", language=Language.ZH)
    print(doc.create())