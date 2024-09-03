import os
map="courses"
cwd=os.getcwd()
pathToCourses=os.path.join(cwd, map)
def nameOfCourse():
    while True:
        ans_continue=False
        ans="n"
        name=input("Enter the name of the course: ")
        if not ans_continue:
            ans = input(f'Is \"{name}\" the right name of the course (y/n)? ')
        if ans == "y" or ans == "yes":
            return name
def exist(name, path):
    name=name.lower()
    if os.path.isdir(os.path.join(path,name)):
        print("Dir does already exist!")
        return 1
    return 0
def createDir(name, path):
    name=name.lower()
    fullPath= os.path.join(path, name)
    print(f"Name of path{fullPath}")
    if not exist(name, path):
        os.mkdir(fullPath)
        return 1
    print(f"File {path} does already exist")
    return 0
def createFiles(name, path):
    name=name.lower()
    fullPath=os.path.join(path,name)
    pPExtensionHtml=f"{fullPath}.html"
    pPExtensionCss=f"{fullPath}.css"
    pPExtensionJs=f"{fullPath}.js"
    html=f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
                <!-- Links will be set via JavaScript below -->
            <link id="cssAll" rel="stylesheet">
            <link id="cssCourses" rel="stylesheet">
            <link id="cssTif083" rel="stylesheet">
            
        </head>
        <body>
            <div class="main">
                <div class="grid_container">
                    <div id="left_div">
                    </div>
                    <div id="right_div">
                    </div>
                </div>
            </div>
            <script>
                function getBaseUrl() {{
                const onGithub = window.location.hostname.includes('github.io');
                return onGithub ? '/darkfteksimpel/' : '../../';
                }}
                const baseUrl = getBaseUrl();
            </script>
            <script>
            // Once the DOM is fully loaded, set the correct paths for CSS and dynamically inject scripts
            document.addEventListener('DOMContentLoaded', function () {{
                document.getElementById('cssAll').href = baseUrl + 'all.css';
                document.getElementById('cssCourses').href = baseUrl + 'courses/courses.css';
                document.getElementById('cssTif083').href = baseUrl + 'courses/{name}/{name}.css';

                // Function to dynamically load script
                function loadScript(src) {{
                var script = document.createElement('script');
                script.src = src;
                script.async = false; // This preserves the execution order
                document.body.appendChild(script);
                }}

                // Load scripts dynamically
                loadScript(baseUrl + 'all.js');
                loadScript(baseUrl + 'courses/{name}/{name}.js');
            }});
            </script>
        </body>
        </html>


        """
    if not exist(name, path):
        with open(pPExtensionHtml, "w") as file:
            file.write(html)
        with open(pPExtensionCss, "w") as file:
            file.write("")
        with open(pPExtensionJs, "w") as file:
            file.write("")
        return 1
    return 0
def changeIndexFile(cwd, course):
    fullPath = os.path.join(cwd, "index.js")
    if exist(cwd, "index.js"):
        with open(fullPath, "r") as file:
            lines = file.readlines()
            firstLine = lines[0].strip()
            old = firstLine[:-2]
            newArray = f'{old},"{course}"];'
            lines[0] = newArray + '\n'

        with open(fullPath, 'w') as file:
            file.writelines(lines)
    else: 
        print("File does not exist")


def main(path):
    name=nameOfCourse().lower()
    createDir(name, path)
    pathToNew=os.path.join(path, name)
    createDir("files", pathToNew)#Makes the empty dir with all the files
    createFiles(name, pathToNew)
    print("Everything worked")
    changeIndexFile(cwd, name)
main(pathToCourses)
