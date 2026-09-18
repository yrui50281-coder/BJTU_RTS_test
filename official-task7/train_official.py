from pathlib import Path

from ultralytics import YOLO


def main():
    base_dir = Path(__file__).resolve().parent
    model = YOLO("yolov8n.pt")
    model.train(
        data=base_dir / "data.yaml",
        epochs=20,
        imgsz=640,
        device="cpu",
        workers=0,
        project=base_dir / "train_output",
        name="official_balls",
        exist_ok=True,
    )


if __name__ == "__main__":
    main()
