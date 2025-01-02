import pyperclip

def get_github_url():
    # Get the filepath from clipboard
    filepath = pyperclip.paste().strip()
    
    # Base GitHub repo URL
    base_url = "https://github.com/abhiisfamiliar/animations/blob/main"
    
    # Remove leading/trailing slashes and 'animations/' if present
    filepath = filepath.strip('/')
    if filepath.startswith('animations/'):
        filepath = filepath[len('animations/'):]
    
    # Construct the full GitHub URL
    github_url = f"{base_url}/{filepath}"
    
    # Copy the result back to clipboard
    pyperclip.copy(github_url)
    return github_url

if __name__ == "__main__":
    try:
        result = get_github_url()
        print(f"GitHub URL copied to clipboard: {result}")
    except Exception as e:
        print(f"An error occurred: {str(e)}") 