import csv, os, subprocess
from PIL import Image

def parse(config_file ="config.csv"):
    paths = {}
    with open(config_file, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for line in reader:
            if len(line) >= 2:
                key, value = line[0].strip(), line[1].strip()
                if key == "visualizer_path":
                    paths[key] = os.path.abspath(value)
                else:
                    paths[key] = value
    return paths["visualizer_path"], paths["repository_path"]

def git_clone(repository_url, repository_path ="cloned_repository"):
    if not os.path.exists(repository_path):
        subprocess.run(["git", "clone", repository_url, repository_path], check=True)

def get_commit_data(repository_path ="cloned_repository"):
    os.chdir(repository_path)
    commit_data = {}
    result = subprocess.run(["git", "log", "--name-only", "--pretty=format:%H"], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    commit_hash = None
    flag = False
    for line in lines:
        if line.strip():
            if flag == False:
                commit_hash = line.strip()
                commit_data[commit_hash] = set()
                flag = True
            else:
                commit_data[commit_hash].add(line.strip())
        else:
            flag = False
    return commit_data

def build_plantuml(commit_data):
    plantuml_text = "@startuml\n"
    for commit, files in commit_data.items():
        node_id = commit.replace('-', '_')
        plantuml_text += f"package \"{commit}\" as {node_id} {{\n"
        for file in files:
            sanitized_file = file.replace('"', '')
            plantuml_text += f"  [{sanitized_file}] as {node_id}_{sanitized_file.replace('.', '_').replace('/', '_')}\n"
        plantuml_text += "}\n"
    for commit1, files1 in commit_data.items():
        node_id1 = commit1.replace('-', '_')
        for commit2, files2 in commit_data.items():
            node_id2 = commit2.replace('-', '_')
            if commit1 != commit2 and files1 & files2:
                plantuml_text += f"{node_id1} --> {node_id2}\n"
    plantuml_text += "@enduml"
    return plantuml_text

def visualize(plantuml_text, visualizer_path, plantuml_path ="../dependencies.puml"):
    with open(plantuml_path, 'w') as f:
        f.write(plantuml_text)
    subprocess.run(["java", "-jar", visualizer_path, plantuml_path])
    Image.open("../dependencies.png").show()

if __name__ == "__main__":
    visualizer_path, repository_url = parse()
    git_clone(repository_url)
    visualize(build_plantuml(get_commit_data()), visualizer_path)