# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 13:23:40 2022

@author: Accubits
"""

import configparser

# CREATE OBJECT
config_file = configparser.ConfigParser()


config_file["INPUT_DATASET"]={
        "INPUT_DATASET_DIR":"input_data",
        "INPUT_COMPANY_DATASET" : "company_data.csv",
        "INPUT_PRODUCT_DATASET" : "product_data.csv"
        }

config_file["SOURCE_DATASET"]={
    "SOURCE_DATASET_DIR":"source_data",
        
    "DATA_DICTIONARY_FILE":"Data_Dictionary_PlanetX_ESP_Goal_Subject_Indicator.csv",
        
    }

config_file["OUTPUT_DATASET"]={
    
    "OUTPUT_DATASET_DIR":"output_data",
    
    "INDICATOR_TABLE_FILE":"0_indicators_raw.csv",
    
    "STANDARDIZATION_METHODS_FILE" :"0_standardization_methods.csv",
    
    "INPUT_COMPANY_DATASET_FILE" : "0_company_scores_raw.csv", 
    
    "INPUT_PRODUCT_DATASET_FILE" : "0_product_scores_raw.csv", 
    

    "STD_METHODS_FILE": "0_standardization_methods.csv",  
    
    
    "COMPANY_STATS_FILE": "0_company_stats.json",
    
    "COMPANY_FIX_LOGS_FILE" : "1_company_fix_logs.json", 
    
    "COMPANY_CLEANED_DATA_FILE" :"1_company_cleaned_data.csv",
    
    
    
    "PRODUCT_STATS_FILE":"0_product_stats.json",
    
    "PRODUCT_FIX_LOGS_FILE" : "1_product_fix_logs.json", 
    
    "PRODUCT_CLEANED_DATA_FILE" :"1_product_cleaned_data.csv",
    
    
    "COMPANY_INDICATOR_ZSCORE_FILE":"2_company_z_scores.csv",
        
    "PRODUCT_INDICATOR_ZSCORE_FILE":"2_product_z_scores.csv",
    
    
    "COMPANY_STANDARDS_CLEANED_FILE" : "3_company_standards_cleaned.csv",
    
    "COMPANY_MINIMUM_STANDARDS_LOG_FILE" : "3_company_minimum_standards_log.json",
    
    "PRODUCT_STANDARDS_CLEANED_FILE" : "3_product_standards_cleaned.csv",
    
    "PRODUCT_MINIMUM_STANDARDS_LOG_FILE" : "3_company_minimum_standards_log.json",
    
    
    "SUBJECT_VALUE_FILE":"4_subject_scores.csv",
    
    "SUBJECT_ZSCORE_FILE":"5_subject_z_scores.csv",
    
    "SUBJECT_SCORES_PERCENTILE_FILE" : "5_subject_scores_percentiles.csv",
    
    
    "ESP_VALUE_FILE":"6_esp_scores.csv",
    
    "ESP_ZSCORE_FILE":"7_esp_z_scores.csv",
    
    
    "ESP_PERCINTILE_FILE":"7_esp_scores_percentiles.csv",
    
    "FINAL_SCORES_FILE" : "8_final_scores.csv",
    
    "FINAL_Z_SCORE_FILE" : "9_final_z_scores.csv",
    "FINAL_SCORE_PERCENTILE_FILE" : "9_final_scores_percentiles.csv",
    
    "FINAL_STATS_FILE" : "final_stats.json"
    
    }

config_file["OUTPUT_METADATA"]={
    "OUTPUT_METADATA_DIR":"output_metadata",

    "COMPANY_INDICATORS_METADATA_FILE" : "company_indicators_stats.csv",

    "PRODUCT_INDICATORS_METADATA_FILE" : "product_indicators_stats.csv",    
    
    "COMPANY_PRODUCT_ESP_METADATA_FILE" : "company_product_esp_stats.csv"
    }


import os
# SAVE CONFIG FILE
with open(r"configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

from configparser import ConfigParser
  
configur = ConfigParser()

configur.read('configurations.ini')



source_dataset_dir = configur.get('SOURCE_DATASET','SOURCE_DATASET_DIR')

data_dictionary_goal_subject_indicator_file = configur.get('SOURCE_DATASET','DATA_DICTIONARY_FILE')



output_dataset_dir = configur.get('OUTPUT_DATASET','OUTPUT_DATASET_DIR')

company_indicator_zscore_file = configur.get('OUTPUT_DATASET','COMPANY_INDICATOR_ZSCORE_FILE')

product_indicator_zscore_file = configur.get('OUTPUT_DATASET','PRODUCT_INDICATOR_ZSCORE_FILE')


company_product_subject_value_file = configur.get('OUTPUT_DATASET','SUBJECT_VALUE_FILE')

company_product_subject_zscore_file = configur.get('OUTPUT_DATASET','SUBJECT_ZSCORE_FILE')

company_product_esp_value_file = configur.get('OUTPUT_DATASET','ESP_VALUE_FILE')

company_product_esp_zscore_file = configur.get('OUTPUT_DATASET','ESP_ZSCORE_FILE')


company_indicator_zscore_file_loc = os.path.join(output_dataset_dir, company_indicator_zscore_file)
product_indicator_zscore_file_loc = os.path.join(output_dataset_dir, product_indicator_zscore_file)

company_product_subject_value_file_loc = os.path.join(output_dataset_dir, company_product_subject_value_file)
             
company_product_subject_value_file_loc = os.path.join(output_dataset_dir, company_product_subject_value_file)
company_product_subject_zscore_file_loc = os.path.join(output_dataset_dir, company_product_subject_zscore_file)




