Read and Write JSON, YAML and TOML Data with Python
###################################################
:date: 2023-07-23 16:30
:author: lofipython
:category: coding, programming, python
:tags: python linters, linting tools, python RST linting, SQL linting, code linting
:slug: serializing-yaml-json-toml-data-python
:status: published


4. Pyyaml and yamllint: YAML is unavoidable as a configration staple in tons of modern software for its readability. These are two options I've tried to work with YAML and Python. I succeeded at my task with pyyaml and appreciated yamllint's instrospective linter prompts when trying to figure out why my YAML config was broken. 


5. tomllib and tomllint


.. code:: 

    pip install PyYAML
    

.. code-block:: python

    import pprint
    import yaml

    stream = open("config.yaml", "r")
    data = yaml.load(stream, Loader=yaml.CLoader)
    pprint.print(data)
    with open("new_config.yaml", "w") as yaml_file:
        yaml_file.write(yaml.dump(data, default_flow_style=False))

source: `Stack Overflow user Chetan <https://stackoverflow.com/questions/28557626/how-to-update-yaml-file-using-python>`__

