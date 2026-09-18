"""Build the final Task7 YOLO dataset from MakeSense labels."""

import argparse
import random
import shutil
import zipfile
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--images", type=Path, required=True)
    parser.add_argument("--labels-zip", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("final_dataset"))
    args = parser.parse_args()

    output = args.output.resolve()
    raw_labels = output.parent / "labels_from_makesense"
    if raw_labels.exists():
        shutil.rmtree(raw_labels)
    raw_labels.mkdir(parents=True)
    with zipfile.ZipFile(args.labels_zip) as archive:
        archive.extractall(raw_labels)

    images = sorted(args.images.glob("*.jpg"), key=lambda path: int(path.stem))
    random.Random(20260918).shuffle(images)
    val_names = {path.stem for path in images[:11]}
    # Preserve the existing split while excluding the color-distorted image.
    images = [path for path in images if path.stem != "32"]

    for split in ("train", "val"):
        (output / "images" / split).mkdir(parents=True, exist_ok=True)
        (output / "labels" / split).mkdir(parents=True, exist_ok=True)

    for image in images:
        split = "val" if image.stem in val_names else "train"
        shutil.copy2(image, output / "images" / split / image.name)
        source_label = raw_labels / f"{image.stem}.txt"
        target_label = output / "labels" / split / source_label.name
        if source_label.exists():
            shutil.copy2(source_label, target_label)
        else:
            target_label.touch()

    print(f"Prepared {len(images) - len(val_names)} training images and {len(val_names)} validation images.")
    print(f"Dataset: {output}")


if __name__ == "__main__":
    main()
