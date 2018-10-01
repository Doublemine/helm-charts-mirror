# encoding: utf-8

import yaml
import requests
from contextlib import closing
import os
from urllib.parse import urlparse

# 转自https://www.zhihu.com/question/41132103/answer/93438156


def wget(url, file_name):
    with closing(requests.get(url, stream=True)) as response:
        chunk_size = 4096  # 单次请求最大值
        print(file_name+" downloading...")
        with open(file_name, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)


def main():
    root = os.path.join(os.getcwd(), 'docs')
    if not os.path.exists(root):
        os.mkdir(root)
    chart_url = os.environ.get(
        "CHARTS_URL", "https://kubernetes-charts.storage.googleapis.com/")
    repo_url = os.environ.get("GIT_REPO")
    if repo_url is None:
        raise RuntimeError("You must specify a git repo!")
    print("parse url...")
    p = urlparse(repo_url)
    git_user = p.path.split("/")[-2]
    repo_name = p.path.split("/")[-1].split(".")[0]
    default_mirror = "https://%s.github.io/%s/" % (git_user.lower(), repo_name)
    mirror_url = os.environ.get("MIRROR_URL", default_mirror)
    index_file = "index.yaml"
    wget(chart_url + index_file, index_file)
    with open(index_file) as f:
        index = yaml.load(f)
    entries = index["entries"]
    new = index.copy()
    for name, charts in entries.items():
        for chart, new_chart in zip(charts, new["entries"][name]):
            url = chart["urls"][0]
            tar_name = url.split("/")[-1]
            target = os.path.join(root, tar_name)
            new_chart["urls"][0] = "/".join(
                [mirror_url[:-1] if mirror_url.endswith("/") else mirror_url, tar_name])
            # datetime format issure
            new_chart["created"] = new_chart["created"].strftime('%Y-%m-%dT%H:%M:%S.%f000Z')
            if os.path.exists(target):
                continue
            wget(url, target)
    new["generated"] = new["generated"].strftime('%Y-%m-%dT%H:%M:%S.%f000Z')
    with open(os.path.join(root, "index.yaml"), "w") as f:
        yaml.dump(new, stream=f)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
        exit(1)
