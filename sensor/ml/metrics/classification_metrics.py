from sensor.entity.artefacts import ClassificationMetricArtifact
from sensor.exception import SensorException
from sklearn.metrics import f1_score, roc_auc_score, recall_score
import os,sys

def get_classification_score(y_true, y_pred)->ClassificationMetricArtifact:
    try:
        model_f1_score = f1_score(y_true, y_pred)
        model_recall_score = recall_score(y_true, y_pred)
        model_roc_auc_score=roc_auc_score(y_true,y_pred)

        classsification_metric =  ClassificationMetricArtifact(f1_score=model_f1_score, roc_auc_score=model_roc_auc_score, recall_score=model_recall_score)
        return classsification_metric
    except Exception as e:
        raise SensorException(e,sys)