## About
This program allows you to extract information from a user's profile on GitHub, such as name, profile image, description, and total count of published repositories.

## Prerequisites
Before running the program, you need to have Python installed on your system. The program has been tested and developed using Python 3.

Additionally, you need to install the requests and beautifulsoup4 libraries. You can install these dependencies using the pip package manager. Run the following commands in the terminal to install the dependencies:

```
pip install requests
pip install beautifulsoup4
```

## How to Use

1. Clone the repository or download the program files to your computer.

2. Open a terminal and navigate to the directory where you saved the program files.

3. Run the program using the command python filename.py, where filename.py is the name of the program file.

4. The program will prompt you to enter the GitHub username for which you want to extract the information. Enter the username and press Enter.

5. The program will make a request to the user's profile on GitHub, extract the information, and display it in the terminal output.

6. The displayed information includes the name, profile image, description, and total count of published repositories for the user. If any information is not available in the profile, a corresponding message will be displayed.

## Example
Here's an example of using the program:

```yaml
$ python github_user_info_extractor.py
Github user: example_user
Name: John Doe
Profile Image: <https://example.com/avatar.jpg>
Description: Software developer passionate about coding.
Total repositories published: 50
```