 ```markdown
# LearnFetch

**LearnFetch** is a Python library designed to search and extract data from the 'Toda Matéria' website. It is useful for accessing information from articles and educational content programmatically.

## Installation

To install LearnFetch, use `pip`. Make sure you have Python 3.12.3 or higher installed.

```bash
pip install LearnFetch
```

## Usage

### Importing the Library

To get started with the library, import the `Pesquisador` class:

```python
from learnfetch import Pesquisador
```

### Creating an Instance and Performing a Search

Create an instance of the `Pesquisador` class and use the `get_response` method to perform searches:

```python
# Creating an instance of the Pesquisador class
researcher = Pesquisador()

# Performing a search
results = researcher.get_response("Photosynthesis")

# Displaying the results
print(results)
```

### Package Structure

The package structure includes:

- **`learnfetch/`**: Directory containing the package with the `pesquisador.py` module.
  - **`__init__.py`**: File that makes the directory a Python package.
  - **`pesquisador.py`**: Contains the `Pesquisador` class with methods for searching and extracting data.

- **`tests/`**: Directory for unit tests.
  - **`__init__.py`**: File that makes the directory a Python package.
  - **`test_pesquisador.py`**: File containing tests for the `Pesquisador` class.

## Complete Example

Here is a complete example of using the library:

```python
from learnfetch import Pesquisador

# Criando uma instância da classe Pesquisador
pesquisador = Pesquisador()

# Realizando uma busca
resultados = pesquisador.get_response("Redes neurais")

# Pegando um determinado dicionário da lista (por exemplo, o segundo)
if len(resultados) > 1:
        segundo_dicionario = resultados[1] 

        # Pegando um valor específico dentro de um dicionário
        conteudo = segundo_dicionario.get("content")
        print("Conteudo do Segundo Dicionário:")
        print(conteudo)
```

## Contributing

If you would like to contribute to the project, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/SaideOmaer1240/LearnFetch).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, you can reach out to:

- **Author**: Saíde Omar Saíde
- **Email**: saideomarsaideleon@gmail.com
```

### Explanation of Sections:

1. **Introduction**: Describes the purpose of the library.
2. **Installation**: Instructions for installing the library using pip.
3. **Usage**: Examples of how to import, create an instance, and use the library.
4. **Package Structure**: Explains the structure of the package directories and files.
5. **Complete Example**: A detailed example of how to use the library.
6. **Contributing**: Information on how to contribute to the project.
7. **License**: Details about the project license.
8. **Contact**: Contact information for support and suggestions.

Make sure to adjust the content as needed to reflect the specifics of your project.