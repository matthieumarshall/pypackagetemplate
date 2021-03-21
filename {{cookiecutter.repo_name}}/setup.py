import setuptools

version = {}
with open("src/{{cookiecutter.repo_name}}/version.py") as fp:
    exec(fp.read(), version)

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{{cookiecutter.repo_name}}",
    version=version["__version__"],
    author="Redslim",
    description="{{cookiecutter.repo_description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "{{cookiecutter.repo_name}}"},
    packages=[
        "{{cookiecutter.repo_name}}",
    ],
    python_requires=">=3.7",
)
