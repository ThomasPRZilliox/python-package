from setuptools import setup, find_packages

# setup(
#     name="my_package",
#     version="0.1.0",
#     package_dir={"": "src"},  # Tell setuptools packages are under src
#     packages=find_packages(where="src"),  # Find all packages under src
#     install_requires=[
#         # List your package dependencies here
#         # e.g., "requests>=2.25.1",
#     ],
#     extras_require={
#         "dev": [
#             "pytest>=6.0",
#             # Other development dependencies
#         ],
#     },
# )

setup(
    name="my_package",
    install_requires=[
        # List your package dependencies here
        # e.g., "requests>=2.25.1",
    ]
)