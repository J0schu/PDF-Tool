from setuptools import setup, find_packages

setup(
    name="pdf-tool",
    version="0.2.0",
    # Use find_packages to handle the discovery
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    
    # This is often the missing piece for Nix builds with src layouts
    py_modules=[], 
    
    entry_points={
        'console_scripts': [
            # Ensure this matches your package structure
            # If __main__.py is directly in src, use:
            'pdf-tool = __main__:main',
        ],
    },
)
