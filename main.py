from pathlib import Path
from dotenv import load_dotenv

# Load .env first so MLFLOW_TRACKING_* (and DagsHub auth) are set before any MLflow code runs
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline 
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evolution_mlflow import ModelEvolutionMlflowPipeline
import dagshub

STAGE_NAME="Data Ingestion Stage "


try:
    logger.info(f">>>>stage {STAGE_NAME} started <<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
except Exception as e:
    logger.exception(e)
    raise e;  

STAGE_NAME="Prepare Base Model Stage"

try:
    logger.info(f">>>>stage {STAGE_NAME} started <<<<<")
    obj=PrepareBaseModelTrainingPipeline()
    obj.main()  
    logger.info(f">>>>stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:  
    logger.exception(e)
    raise e;

STAGE_NAME="Model Training Stage"
try:
    logger.info(f">>>>stage {STAGE_NAME} started <<<<<")
    obj=ModelTrainingPipeline()
    obj.main()  
    logger.info(f">>>>stage {STAGE_NAME} completed <<<<<\n\nx=========x")   
except Exception as e:
    logger.exception(e)
    raise e;

STAGE_NAME="Model Evolution with Mlflow Stage"
try:
    
    logger.info(f">>>>stage {STAGE_NAME} started <<<<<")
    obj=ModelEvolutionMlflowPipeline()
    obj.main()
    logger.info(f">>>>stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e;