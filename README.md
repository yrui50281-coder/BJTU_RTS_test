# BJTU-RTS 视觉算法组学习记录

- 姓名：杨睿
- 学号：25511443
- 个人简历：[杨睿简历](resume.pdf)

## 学习报告

| 任务 | 文档 | 内容 |
| --- | --- | --- |
| Task1 | [Shell 学习报告](Task1-Shell.md) | 命令行操作、脚本、权限及管道 |
| Task2 | 各任务 Markdown 报告 | Markdown 文档编写实践 |
| Task3 | [Git 学习报告](Task3-Git.md) | 版本管理与 GitHub 提交 |
| Task4 | [CMake 学习报告](Task-4-CMake.md) | C++ 示例程序及构建过程 |
| Task5 | [OpenCV 学习报告](Task5-OpenCV.md) | 图像处理实践 |
| Task6 | [ROS1 学习报告](Task-6-ROS1.md) | 发布、订阅和自定义消息 |
| Task7 | [YOLOv8 学习报告](Task7-YOLO.md) | 官方球类数据标注、训练与结果 |

Task4 尚需补充 Ubuntu 编译验证；Task5 尚需补充源码编译 OpenCV 和 C++ 项目；Task6 尚需按指南补充三个 int64 消息及 launch 启动。Task8 为可选任务，正在准备。

## 仓库结构

| 路径 | 内容 |
| --- | --- |
| `resume.pdf` | 个人简历 |
| 根目录中的 `Task*.md` | 各任务的实验步骤、解释及结果 |
| 根目录中的 `task*.png` | 各任务运行及结果截图 |
| `cmake-hello/` | Task4 的 C++ 源文件与 CMake 配置 |
| `opencv-demo/` | Task5 的 Python 图像处理脚本、CMake 配置和输出图片 |
| `ros1-custom-message/message_publisher/` | Task6 发布节点功能包和自定义消息 |
| `ros1-custom-message/message_subscriber/` | Task6 订阅节点功能包 |
| `official-task7/` | Task7 正式 YOLOv8 实验，包含训练及数据整理脚本、数据配置 |
| `official-task7/final_dataset/` | 正式手动标注数据：44 张训练图、11 张验证图及对应标签 |
| `official-task7/train_output/official_balls/` | 训练参数、指标记录、曲线、预测图与 `weights/best.pt` |
| `yolo-demo/` | 早期 YOLO 练习材料；正式 Task7 以 `official-task7/` 和最新报告为准 |
| `.gitignore` | 构建目录和临时文件的忽略规则 |

训练配置中的本机绝对路径需要按运行电脑的位置调整。具体命令及实验限制见对应任务报告。
