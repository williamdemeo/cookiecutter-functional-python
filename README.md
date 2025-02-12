# Cookiecutter template for a simple functional Python project

## Usage

``` sh
cookiecutter https://github.com/williamdemeo/cookiecutter-functional-python
cd my_project
poetry install
pytest
mkdocs serve  # View documentation locally
```


## MkDocs

``` yaml
site_name: "{{ cookiecutter.project_name }}"
theme:
  name: material

plugins:
  - search
  - mkdocstrings:
      default_handler: python

nav:
  - Home: index.md
  - API Reference: api.md
```

**Explanation**.

1. `site_name: "{{ cookiecutter.project_name }}"`

   + Sets the documentation site’s title dynamically based on the project name.

2. `theme: material`

   + Uses the Material for MkDocs theme (modern and user-friendly).
   + If you haven't installed it, do so with `pip install mkdocs-material` or by adding
     the following to your `/etc/nixos/configuration.nix` file:

     ``` nix
     environment.systemPackages = with pkgs; [
       (python3.withPackages (p: [ p.pip p.cookiecutter p.docutils p.pyinstaller
                                   p.mkdocs p.mkdocs-material p.mkdocstrings-python
                                 ]
                             )
       )
     ```
3. `plugins:`
   + `search:` Enables a search bar in the documentation.
   + `mkdocstrings:` Automatically extracts and renders docstrings from Python files into Markdown documentation.
     + If you haven't installed it, install with `pip install mkdocstrings[python]`
       or using the NixOS configuration above (in 2).

4. `nav:`
   + Defines the navigation structure.
   + Maps `index.md` (home page) and `api.md` (auto-generated API docs).


### Preview the Docs
Once the project is generated, run `mkdocs serve` in a terminal window,
then open http://127.0.0.1:8000/ in your browser.

### Deployment
To deploy documentation to GitHub Pages, run `mkdocs gh-deploy`.
(Make sure you have initialized Git and pushed your repository first.)


 
