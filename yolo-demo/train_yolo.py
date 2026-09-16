from pathlib import Path

from ultralytics import YOLO


def main():
    base_dir = Path(__file__).resolve().parent
    model = YOLO(base_dir / "yolo11n.pt")
    model.train(
        data="coco8.yaml",
        epochs=3,
        imgsz=320,
        device="cpu",
        workers=0,
        project=base_dir / "train_output",
        name="experiment",
        exist_ok=True,
    )


if __name__ == "__main__":
    main()
