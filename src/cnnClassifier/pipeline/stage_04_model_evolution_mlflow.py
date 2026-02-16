from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evolution_mlflow import Evaluation
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import EvaluationConfig
import dagshub
STAGE_NAME="Model Evolution with Mlflow Stage"



class ModelEvolutionMlflowPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        evaluation_config=config.get_evaluation_config()
        evaluation=Evaluation(evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()
        dagshub.init(repo_owner='mrhrasel232', repo_name='Kidney-Disease-Classification-Deep-Learning-Project', mlflow=True)

        # evaluation.log_into_mlflow()
        
if __name__=='__main__':
    try:
        logger.info(f">>>>stage {STAGE_NAME} started <<<<<")
        obj=ModelEvolutionMlflowPipeline()
        obj.main()
        logger.info(f">>>>stage {STAGE_NAME} completed <<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        