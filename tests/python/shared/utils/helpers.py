# Copyright (C) 2022 CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

import subprocess
from io import BytesIO
from typing import List

from PIL import Image

from shared.fixtures.init import get_server_image_tag


def generate_image_file(filename="image.png", size=(50, 50), color=(0, 0, 0)):
    f = BytesIO()
    image = Image.new("RGB", size=size, color=color)
    image.save(f, "jpeg")
    f.name = filename
    f.seek(0)

    return f


def generate_image_files(count, prefixes=None) -> List[BytesIO]:
    images = []
    for i in range(count):
        prefix = prefixes[i] if prefixes else ""
        image = generate_image_file(f"{prefix}{i}.jpeg", color=(i, i, i))
        images.append(image)

    return images


def generate_manifest(path: str) -> None:
    command = [
        "docker",
        "run",
        "--rm",
        "-u",
        "root:root",
        "-v",
        f"{path}:/local",
        "--entrypoint",
        "python3",
        get_server_image_tag(),
        "utils/dataset_manifest/create.py",
        "--output-dir",
        "/local",
        "/local",
    ]
    subprocess.check_output(command)
