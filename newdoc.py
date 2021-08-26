from InquirerPy import inquirer
from InquirerPy.utils import color_print
from InquirerPy.separator import Separator
from InquirerPy.validator import EmptyInputValidator

from cli.ExchangeDocument import Language, ExchangeDocument
language = inquirer.select(
    message="In which language would you like to write the document?",
    choices=[
        {"name": "中文", "value": Language.ZH},
        {"name": "English", "value": Language.EN},
        Separator(),
        {"name": "Exit", "value": None}],
    max_height="60%"
).execute()

if language:
    category = inquirer.select(
        message="Which category does the document belong to?",
        choices=[
            "Administration",
            "Client Connectivity",
            "Compliance",
            "Development",
            "Distribution Lists",
            "Mail Flow",
            "Migration",
            "Public Folders",
            "Setup",
            Separator(),
            {"name": "Exit", "value": None}],
        default=None,
        max_height="60%"
    ).execute()
    
if language and category:
    title = inquirer.text(
        message="Enter the title of the file (e.g. 454 Temporary Authentication Failure):",
        validate=EmptyInputValidator()
        ).execute()

    if title:
        file_name = inquirer.text(
            message="Enter the name of the file (e.g. 454-temporary-authentication-failure):",
            validate=EmptyInputValidator()
            ).execute()
        
    if file_name:
        author = inquirer.text(
            message="Enter the name of the author (e.g. Molly Xu):",
            validate=EmptyInputValidator()
            ).execute()
    
    doc = ExchangeDocument(
        category=category,
        language=language,
        file_name=file_name,
        title=title,
        author=author)
    
    try:
        doc.create()
        color_print([('#00FF00', 'Document initialised 🚀')])
    except Exception:
        color_print([('#FF0000', 'Document failed to initialise ❌')])
        color_print([('#FF0000', Exception.message)])