import os
from sensor.constant.s3_bucket import TRAINING__BUCKET_NAME

TARGET_COLUMN="class"
PIPELINE_NAME : str = "sensor"
ARTIFACT_DIR : str = "artifact"
FILE_NAME : str ="sensor.csv"

TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME="processing.pkl"
MODEL_FILE_NAME ="model.pkl"
SCHEMA_FILE_PATH =os.path.join("config","schema.yaml")
SCHEMA_DROP_COLS="drop_columns"
