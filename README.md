# CSS Wuxi MW Exchange Support Doc Site

[![Deploy to GitHub Pages](https://github.com/microsoft/exchange-css-docsite/actions/workflows/deploy-gh.yml/badge.svg)](https://github.com/microsoft/exchange-css-docsite/actions/workflows/deploy-gh.yml)

A Doc Site to host MW Exchange related supporting documents for CSS Wuxi.

## Prerequisite

- [Python 3](https://www.python.org/downloads/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/getting-started/#installation)

## Create a New Document

In order to create a new document, several conditions are needed to be satisfied:

- The document is written is proper Markdown syntax
- Metadata to describe the document is at the head of the document
- The document is placed in the right directory in `docs/`
- The path to the document is added to `mkdocs.yml` to be displayed on the navigation sidebar

A Python CLI has been implemented to automate some of the workflows. At the root directory, install the dependencies used by the CLI:

``` shell
pip3 install -r requirements.txt
```

Start the CLI and follow the wizard 🧙‍♂️:

``` shell
python3 newdoc.py
```

The CLI will:

1. Copy the template of the chosen language and paste to the chosen category directory with the given file name.

2. Create `yaml` metadata based on your input and add the metadata to the head of the newly created document.

3. Add the path to the document (relative to `docs/`) to the `nav` section of `mkdocs.yml`.

From there, you should complete the metadata and replace the placeholder contents with your actual contents. Commit your changes when the contents are ready.

## Developing

You can start the live-reloading docs server using:

``` shell
mkdocs serve
```

Any saved changes will be lively reloaded.

## Deployment

By default, any pushes to `main` branch at origin ([`microsoft/exchange-css-docsite` on GitHub](https://www.github.com/microsoft/exchange-css-docsite)) will trigger continuous deployment. However, manual deployment or creating new CD workflows to deploy to other platforms (e.g. Azure Static Web App) are possible.

### Continuous Deployment (CD)

A GitHub Actions workflow (`.github/workflows/deploy-gh.yml`)has been implemented to achieve continuous deployment. It will deploy the built static website to GitHub Pages.

### Manual Deployment

In rare cases (e.g. attempting to deploy to platforms other than GitHub Pages), you can manually build the site with:

``` shell
mkdocs build
```

The static website will be available at `site/` (ignored by `git`).

## Metadata

The metadata describes the document in an object-orientated approach. Currently, the metadata follows the following model:

``` yaml
---
title: An Example of the Markdown Metadata We Use
author: Tony Wu
description: This is a short description that will be displayed at the top of the page
kbIDs:
    - KB100001
    - KB100002
caseIDs:
    - 100001
    - 100002
date: 1970-01-01
---
```

### `title: string`

The title of the document, which will be rendered at the top of the document

### `author: string`

The author of the document

> In future development, maybe it could be extended to be the GitHub account(s) of the author(s) and render their GitHub avatar.

### `description: string`

A short description of the document, which will be rendered at the top of the document, following the title

### `kbIDs: string[]`

An array of Microsoft Knowledge Base ID of the Microsoft Knowledge Base articles this document is based on or is referring to

### `caseIDs: string[]`

An array of case ID of the cases this document is based on or is referring to

### `date: string`

The `ISOFormat` date string

> The CLI initialise the date with:
>
> ``` python
> import date from datetime
> date.today().isoformat()
> ```

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
