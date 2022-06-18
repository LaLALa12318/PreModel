
import os.path as osp
PROJECT_PATH = osp.abspath(osp.join(osp.dirname(__file__), '..'))

DATA_PATH = osp.join(PROJECT_PATH, 'data')


MODEL_TYPE = {
    "TYPE": "YOLOv4"
}

CONV_TYPE = {"TYPE": "DO_CONV"}

ATTENTION = {"TYPE": "NONE"}

# train
TRAIN = {
    "DATA_TYPE": "Radar",
    "TRAIN_IMG_SIZE": 416,
    "AUGMENT": True,
    "BATCH_SIZE": 4,
    "MULTI_SCALE_TRAIN": True,
    "IOU_THRESHOLD_LOSS": 0.5,
    "YOLO_EPOCHS": 151,
    "Mobilenet_YOLO_EPOCHS": 120,
    "NUMBER_WORKERS": 0,
    "MOMENTUM": 0.9,
    "WEIGHT_DECAY": 0.0005,
    "LR_INIT": 1e-4,
    "LR_END": 1e-6,
    "WARMUP_EPOCHS": 2,  # or None
    "showatt": False
}

# val
VAL = {
    "TEST_IMG_SIZE": 416,
    "BATCH_SIZE": 1,
    "NUMBER_WORKERS": 0,
    "CONF_THRESH": 0.01,
    "NMS_THRESH": 0.45,
    "MULTI_SCALE_VAL": False,
    "FLIP_VAL": False,
    "Visual": False,
    "showatt": False
}

Radar={
    "NUM":1,
    "CLASSES":["Cavity"], #"Norm",
    "CONF_THRESH": 0.01,
    "NMS_THRESH": 0.1,   #非极大值抑制
    "MULTI_SCALE_VAL": False,
}

# model
MODEL = {
    "ANCHORS": [
        [
            (1.25, 1.625),
            (2.0, 3.75),
            (4.125, 2.875),
        ],  # Anchors for small obj(12,16),(19,36),(40,28)
        [
            (1.875, 3.8125),
            (3.875, 2.8125),
            (3.6875, 7.4375),
        ],  # Anchors for medium obj(36,75),(76,55),(72,146)
        [(3.625, 2.8125), (4.875, 6.1875), (11.65625, 10.1875)],
    ],  # Anchors for big obj(142,110),(192,243),(459,401)
    "STRIDES": [8, 16, 32],
    "ANCHORS_PER_SCLAE": 3,
}
