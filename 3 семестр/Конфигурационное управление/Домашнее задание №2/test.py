import pytest
import os, subprocess
from PIL import Image
from main import parse, git_clone, get_commit_data, build_plantuml, visualize

def test_parse():
    visualizer_path, repository_url = parse()
    assert os.path.isfile(visualizer_path), "PlantUML.jar не найден по указанному пути"
    assert repository_url == "https://github.com/kriru/firstJava", "Некорректный URL репозитория"


def test_git_clone():
    _, repository_url = parse()
    repository_path = "pytest_repository"
    git_clone(repository_url, repository_path)
    assert os.path.exists(repository_path), "Репозиторий не был клонирован"
    assert os.path.isdir(repository_path), "Путь не является директорией"
    files = os.listdir(repository_path)
    assert len(files) > 0, "В клонированном репозитории нет файлов"


def test_get_commit_data():
    repository_path = "pytest_repository"
    commit_data = get_commit_data(repository_path)
    assert isinstance(commit_data, dict), "Результат не является словарём"
    assert len(commit_data) > 0, "Коммитов не обнаружено"
    for commit, files in commit_data.items():
        assert isinstance(commit, str), "Коммит должен быть строкой"
        assert len(files) > 0, "Коммит не содержит файлов"


def test_build_plantuml():
    commit_data = {
        "c1o2m3m4i5t": {"Main.java", "README.md"},
        "c6o7m8m9i0t": {"README.md"}
    }
    plantuml_text = build_plantuml(commit_data)
    assert "@startuml\npackage \"c1o2m3m4i5t\" as c1o2m3m4i5t {\n  [README.md] as c1o2m3m4i5t_README_md\n  [Main.java] as c1o2m3m4i5t_Main_java\n}\npackage \"c6o7m8m9i0t\" as c6o7m8m9i0t {\n  [README.md] as c6o7m8m9i0t_README_md\n}\nc1o2m3m4i5t --> c6o7m8m9i0t\nc6o7m8m9i0t --> c1o2m3m4i5t\n@enduml" in plantuml_text


def test_visualize():
    os.chdir("../")
    visualizer_path, _ = parse()
    commit_data = {
        "c1o2m3m4i5t": {"Main.java", "README.md"},
        "c6o7m8m9i0t": {"README.md"}
    }
    plantuml_text = build_plantuml(commit_data)
    plantuml_path = "dependencies.puml"
    os.chdir("pytest_repository")
    visualize(plantuml_text, visualizer_path, plantuml_path)
    assert os.path.exists(plantuml_path), "Файл диаграммы не создан"
    assert os.path.exists("dependencies.png"), "Изображение не сгенерировано"
    with Image.open("../dependencies.png") as img:
        assert img.size[0] > 0 and img.size[1] > 0, "Изображение имеет некорректный размер"