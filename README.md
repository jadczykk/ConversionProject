# ConversionProject

## Overview
ConversionProject is a Python-based tool for converting data between JSON, XML, and YAML formats. It supports reading and writing files in these formats, making it easy to transform data for various use cases.

## Features
- Convert between JSON, XML, and YAML formats.
- Command-line interface for easy usage.
- Built-in error handling for invalid file formats.
- GitHub Actions workflow for building and uploading executables.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/jadczykk/ConversionProject.git
    cd ConversionProject
    ```
2. Install required Python packages:
    ```bash
    ./installResources.ps1
    ```

## Usage
Run the program with the following syntax:
```bash
python main.py <input_file> <output_file>
```
Example:
```bash
python main.py example.json example.xml
```

Supported file formats:
- `.json`
- `.xml`
- `.yaml` / `.yml`

## Build Executable
To build a standalone executable:
1. Run the `installResources.ps1` script to install dependencies.
2. Use PyInstaller:
    ```bash
    pyinstaller --onefile main.py
    ```

## GitHub Actions
The project includes a workflow (`.github/workflows/build-exe.yml`) to automate building and uploading executables. The workflow triggers on:
- Pushes to the `Trigger` branch.
- Manual dispatch.
- Weekly schedule (Monday at 8:00 AM UTC).

## File Structure
- `main.py`: Entry point for the program.
- `json_handler.py`: Handles JSON file operations.
- `yaml_handler.py`: Handles YAML file operations.
- `xml_handler.py`: Handles XML file operations.
- `example.*`: Example input files in JSON, XML, and YAML formats.
- `.gitignore`: Specifies files to ignore in version control.

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## Contact
For questions or feedback, please contact [your email or GitHub profile].
