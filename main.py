from src.mlProject import logger
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME_Validation = "Data Validation  Stage"
try:
    
    logger.info(f">>>> stage {STAGE_NAME_Validation} started <<<<")
    data_validation= DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>> stage {STAGE_NAME_Validation} completed <<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e 