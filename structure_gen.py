import os

# Define the project structure
project_structure = {
    "pet-memories-webapp": {
        "public": [
            "index.html",
            "favicon.ico"
        ],
        "src": {
            "assets": [],
            "components": {
                "Auth": ["Login.js", "Register.js"],
                "Dashboard": ["UserDashboard.js"],
                "Memories": [
                    "MemoryForm.js", "MemoryList.js", "MemoryDetail.js",
                    "MemoryTimeline.js", "MemoryAlbum.js"
                ],
                "Pets": ["PetProfile.js", "PetMilestones.js"],
                "Community": ["CommunityFeed.js", "Post.js", "Comment.js"],
                "Layout": ["Header.js", "Footer.js", "Sidebar.js"]
            },
            "contexts": [
                "AuthContext.js", "MemoryContext.js",
                "PetContext.js", "CommunityContext.js"
            ],
            "hooks": ["useLocalStorage.js", "useAuth.js"],
            "pages": [
                "Home.js", "LoginPage.js", "RegisterPage.js",
                "DashboardPage.js", "MemoryPage.js", "PetPage.js", "CommunityPage.js"
            ],
            "utils": ["authUtils.js", "memoryUtils.js", "petUtils.js"],
            "App.js": "",
            "index.js": "",
            "styles.css": ""
        },
        ".gitignore": "",
        "package.json": "",
        "README.md": ""
    }
}

# Recursive function to create folders and files
def create_structure(base_path, structure):
    if isinstance(structure, dict):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_structure(path, content)
            elif isinstance(content, list):
                os.makedirs(path, exist_ok=True)
                for item in content:
                    with open(os.path.join(path, item), 'w') as f:
                        f.write("")
            elif isinstance(content, str):
                with open(path, 'w') as f:
                    f.write("")
    elif isinstance(structure, list):
        for item in structure:
            with open(os.path.join(base_path, item), 'w') as f:
                f.write("")

# Run the function
create_structure(".", project_structure)
print("Project structure created successfully.")
